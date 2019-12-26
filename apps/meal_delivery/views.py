import datetime

from django.shortcuts import redirect, render

from mdrm.resources.client_account.resource import ClientAccountResource, Profile
from mdrm.resources.delivery.resource import DeliveryWindow
from mdrm.resources.menu.resource import Meal
from mdrm.resources.order.models import Order
from mdrm.models import Allergen
from django.views.generic.base import  TemplateView
from django.views import View
from django.views.generic.edit import FormView
from apps.meal_delivery.forms import ProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from apps.portfolio.forms import RegistrationForm


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('md_index')


def login(request):
    if not request.POST:
        return render(request, 'meal_delivery/login.html')

    if request.POST['username'] and request.POST['password']:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            auth_login(request, user)
            return redirect(request.path_info)

    messages.error(request, 'Invalid Credentials')
    return redirect('md_login')


def register(request):
    if not request.POST:
        return render(request, 'meal_delivery/register.html')

    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return render(request, 'meal_delivery/register.html', {'form': form})

    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    auth_login(request, user)
    messages.success(request, 'Thank you for registering')
    return redirect('md_index')


class IntroView(TemplateView):
    template_name = 'meal_delivery/intro.html'

    def get_context_data(self, **kwargs):
        context = super(IntroView, self).get_context_data(**kwargs)
        context['page_number'] = kwargs['page']
        return context


class IndexView(TemplateView):
    template_name = 'meal_delivery/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['upcoming_windows'] = DeliveryWindow.objects.upcoming(datetime.datetime.now())
        return context


class ProfilePageView(FormView):
    template_name = 'meal_delivery/profile.html'
    form_class = ProfileForm
    success_url = '/meal_delivery/profile'

    def form_valid(self, form):
        profiles = Profile.object.filter(user_id=self.request.user.id)
        if profiles:
            profile = profiles[0]
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.address1 = form.cleaned_data['address1']
            profile.address2 = form.cleaned_data['address2']
            profile.city = form.cleaned_data['city']
            profile.state = form.cleaned_data['state']
            profile.zip_code = form.cleaned_data['zip_code']
            profile.save()
            profile.allergens.clear()
            profile.allergens.add(*form.cleaned_data['allergens'])
            messages.success(self.request, 'Profile Updated')
        else:
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
            messages.success(self.request, 'Profile Saved')
        return super(ProfilePageView, self).form_valid(form)

    def get_initial(self):
        profiles = Profile.object.filter(id=self.request.user.id)
        if not profiles:
            return {}
        return {
            'first_name': profiles[0].first_name,
            'last_name': profiles[0].last_name,
            'address1': profiles[0].address1,
            'address2': profiles[0].address2,
            'city': profiles[0].city,
            'state': profiles[0].state,
            'zip_code': profiles[0].zip_code,
            'allergens': [x.id for x in profiles[0].allergens.all()]
        }

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        profiles = Profile.object.filter(id=self.request.user.id)
        context['allergens'] = Allergen.objects.all()
        context['profile'] = profiles[0] if profiles else None
        return context


class DeliveryWindowView(TemplateView):
    template_name = 'meal_delivery/view_delivery_window.html'

    def get_context_data(self, **kwargs):
        context = super(DeliveryWindowView, self).get_context_data(**kwargs)
        window = None
        if kwargs['window_id']:
            window = DeliveryWindow.objects.get_window(kwargs['window_id'])
        context['window'] = window
        return context


class ViewMealView(TemplateView):
    template_name = 'meal_delivery/view_meal.html'

    def get_context_data(self, **kwargs):
        context = super(ViewMealView, self).get_context_data(**kwargs)
        associated_meals = None
        meals = None
        orders = None
        if 'meal_id' in kwargs:
            meals = Meal.objects.filter(id=kwargs['meal_id'])
            if meals:
                if 'window_id' in kwargs:
                    window = DeliveryWindow.objects.get(id=kwargs['window_id'])
                    associated_meals = Meal.objects.filter(serve_start__lte=window.date, serve_end__gte=window.date)\
                        .exclude(id=kwargs['meal_id'])

                    orders = Order.objects.filter(meal=meals[0], delivery_window=window)
        context['meal'] = meals[0] if meals else None
        context['associated_meals'] = associated_meals if associated_meals else None
        context['window_id'] = kwargs['window_id'] if 'window_id' in kwargs else None
        context['order'] = orders[0] if orders else None
        return context


class AppendToOrder(View):
    def dispatch(self, request, *args, **kwargs):
        if request.POST:
            if 'meal_id' in request.POST and 'window_id' in request.POST:
                # check if order exists first
                orders = Order.objects.filter(user= request.user,
                                              delivery_window_id = request.POST['window_id'],
                                              meal_id=request.POST['meal_id'])
                if orders:
                    order = orders[0]
                    order.quantity = request.POST.get('quantity')
                    order.save()
                    messages.success(request, 'Order Updated')
                else:
                    order = Order.objects.create(quantity= request.POST.get('quantity'),
                                                 user=request.user,
                                                 delivery_window_id=request.POST['window_id'],
                                                 meal_id=request.POST['meal_id']
                                                 )
                    messages.success(request, 'Order Saved')
        return redirect('md_index')


class MyDeliveriesView(TemplateView):
    template_name = 'meal_delivery/my_deliveries.html'

    def get_context_data(self, **kwargs):
        context = super(MyDeliveriesView, self).get_context_data(**kwargs)
        grouped_orders = {}
        total=0
        for order in Order.objects.filter(user=self.request.user):
            if not order.delivery_window.date in grouped_orders:
                grouped_orders[order.delivery_window.date] = {
                    'delivery_window': order.delivery_window,
                    'orders': []
                }
            order.total = order.quantity * order.meal.price
            total += order.total
            grouped_orders[order.delivery_window.date]['orders'].append(order)
        deliveries = []
        for order in grouped_orders.values():
            deliveries.append(order)
        context['deliveries'] = deliveries
        context['total'] = total
        return context


class RemoveOrder(View):
    def dispatch(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            orders = Order.objects.filter(id=kwargs['pk'])
            if orders:
                orders[0].delete()
                messages.success(request, 'Order has been removed')
        return redirect(request.META.get('HTTP_REFERER', '/'))


class CheckoutView(TemplateView):
    template_name = 'meal_delivery/checkout.html'

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        grouped_orders = {}
        for order in Order.objects.filter(user=self.request.user):
            if not order.delivery_window.date in grouped_orders:
                grouped_orders[order.delivery_window.date] = {
                    'delivery_window': order.delivery_window,
                    'orders': []
                }
            grouped_orders[order.delivery_window.date]['orders'].append(order)
        deliveries = []
        for order in grouped_orders.values():
            deliveries.append(order)
        context['deliveries'] = deliveries
        return context