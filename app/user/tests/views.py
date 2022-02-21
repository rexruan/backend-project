"""
Test API working in our repository
"""
import json
from urllib import response

from django.test import Client
from django.test import TestCase

from ..models import User


class TestAPI(TestCase):
    
    @classmethod
    def setUpTestClient(cls):
        cls.client = Client()
        
    

    def test_connection(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode(encoding='utf-8'))
        self.assertEqual(content.get('success'), 1)
    
    def test_view_all_users(self):
        response = self.client.get('/api/view-all')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode(encoding='utf-8'))
        self.assertEqual(content.get('users'), [])
    

    def test_create_new_user(self):
        response = self.client.post(
            path='/api/create',
            data=json.dumps(
                {
                    'username': 'username',
                    'password': 'Passw0rd',
                    'email': 'example@gmail.com'
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(
            response.status_code,
            200
        )
        content = json.loads(response.content.decode(encoding='utf-8'))
        self.assertEqual(content.get('success'), 1)
        self.assertEqual(content.get('msg'), 'username has been successfully created')

    # def test_create_invalid_user(self):
    #     response = self.client.post(
    #         path='/api/create',
    #         data=json.dumps(
    #             {
    #                 'username': 'username',
    #                 'password': 'Password',
    #                 'email': 'example@gmail.com'
    #             }
    #         ),
    #         content_type='application/json'
    #     )
        # self.assertEqual(response.status_code, 200)
        # content = json.loads(response.content.decode(encoding='utf-8'))
        # self.assertEqual(content.get('success'), 0)
        # self.assertEqual(content.get('msg'), None)

    def test_update_user(self):
        User.objects.create(
            username='username',
            password='Passw0rd',
            email='example@gmail.com'
        )
        response = self.client.put(
            path='/api/update',
            data=json.dumps(
                {
                    'pk': 1,
                    'username': 'updated user',
                    'password': 'newPassw0rd',
                    'email': 'udpated_email@gmail.com',
                }
            ),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode(encoding='utf-8'))
        self.assertEqual(content.get('success'), 1)
        self.assertEqual(content.get('msg'), 'Updated successfully')
    
    def test_remove_user(self):
        User.objects.create(
            username='username',
            password='Passw0rd',
            email='exampl@gmail.com'
        )
        response = self.client.delete(
            path='/api/remove',
            data=json.dumps(
                {
                    'pk':1
                }
            )
        )
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode(encoding='utf-8'))
        self.assertEqual(content.get('success'), 1)
        self.assertEqual(content.get('msg'), 'Successfully deleted')
