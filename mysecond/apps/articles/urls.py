from django.urls import path

from . import views

urlpatterns = [
	path('', views.article_list, name = 'article_list'),
	path('add/', views.article_post, name = 'article_post'),
	path('all/', views.ArticleAll.as_view(), name = 'article_all'),
	path('about/', views.about, name = 'about'),
	path('project/', views.project, name = 'project'),
	path('login/', views.login, name = 'login'),
	path('<slug:slug>/', views.article_detail, name = 'article_detail'),
	path('review/<int:pk>/', views.leave_comment, name = 'leave_comment'),
	path('<slug:slug>/edit/', views.post_edit, name = 'post_edit'),
	path('<slug:slug>/delete/', views.post_delete, name = 'post_delete')
]