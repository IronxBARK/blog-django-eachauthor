from django.db import models

# Create your models here.
class BlogEntry(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    particular = models.TextField()
    date = models.DateField(auto_now_add=True)
    
    blog = models.Manager()
    
    class Meta:
        verbose_name_plural = 'Blog Enteries'
        
    def __str__(self):
        return self.title