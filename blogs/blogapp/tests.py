from django.test import TestCase
from .models import BlogEntry
from django.contrib.auth.models import User

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