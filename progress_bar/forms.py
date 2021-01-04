from django import forms


class FilesForm(forms.Form):
    files = forms.FileField()
