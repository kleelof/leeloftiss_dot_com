import datetime
from mdrm.resources.client_account.resource import ClientAccountResource, Profile
from mdrm.resources.delivery.resource import DeliveryWindow
from mdrm.resources.menu.resource import Meal
from mdrm.models import Allergen
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from apps.meal_delivery.forms import ProfileForm
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'meal_delivery/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['upcoming_windows'] = DeliveryWindow.object.upcoming(datetime.datetime.now())
        return context



class ProfilePageView(FormView):
    template_name = 'meal_delivery/profile.html'
    form_class = ProfileForm
    success_url = '/meal_delivery/profile'

    def form_valid(self, form):
        profiles = Profile.object.filter(user_id=self.request.user.id)
        if profiles:
            form.instance = profiles[0]
            form.save(commit=True)
        else:
            obj = form.save(commit=False)
            obj.user = self.request.user
            obj.save()
        messages.success(self.request, 'Profile Updated')
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
            'allergens': profiles[0].allergens
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
            window = DeliveryWindow.object.get_window(kwargs['window_id'])
        context['window'] = window
        return context


class ViewMealView(TemplateView):
    template_name = 'meal_delivery/view_meal.html'

    def get_context_data(self, **kwargs):
        context = super(ViewMealView, self).get_context_data(**kwargs)
        meal = None
        if kwargs['meal_id']:
            meals = Meal.objects.filter(id=kwargs['meal_id'])
            if meals:
                meal = meals[0]
        context['meal'] = meal
        return context