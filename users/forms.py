from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        label="Contraseña"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "form-control"}),
        label="Confirma tu contraseña"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'tel', 'direction']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control", 'required': "required", 'id': "name"}),
            'first_name': forms.TextInput(attrs={'class': "form-control", 'required': "required", 'id': "paterno"}),
            'last_name': forms.TextInput(attrs={'class': "form-control", 'required': "required", 'id': "materno"}),
            'email': forms.EmailInput(attrs={'class': "form-control", 'required': "required", 'id': "email"}),
            'tel': forms.TextInput(attrs={'class': "form-control", 'required': "required", 'id': "tel"}),
            'direction': forms.Textarea(attrs={'class': "form-control", 'required': "required", 'id': "message"}),
        }
