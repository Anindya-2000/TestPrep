from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime

EXAMS=[
    ('JEE Mains','JEE Mains'),
    ('JEE Advanced','JEE Advanced'),
    ('KVPY','KVPY'),
    ('Bitsat','Bitsat')
]

TYPE_OF_QUESTIONS=[
    ('SingleCorrect','SingleCorrect')
]

SINGLE_CORRECT_OPTIONS=[
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D')
]

class CreateForm(forms.Form):
    exam=forms.ChoiceField(label="Exam",initial=('JEE Mains','JEE Mains'),choices=EXAMS, widget=forms.Select(attrs={'class': 'custom-select category', 'required': 'true'}))
    year=forms.IntegerField(label="Year ",widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2000', 'required': 'true'}))
    details=forms.CharField(label="Details ",widget=forms.TextInput(attrs={'class': 'input-line full-width',}))
    typeofq=forms.ChoiceField(label="Question Type",initial=('SingleCorrect','SingleCorrect'),choices=TYPE_OF_QUESTIONS, widget=forms.Select(attrs={'class': 'custom-select category', 'required': 'true'}))
    numberOfquestion=forms.IntegerField(label="Enter number of questions ",widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90', 'required': 'true'}))
# self.fields['question_%d' % i] = forms.ImageField(widget=forms.HiddenInput())
class UploadQuestions(forms.Form):
    def __init__(self,extra, *args, **kwargs):
        # extra = kwargs.pop('extra')
        super(UploadQuestions, self).__init__(*args, **kwargs)
        for i in range(extra):
            self.fields['question_number_%d' % i]=forms.IntegerField(label="Enter question number ",initial=i+1,widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '1'}))
            self.fields['question_%d' % i] = forms.ImageField(label="Select the Image",initial='1.png')
            self.fields['correct_answer_%d' % i] = forms.ChoiceField(label="Select the correct Option",initial=('A','A'),choices=SINGLE_CORRECT_OPTIONS, widget=forms.Select(attrs={'class': 'custom-select category', 'required': 'true'}))
