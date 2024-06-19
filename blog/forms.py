from django import forms
from .models import Comment , Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50}),  # Customizing textarea attributes
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description' , 'img']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px;',
                'placeholder': 'Enter the title'
            }),
            'description': forms.Textarea(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px; resize: vertical; height: 150px;',
                'placeholder': 'Enter the description'
            }),
            'image': forms.ClearableFileInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px; font-size: 16px;',
            }),
        }
       