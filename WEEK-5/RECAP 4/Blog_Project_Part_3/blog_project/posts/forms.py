from django import forms 

from posts.models import Post
from posts.models import Comment 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        