from django import forms
from ghostpost.models import GhostPost

class GhostPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = GhostPost
        fields = [
            'isBoast',
            'content'
        ]