# from django import forms
from django import forms



# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class ProfileForm(forms.Form):
   picture = forms.ImageField()