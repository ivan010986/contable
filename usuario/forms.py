from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):    
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'
        widgets = {
            'uen': forms.CheckboxSelectMultiple,
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'regional', 'uen')
        widgets = {
            'uen': forms.CheckboxSelectMultiple,
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email