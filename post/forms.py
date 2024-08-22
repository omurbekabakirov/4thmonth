from django import forms


class PostForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField()
    content = forms.CharField()
    rating = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        if title == 'python':
            forms.ValidationError('title cannot be python')
        return cleaned_data
