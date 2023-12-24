from todo.models import Todo
from authentication.models import User
from django.urls import reverse

from utils.setup_test import TestSetup

class TestViews(TestSetup):
    
    def test_create_todo(self):        
        user = self.create_test_user()
        self.client.post(reverse('login'), {
            'username': user.username,
            'password': '123456'
        })
        
        todos = Todo.objects.all()
        self.assertEqual(todos.count(), 0)
        
        response = self.client.post(reverse('create-todo'), {
            'owner': user,
            'title': 'Todo #1',
            'description': 'Doing this'
        })
        
        updated_todos = Todo.objects.all()
        
        self.assertEqual(updated_todos.count(), 1)
        self.assertEqual(response.status_code, 302)

        
        