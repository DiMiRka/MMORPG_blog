from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = field.help_text


class RegisterForm(PlaceholderForm, UserCreationForm):
    email = forms.EmailField(label='', help_text="Email")
    first_name = forms.CharField(label='', help_text="First name")
    last_name = forms.CharField(label='', help_text="Last name")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Username'
        self.fields['username'].label = ''
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = 'Password'
        self.fields['password2'].help_text = 'Password confirmation'
        self.fields['password2'].label = ''

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)


class OneTimeCode(models.Model):
    code = models.CharField(max_length=6)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
