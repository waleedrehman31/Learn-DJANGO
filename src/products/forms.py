from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title",
            }
        )
    )
    email = forms.EmailField()
    discription = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Discription",
                "class": "new_class_name two",
                "id": "my-id",
                "rows": 20,
                "cols": 120,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'discription',
            'price'

        ]
# pylint: disable=E1101

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "waleed" in title:
            return title
        else:
            raise forms.ValidationError("This is not valid title!")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("title")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not valid email!")
        return email


class RawProductForm(forms.Form):
    title = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your Title",
            }
        )
    )
    discription = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Discription",
                "class": "new_class_name two",
                "id": "my-id",
                "rows": 20,
                "cols": 120,
            }
        )
    )
    price = forms.DecimalField(initial=199.99)
