from django.test import TestCase
from django.contrib.auth.models import User
from .models import Link

# Create your tests here.

class LinkTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Alain', password='Alain321jonse')
        Link.objects.create(user=self.user, title='The 1st Lkin')
        
    def test_link_creation(self):
        qs = Link.objects.create(user = self.user, title = 'a test')
        self.assertEqual(qs.title, 'a test')
        
    def test_edit_link(self):
        qs = Link.objects.get(user = self.user)
        qs.title = 'The 1st link'
        qs.save()
        qs = Link.objects.get(user = self.user)
        self.assertEqual(qs.title, 'The 1st link')
    
    def test_delete_link(self):
        Link.objects.get(user = self.user).delete()
        qs = Link.objects.filter(user = self.user)
        self.assertEqual(qs.exists(), False)