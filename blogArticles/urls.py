from django.urls import path
from blogArticles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('blog/', views.blog, name='blog'),
    path('<slug:post_slug>/', views.blog_details, name='details'),
] 

# urlpatterns += static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)