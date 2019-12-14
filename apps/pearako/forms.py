from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean(self):
        if not 'username' in self.cleaned_data:
            raise ValidationError('Username Required')
        elif User.objects.filter(username=self.cleaned_data['username']):
            raise ValidationError('That username is already being used')

        if not self.cleaned_data['email']:
            raise ValidationError('Email required')

        if not 'password1' in self.cleaned_data or not 'password2' in self.cleaned_data:
            raise ValidationError('Password and confirmation password are both required')
        elif self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise ValidationError('Password and confirmation passwords do not match')