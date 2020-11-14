from django import forms
from .models import Question,Participant

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

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['selected_option']
        # fields = ['selected_option']
        # widgets = {
        # 'selected_option':forms.MultipleChoiceField(
        #     choices = [(1,1),(2,2),(3,3),(4,4)]
        #  )
        #  }
        