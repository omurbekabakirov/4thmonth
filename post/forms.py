from django import forms

from post.models import Tags


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


class SearchForm(forms.Form):
    search = forms.CharField(required=False,
                             max_length=100,
                             min_length=1,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control',
                                        'placeholder': 'Search'}
                             ))
    tag = forms.ModelMultipleChoiceField(
        required=False, queryset=Tags.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    orderings = (
        ('title', 'title'),
        ('-title', 'title(in backwards)'),
    )
    ordering = forms.ChoiceField(choices=orderings,
                                 required=False,
                                 widget=forms.Select(attrs={'class': 'form-control'})
                                 )
