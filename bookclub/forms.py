from django import forms
from bookclub.models import Discussion

class DiscussionForm(forms.ModelForm):

    class Meta:
        model = Discussion
        fields = ('opinion',)
