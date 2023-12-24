from django.test import TestCase
from authentication.models import User
from faker import Faker

class TestSetup(TestCase):
    
    def setUp(self) -> None:
        #print('Test started')
        self.faker = Faker()
        self.password = self.faker.paragraph(nb_sentences=5)
        self.user = {
            'username': self.faker.name().split(" ")[0],
            'email': self.faker.email(),
            'password': self.password,
            'password2': self.password
        }
        
    def create_test_user(self):
        user = User.objects.create_user(username='User', email='e@mail.com')
        user.set_password('123456')
        user.is_email_verified = True
        user.save()
        return user
    
    def create_2nd_test_user(self):
        user = User.objects.create_user(username='User1', email='e1@mail.com')
        user.set_password('123456')
        user.is_email_verified = True
        user.save()
        return user
    
    def tearDown(self) -> None:
        #print('Test finished')
        return super().tearDown()