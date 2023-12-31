from django import forms
from . import models

class MerchForm(forms.Form):
    #this will be the main form for collecting data
    your_name = forms.CharField(label="Your name", max_length=100) #example

    #idk if working. will have to test
    for shirt in models.Shirts:
        forms.IntegerField(label = shirt.name+" quaintity", min_value=1, widget=forms.Select())
    #for each merch that exists, there should be an option to see/buy it
