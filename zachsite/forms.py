from django import forms

class SignupForm(forms.Form):
	"""
	For signup fields.
	"""
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	fname = forms.CharField(label='First Name', max_length=30, required=False)
	lname = forms.CharField(label='Last Name', max_length=30, required=False)
	email = forms.EmailField(label='Email', required=False)