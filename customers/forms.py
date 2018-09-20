from django import forms
from .models import Customers
#from django.contrib.auth.models import User
#from django.contrib.auth import views
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ['name', 'age','email']

""" 
class UserRegistration(forms.ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget = forms.PasswordInput())
        confirm_password = forms.CharField(widget = forms.PasswordInput())
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def confirm_password_cleaned(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Paswords do not match")
        return confirm_password
 """