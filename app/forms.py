from django import forms
from .models import User, EncodedText

class UserForm(forms.ModelForm):
    ENCODING_CHOICES = [
        ('Base64', 'Base64'),
        ('Hash', 'Hash'),
    ]
    region = forms.ChoiceField(choices=ENCODING_CHOICES, label="Select Encoding Method")

    class Meta:
        model = User
        fields = ['name', 'region']

class EncodedTextForm(forms.ModelForm):
    class Meta:
        model = EncodedText
        fields = ['original_text']
