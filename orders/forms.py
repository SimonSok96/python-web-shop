from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city']
        labels = {
            'first_name': _('First name'), 
            'last_name': _('Last name'), 
            'email': "e-mail", 
            'address': _('Address'), 
            'city': _('City'),
            }
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email
        for field in self.fields.values():
            field.widget.attrs.update({"placeholder": field.label, 'class': 'w-75'})
    