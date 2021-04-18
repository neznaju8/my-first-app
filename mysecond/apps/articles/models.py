import datetime
from django.db import models
from django.urls import reverse


class Article(models.Model):
	article_title = models.CharField('Название статьи', max_length = 200)
	article_text = models.TextField('Текст статьи')
	article_date = models.DateTimeField('Дата публикации')
	article_author = models.CharField('Имя автора', max_length = 50)
	url = models.SlugField(verbose_name = 'slug', max_length = 160, unique = True, default = '')
	draft = models.BooleanField('Черновик', default = False)

	def __str__(self):
		return self.article_title

	def get_absolute_url(self):
		return reverse('article_detail', kwargs = {'slug': self.url})

	def get_comment(self):
		return self.comment_set.filter(parent__isnull = True)

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

class Comment(models.Model):
	comment_author = models.CharField('Имя автора', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 200)
	comment_image = models.ImageField(
		'Изображение автора коммента', upload_to = 'comment_image/', null = True
	)
	comment_date = models.DateTimeField('Дата отправки комментария', null = True)
	comment = models.ForeignKey(
		Article, verbose_name = 'Статья', on_delete = models.CASCADE
	)
	parent = models.ForeignKey(
		'self', verbose_name = 'Родитель', on_delete = models.SET_NULL, blank = True,
		null = True, related_name = 'comments'
	)

	def __str__(self):
		return self.comment_author

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'

