from django.views.generic import ListView
from .models import BlogEntry

# Create your views here.
class MainPage(ListView):
    model = BlogEntry
    template_name = 'home.html'
    
    context_object_name = 'blogs'