from django import forms
from .models import Content

class NewForm (forms.ModelForm):
    class Meta:
        
        model = Content

        fields =[
            "Vocabulary",
            "image",
            "content",
            "translation",
        ]