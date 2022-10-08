from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def blog(request):
    # fetch the data from admin panel or database
    allBlogs = Blog.objects.all()
    context = {'allBlogs':allBlogs}
    return render(request, 'blog/blog.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first
    context = {'blog':blog}
    return render(request, 'blog/blogpost.html', context)
