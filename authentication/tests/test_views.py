from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages


class TestViews(TestCase):
    
    def test_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")
        
    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")
        
    def test_signup_user(self):
        self.user = {
            'username':'username',
            'email':'e@mail.com',
            'password':'123456',
            'password2':'123456'
        }
        
        response = self.client.post(reverse('register'), self.user)
        self.assertEqual(response.status_code, 302)
        
    def test_signup_user_failed_username_taken(self):
        self.user = {
            'username':'username',
            'email':'e@mail.com',
            'password':'123456',
            'password2':'123456'
        }
        
        self.client.post(reverse('register'), self.user)
        response = self.client.post(reverse('register'), self.user)
        self.assertEqual(response.status_code, 409)
        
        storage = get_messages(response.wsgi_request)
        
        msgs = []
        for msg in storage:
            #print(msg)
            msgs.append(msg.message)
        
        self.assertIn("Username is taken, choose another one", msgs)
        
    def test_signup_user_failed_email_taken(self):
        self.user = {
            'username':'username',
            'email':'e@mail.com',
            'password':'123456',
            'password2':'123456'
        }
        
        self.user1 = {
            'username':'username1',
            'email':'e@mail.com',
            'password':'123456',
            'password2':'123456'
        }
        
        self.client.post(reverse('register'), self.user)
        response = self.client.post(reverse('register'), self.user1)
        self.assertEqual(response.status_code, 509)
        
        storage = get_messages(response.wsgi_request)
        
        self.assertIn("Email is already used, choose another one", 
                      list(map(lambda x: x.message, storage)))