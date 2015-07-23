from django import forms


class Contact(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    body = forms.CharField(widget=forms.Textarea, label='Body')