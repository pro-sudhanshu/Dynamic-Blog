from django.shortcuts import render, get_object_or_404, redirect
from blogArticles.models import Post
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all().order_by('-post_published_date')
    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog.html', {'page_obj': page_obj})

def blog_details(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    related_posts = Post.objects.filter(post_category=post.post_category).exclude(id=post.id)[:3]
    return render(request, 'details.html', {'post':post, 'related_posts': related_posts})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(
            Q(post_title__icontains=query) |
            Q(post_content__icontains=query) |
            Q(post_category__icontains=query)
        )
    else:
        results = Post.objects.all().order_by('-post_published_date')  # Return all posts if no query is provided
    
    paginator = Paginator(results, 6)  # Show 6 posts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_results.html', {'query': query, 'page_obj': page_obj})
