from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    
    """
    Class Meta provides additional customization for the front-end display
    of the form, from Class Meta labels can be changed, as well as provide
    better customization towards the presentation of the form

    All form fields are considered required by default unless specified otherwise.
    This can be changed by adding 'required=False' when defining a field
    """

    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'text': 'Write your thoughts here:'
        }

    """
    An example of a method that filters unwanted behavior from the title field
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We only accept notes about Django!")
        return title
    """