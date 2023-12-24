from django.test import TestCase

from todo.models import Todo
from authentication.models import User

class TestModels(TestCase):
    
    def test_create_todo(self):
        user = User.objects.create_user(username='User', email='e@mail.com')
        user.set_password('123456')
        user.save()
        
        todo = Todo(owner=user, title='Buy milk', description='Do it')
        todo.save()
        
        self.assertEqual(str(todo), 'Buy milk')
        
        