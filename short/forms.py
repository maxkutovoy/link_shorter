from django.forms import ModelForm, TextInput, SlugField

from .models import Link


class LinkForm(ModelForm):
    slug = SlugField(
        max_length=255,
        required=False,
        widget=TextInput(
            attrs={
                'placeholder': 'Short URL'
            }
        )
    )

    class Meta:
        model = Link
        fields = ['full_link', 'slug']

        widgets = {
            'full_link': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'URL',
                    'length': '500',
                }
            ),
        }
