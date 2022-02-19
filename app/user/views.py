
import json

from django.core.exceptions import ValidationError
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
from .models import User
from .validators import validate_username, validate_password, validate_user_email

def user_page(request):
    return JsonResponse({'success': 1})

@require_http_methods(['POST'])
def create_user(request):
    """
    """
    new_user = json.loads(request.body)['newUser']
    username = new_user.get('username')
    password = new_user.get('password')
    email = new_user.get('email')
    try:
        validate_username(username)
        validate_password(password)
        validate_user_email(email)

    except ValidationError:
        return JsonResponse({
            'success': 0,
            'msg': ValidationError.messages 
        })
    except Exception as e:
        return JsonResponse({
            'success': 0,
            'msg': str(e)
        })

    User.objects.create(
        username = username,
        password = password,
        email = email 
    )
    return JsonResponse({
        'success': 1,
        'msg': f'{username} has been successfully created'
    })

    
def view_all_users(request):
    users = User.objects.all()
    serialized_users = serializers.serialize('json', users, fields=('username', 'email'))
    print('user', serialized_users)
    return JsonResponse({
        'users': eval(serialized_users)
    })


@require_http_methods(['PUT'])
def edit_user(request):
    try:
        user = json.loads(request.body)['updated_user']
        user_obj = User.objects.get(pk=user.get('pk'))
    except User.DoesNotExist as err:
        return JsonResponse({
            'success': 0,
            'msg': str(err)
        })
    
    username = user.get('username')
    password = user.get('password')
    email = user.get('email')

    try:
        validate_username(username)
        validate_password(password)
        validate_user_email(email)
    except ValidationError as err:
        return JsonResponse({
            'success': 0,
            'msg': str(err)
        })
    user_obj.username = username
    user_obj.password = password
    user_obj.email = email
    user_obj.save()
    
    return JsonResponse({
        'success': 1,
        'msg': 'Updated successfully'
    })


@require_http_methods(['DELETE'])
def remove_user(request):
    try:
        user = json.loads(request.body)['deleted_user']
        user_obj =  User.objects.get(pk=user.get('pk'))
        user_obj.delete()
    except Exception as err:
        return JsonResponse({
            'success': 0,
            'msg': str(err)
        })
