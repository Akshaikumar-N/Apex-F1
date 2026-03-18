from django import forms
from .models import Rating, Prediction

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 10, 'class': 'form-control'})
        }

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = ['driver']
        widgets = {
            'driver': forms.Select(attrs={'class': 'form-control'})
        }
