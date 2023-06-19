from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'image', 'message', 'blog']
        exclude = ('blog', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control'
        })

    def clean(self):
        self.cleaned_data['message'] = self.cleaned_data['message'].capitalize()
        if self.cleaned_data['name']:
            self.cleaned_data['name'] = self.cleaned_data['name'].title()

        return None

