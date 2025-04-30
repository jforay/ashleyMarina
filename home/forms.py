from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
