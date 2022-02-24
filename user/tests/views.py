"""
Test API working in our repository
"""
import json

from django.test import Client
from django.test import TestCase

from ..models import User


class TestAPI(TestCase):
    
    @classmethod
    def setUpTestClient(cls):
        cls.client = Client()
        
    def api_test_helper(self, response, **kwargs):
        self.assertEqual(response.status_code, 200)    
        content = json.loads(response.content.decode(encoding='utf-8'))
        for kwarg in kwargs:
            self.assertEqual(content.get(kwarg), kwargs[kwarg])

    def generate_valid_user(self, pk=None):
        return json.dumps(
            {
                'pk': pk,
                'username': 'username',
                'password': 'Passw0rd',
                'email': 'example@gamil.com'
            }
        )
    
    def generate_invalid_user(self,pk=None):
        return json.dumps(
            {
                'pk': pk,
                'username': 'username',
                'password': 'password',
                'email': 'example@gmail.com'
            }
        )
    
    def create_user_object(self):

        user = User.objects.create(
            username='username',
            password='Passw0rd',
            email='example@gmail.com'
        )
        user.save()
        return user

    def test_connection(self):
        response = self.client.get('/api/')
        self.api_test_helper(response, **{'success': 1})
    
    def test_view_all_users(self):
        response = self.client.get('/api/view-all')
        self.api_test_helper(response, **{'success': 1, 'users': []})

    def test_create_new_user(self):
        response = self.client.post(
            path='/api/create',
            data=self.generate_valid_user(),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 1,
                'msg': 'username has been successfully created'
            }
        )

    def test_create_invalid_user_with_exception(self):
        response = self.client.post(
            path = '/api/create',
            data = json.dumps({}),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': "object of type 'NoneType' has no len()"
            }
        )

    def test_create_invalid_user_with_validator_error(self):
        response = self.client.post(
            path='/api/create',
            data=self.generate_invalid_user(),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': 'The length of password is between 8 and 32;'
                       'Password contains number, uppercase and lowercase.'
            }
        )
    


    def test_update_user(self):
        user = self.create_user_object()
        response = self.client.put(
            path='/api/update',
            data=self.generate_valid_user(pk=user.pk),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 1,
                'msg': 'Updated successfully'
            }
        )
    
    def test_update_with_non_existing_user(self):
        response = self.client.put(
            path='/api/update',
            data=json.dumps({'pk': 1}),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': 'User matching query does not exist.'
            }
        )

    def test_update_with_empty_input(self):
        response = self.client.put(
            path='/api/update',
            data=json.dumps([]),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': "'list' object has no attribute 'get'"
            }
        )

    def test_update_with_invalid_user(self):
        user = self.create_user_object()
        response = self.client.put(
            path='/api/update',
            data=self.generate_invalid_user(pk=user.pk),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': 'The length of password is between 8 and 32;'
                       'Password contains number, uppercase and lowercase.'
            }
        )

    def test_remove_user(self):
        user = self.create_user_object()
        response = self.client.delete(
            path='/api/remove',
            data=json.dumps({'pk': user.pk})
        )
        self.api_test_helper(
            response,
            **{
                'success': 1,
                'msg': 'Deleted successfully'
            }
        )

    def test_remove_non_existing_user(self):
        response = self.client.delete(
            path='/api/remove',
            data=json.dumps({'pk':1}),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': 'User matching query does not exist.'
            }
        )
    
    def test_remove_empty_input(self):
        response = self.client.delete(
            path='/api/remove',
            data=json.dumps([]),
            content_type='application/json'
        )
        self.api_test_helper(
            response,
            **{
                'success': 0,
                'msg': "'list' object has no attribute 'get'"
            }
        )
