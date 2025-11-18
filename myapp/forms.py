from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label='Task Title', max_length=100, widget=forms.TextInput(attrs={ 'class': 'input'}))
    description = forms.CharField(label='Task Description', widget=forms.Textarea(attrs={ 'class': 'input'}))

class ProjectForm(forms.Form):
    name = forms.CharField(label='Project Name', max_length=100, widget=forms.TextInput(attrs={ 'class': 'input'}))