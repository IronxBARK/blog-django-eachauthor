from django.views.generic import ListView, DetailView
from .models import BlogEntry

# Create your views here.
class MainPage(ListView):
    model = BlogEntry
    template_name = 'home.html'
    
    context_object_name = 'blogs'
    
    slug_field = 'slug'
    slug_url_kwargs = 'slug'
    
class Detail(DetailView):
    model = BlogEntry
    template_name = 'one.html'
    
    context_object_name = 'one'