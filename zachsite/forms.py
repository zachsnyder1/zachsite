"""
Forms for zachsite app.
"""

from django import forms

class SignupForm(forms.Form):
    """
    For signup fields.
    """
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    email = forms.EmailField(label='Email', required=False)
