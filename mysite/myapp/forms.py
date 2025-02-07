from django import forms
class contactForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=100,required=True)
    message = forms.CharField(widget=forms.Textarea,required=True)