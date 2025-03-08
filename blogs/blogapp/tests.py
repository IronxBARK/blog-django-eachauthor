from django.test import TestCase
from .models import BlogEntry
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class MainTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='x',password='0077amar')
        self.entry = BlogEntry.blog.create(title='Hello', particular='i am learning django', author=self.user)
        
    
    def test_working(self):
        self.check = BlogEntry.blog.get(id=self.entry.id)
        self.assertEqual(self.check.title, 'Hello')
        
    def test_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_absolute_url(self):
        self.assertEqual(self.entry.get_absolute_url(), '/blog/hello')
        
    def test_create_view(self):
        response = self.client.post(reverse('create'),{
            'title' : 'this is title',
            'particular' : 'this is particular',
            'author' : self.user 
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'this is title')
        self.assertContains(response, 'this is particular')
        
    def test_update_view(self):
        response = self.client.post(reverse('update', args=['hello']), {
            'title' : 'this is updated title',
            'particular' : 'this is updated particular',
        })
        
        self.assertContains(response, 'this is updated title')
        self.assertContains(response, 'this is updated particular')
        
    def test_delete_view(self):
        response = self.client.post(reverse('delete', args=['hello']))