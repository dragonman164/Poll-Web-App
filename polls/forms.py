from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question','no_of_options']
        widgets = {
            'question':forms.TextInput(attrs= {'class':'form-control'}),
            'no_of_options':forms.NumberInput(attrs= {'class':'form-control'}),

            
        }
