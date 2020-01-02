from django import forms
from mdrm.models import Profile, Allergen


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=100)
    address1 = forms.CharField(max_length=200)
    address2 = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=25)

    allergens = forms.ModelMultipleChoiceField(queryset=Allergen.objects.all(), required=False)

    class Meta:
        model = Profile
        fields=['first_name', 'last_name', 'address1', 'address2', 'city', 'state', 'zip_code', 'allergens']

    def clean(self):
        pass