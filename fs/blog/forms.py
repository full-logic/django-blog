from django import forms

from .models import Comment


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=255)
	email = forms.EmailField()
	to = forms.EmailField()
	comments = forms.CharField(
		required=False,
		widget=forms.Textarea
	)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
	query = forms.CharField()
