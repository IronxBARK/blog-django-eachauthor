from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogEntry
from django.urls import reverse_lazy
from .forms import EntryForm 
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404


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
    
class Create(CreateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
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
