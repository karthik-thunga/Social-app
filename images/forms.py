from django import forms
from .models import Image
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widget = {
            'url' : forms.HiddenInput,
        }
    
    def clean_url(self):
        url =self.cleaned_data['url']
        allowed_format=['jpeg','jpg']
        url_format = url.rsplit('.', 1)[1].lower()

        if url_format not in allowed_format:
            raise forms.ValidationError("Given url does not contain valid Image format")

        return url

    def save(self, force_insert=False, force_update=False, commit=True):

        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data['url']
        image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.', 1)[1])

        # Downloading the image 
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False )
        
        if commit:
            image.save()

        return image

