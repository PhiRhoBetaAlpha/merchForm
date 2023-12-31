from django import forms, ModelForm
from . import models

class MerchForm(ModelForm):
    #this will be the main form for collecting data
    your_name = forms.CharField(label="Your name", max_length=100) #example

    #for each merch that exists, there should be an option to see/buy it
    class Meta:
        model = models.Shirts
        fields = ["name", "price", "img_path"]