from django.forms import ModelForm
from photos.models import Photo,Category

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['category','description','image']