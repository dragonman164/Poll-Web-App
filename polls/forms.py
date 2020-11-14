from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question','option1','option2','option3','option4']
        widgets = {
            'question':forms.TextInput(attrs= {'class':'form-control'}),
            'option1':forms.TextInput(attrs ={'class':'form-control'}),
            'option2':forms.TextInput(attrs ={'class':'form-control'}),
            'option3':forms.TextInput(attrs ={'class':'form-control'}),
            'option4':forms.TextInput(attrs ={'class':'form-control'}),        
        }

