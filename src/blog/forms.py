from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title",
            }
        )
    )
    content = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Content",
                "rows": 20,
                "cols": 120,
            }
        )
    )

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'

        ]
