from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Knowledge_base
from .models import Faq

# Create your views here.

def home(request):
    return render(request, 'blog/base.html')

def knowledge_base(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/knowledge_base.html',{'posts':posts})

def faq(request):
    faq=Faq.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/faq.html',{'faq':faq})
