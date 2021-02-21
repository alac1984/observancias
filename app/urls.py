from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre/', views.AboutView.as_view(), name='about'),
    path('contato/', views.ContactView.as_view(), name='contact'),
    path('post/', views.PostView.as_view(), name='post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]