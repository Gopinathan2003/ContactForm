from django import forms


class ContactForm(forms.Form):
    name = forms.CharField( label='Name', max_length=50, required=True)
    email = forms.EmailField( label='Email', required=True)
    message = forms.CharField( max_length=300, label='Message', required=True)