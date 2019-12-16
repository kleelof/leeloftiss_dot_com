from mdrm.resources.client_account.resource import ClientAccountResource, Profile
from mdrm.models import Allergen
from django.views.generic.base import View, TemplateView
from django.views.generic.edit import FormView
from apps.meal_delivery.forms import ProfileForm


class IndexView(TemplateView):
    template_name = 'meal_delivery/index.html'


class ProfilePageView(FormView):
    template_name = 'meal_delivery/profile.html'
    form_class = ProfileForm
    success_url = '/profile/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()


    def form_invalid(self, form):
        t=1

    def get_initial(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super(FormView, self).get_context_data(**kwargs)
        profiles = Profile.object.filter(id=self.request.user.id)
        context['allergens'] = Allergen.objects.all()
        context['profile'] = profiles[0] if profiles else None
        return context

