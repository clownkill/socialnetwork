from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': 3,
                   'placeholder': 'Say Something...'}
        ))

    class Meta:
        model = Post
        fields = ['body']


class CommentFrom(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'rows': 3,
                   'placeholder': 'Say Something...'}
        )
    )

    class Meta:
        model = Comment
        fields = ['comment']
