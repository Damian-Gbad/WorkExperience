from django import forms 

class CreatNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    password = forms.CharField(label="password", max_length=200)
    over_18 = forms.BooleanField(required=False)
