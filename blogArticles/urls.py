from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('blog/', views.blog, name='blog'),
    path('<slug:post_slug>/', views.blog_details, name='details'),
]