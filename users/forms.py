from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    company = forms.CharField(label="Company", max_length=30)
    address = forms.CharField(label="Address", max_length=30)
    postcode = forms.CharField(label="Postcode", max_length=10)
    country = forms.CharField(label="Country", max_length=20)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'company', 'address', 'postcode', 'country')
