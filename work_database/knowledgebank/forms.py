from django import forms
from knowledgebank import models


class NewCountry(forms.Form):
    country = forms.CharField(label='Country', max_length=64)


class NewClient(forms.Form):
    client = forms.CharField(label='Client', max_length=64)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = models.Question
        fields = ['content']
        widgets = {
            'content': forms.Textarea()
        }


class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea, label='')
