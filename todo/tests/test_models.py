from todo.models import Todo
from authentication.models import User

from utils.setup_test import TestSetup

class TestModels(TestSetup):
    
    def test_create_todo(self):
        '''
        user = User.objects.create_user(username='User', email='e@mail.com')
        user.set_password('123456')
        user.save()
        '''
        
        user = self.create_test_user()
        todo = Todo(owner=user, title='Buy milk', description='Do it')
        todo.save()
        
        self.assertEqual(str(todo), 'Buy milk')
        
        