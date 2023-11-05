from django import forms

class Urldata(forms.Form):
    url = forms.CharField(label="URL")