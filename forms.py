from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email','phone')