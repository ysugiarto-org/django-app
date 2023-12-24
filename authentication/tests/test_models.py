from authentication.models import User
from utils.setup_test import TestSetup

class TestModels(TestSetup):
    
    def test_create_user(self):
        '''
        user = User.objects.create_user(username='User', email='e@mail.com')
        user.set_password('123456')
        user.save()
        '''
        user = self.create_test_user()
        self.assertEqual(str(user), 'e@mail.com')
        
        