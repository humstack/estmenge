from django import forms


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = forms.CharField(max_length=50, label="Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=50, label="Subject", widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class': 'form-control'}))


