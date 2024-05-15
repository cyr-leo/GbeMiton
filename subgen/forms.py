from django import forms


class SubgenForm(forms.Form):

    vidlink = forms.CharField(max_length=3000)