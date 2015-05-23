from django import forms

class IncidentLog(forms.Form):
    your_email = forms.EmailField(label='Your email')
    name = forms.CharField(label='Name(s)', max_length=100, required=False)
    location = forms.CharField(label='Location', max_length=100, required=False)
    context = forms.CharField(label='Context/Situation')
    quote = forms.CharField(label='Quote')
    tags = forms.CharField(label='Tags', max_length=50, required=False)
