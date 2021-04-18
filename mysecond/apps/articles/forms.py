from django import forms

from .models import Article, Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("comment_text",)

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ("article_title", "article_text",)