from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Task Title', max_length=100)
    description = forms.CharField(label='Task Description', widget=forms.Textarea)