from django.urls import path
from .import views
from .feeds import LatestEntriesFeed

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre/', views.AboutView.as_view(), name='about'),
    path('contato/', views.ContactView.as_view(), name='contact'),
    path('busca/', views.search_result, name='search'),
    path('feed/', LatestEntriesFeed(), name='feed'),
    path('podcasts/', views.PodcastView.as_view(), name='podcasts'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]