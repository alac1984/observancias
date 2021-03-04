from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sobre/', views.AboutView.as_view(), name='about'),
    path('contato/', views.ContactView.as_view(), name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]