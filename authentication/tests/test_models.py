from django.test import TestCase

from authentication.models import User

class TestModels(TestCase):
    
    def test_create_user(self):
        user = User.objects.create_user(username='User', email='e@mail.com')
        user.set_password('123456')
        user.save()
        
        self.assertEqual(str(user), 'e@mail.com')
        
        