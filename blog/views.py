from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    context = {
        'blogs': Blog.objects.order_by('-id')[:4],
    }
    return render(request, 'blog/index.html', context)