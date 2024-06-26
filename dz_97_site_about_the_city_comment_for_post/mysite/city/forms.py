from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Введите текст комментария",
                "rows": 5
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ("comment",)