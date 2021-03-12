from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title eingeben"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs=
    {
        "class": "new class name",
        "placeholder": "Beschreibung eingeben",
        "id": "my id for textarea",
        "rows": 20,
        "cols": 120

    }))

    class Meta:
        model = Post
        fields = ["title",
                  "description", ]
