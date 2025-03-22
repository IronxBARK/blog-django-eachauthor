from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogEntry
from django.urls import reverse_lazy
from .forms import EntryForm 
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoginRequired
from django.core.exceptions import PermissionDenied
# Create your views here.

class MainPage(LoginRequired, ListView):
    model = BlogEntry
    template_name = 'main.html'
    
    context_object_name = 'blogs'
    
    slug_field = 'slug'
    slug_url_kwargs = 'slug'
    
    # If we use basic login required mixin we have to give login_url variable
    
    def get_queryset(self):
        # Filter the queryset to include only entries authored by the logged-in user
        return BlogEntry.blog.filter(author=self.request.user).order_by('date')
    
class Detail(LoginRequired, DetailView):
    model = BlogEntry
    template_name = 'one.html'
    
    context_object_name = 'one'
    
    def get_queryset(self):
        # Filter the queryset to include only entries authored by the logged-in user
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    
    
class Create(LoginRequired, CreateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as author
        return super().form_valid(form)
    
    
class Update(LoginRequired, UpdateView):
    form_class = EntryForm
    template_name = 'create.html'
    
    success_url = reverse_lazy('main')
    
    def get_queryset(self):
        # Filter the queryset to include only entries authored by the logged-in user
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
    
    def form_valid(self, form):
        # Display a success message when the form is valid
        messages.success(self.request, "Blog entry updated successfully!")  
        # Call the parent class's form_valid method to save the form and redirect
        return super().form_valid(form)

class Delete(LoginRequired, DeleteView):
    model = BlogEntry
    template_name = 'one.html'

    success_url = reverse_lazy('main')

    def get_queryset(self):
        # Filter the queryset to include only entries authored by the logged-in user
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)
