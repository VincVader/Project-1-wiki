from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Search",required= False, widget=forms.TextInput(attrs={'placeholder':'Search Encyclopedia'}))

markdown = forms.CharField(
    label='Markdown content',
    required=False,
    widget=forms.Textarea(attrs={
        'size': 50,
        'placeholder': 'Enter markdown content...',

}))

class BaseForm(forms.Form):
    title = forms.CharField(label='Title', required=True)
    content = markdown


class EditForm(forms.Form):
    title = forms.CharField(label='Title', required=False, widget=forms.HiddenInput)
    content = markdown


