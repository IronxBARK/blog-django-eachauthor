from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogEntry
from django.urls import reverse_lazy
from .forms import EntryForm 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoginRequired
# Create your views here.

class MainPage(LoginRequired, ListView):
    model = BlogEntry
    template_name = 'main.html'
    
    context_object_name = 'blogs'
    
    slug_field = 'slug'
    slug_url_kwargs = 'slug'
    
    def get_queryset(self):
        return BlogEntry.blog.filter(author=self.request.user).order_by('date')
    
class Detail(DetailView):
    model = BlogEntry
    template_name = 'one.html'
    
    context_object_name = 'one'
    
class Create(CreateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as author
        return super().form_valid(form)
    
class Update(UpdateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    
    def get_queryset(self):
        return BlogEntry.blog.filter(slug=self.kwargs['slug'])
    
    def form_valid(self, form):
        messages.success(self.request, "Blog entry updated successfully!")  
        return super().form_valid(form)


class Delete(DeleteView):
    model = BlogEntry
    template_name = 'one.html'

    success_url = reverse_lazy('main')
