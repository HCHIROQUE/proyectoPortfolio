from django import forms
from .models import aniade_item

# creating a form
class InputForm(forms.Form):
    username = forms.CharField(max_length = 256)
    password = forms.CharField()

class aniade_item_forms(forms.Form):
    class Meta:
        model = aniade_item
        fields = ["titulo_proyecto","descripcion_proyecto","tags","url_github"]