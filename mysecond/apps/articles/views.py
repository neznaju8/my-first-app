from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.base import View

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from datetime import timezone, datetime


class ArticleAll(ListView):
	model = Article
	queryset = Article.objects.filter(draft = False)
	template_name = "articles/article_all.html"
	paginate_by = 5

def article_list(request):
	articles = Article.objects.filter(draft = False).order_by('-id')[:15]
	return render(request, "articles/article_list.html", {"article_list": articles})

def article_detail(request, slug):
	article = Article.objects.filter(draft = False).get(url = slug)
	return render(request, "articles/article_detail.html", {"article": article})

def leave_comment(request, pk):
	form = CommentForm(request.POST)
	comment = Article.objects.get(id = pk)
	if form.is_valid():
		form = form.save(commit = False)
		if request.POST.get('parent', None):
			form.parent_id = int(request.POST.get('parent'))
		form.comment = comment
		form.comment_date = datetime.now()
		if request.user.first_name:
			form.comment_author = request.user.first_name
		else:
			form.comment_author = request.user
		form.save()
	return redirect(comment.get_absolute_url())

def article_post(request):
	if request.method == "POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form = form.save(commit = False)
			count = Article.objects.count()
			count += 1
			article_url = "post-" + str(count)
			form.article_date = datetime.now()
			form.url = article_url
			if request.user.first_name:
				form.article_author = request.user.first_name
			else:
				form.article_author = request.user
			form.save()
			return redirect("article_detail", slug = article_url)
	else:
		return render(request, "articles/article_post.html")

def post_edit(request, slug):
	post = Article.objects.get(url = slug)
	if request.method == "POST":
		form = ArticleForm(request.POST, instance = post)
		if form.is_valid():
			post = form.save(commit = False)
			post.article_date = datetime.now()
			post.save()
			return redirect("article_detail", slug = slug)
	else:
		form = ArticleForm(instance = post)
	return render(request, "articles/article_update.html", {'form': form})

def post_delete(request, slug):
	post = Article.objects.get(url = slug)
	if request.method == "POST":
		form = ArticleForm(instance = post)
		post = form.save(commit = False)
		post.draft = True
		post.save()
		return redirect("/")
	return render(request, "articles/article_delete.html")

def about(request):
	return render(request, "articles/about.html")

def project(request):
	return render(request, "articles/project.html")

def login(request):
	return render(request, "articles/login.html")