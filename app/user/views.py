import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
from .models import User

def user_page(request):
    return JsonResponse({'success': 1})

@require_http_methods(['POST'])
def create_user(request):
    """
    """
    new_user = json.loads(request.body)['newUser']
    new_user_object = User.objects.create(
        username = new_user.get('username'),
        password = new_user.get('password'),
        email = new_user.get('email') 
    )
    


@require_http_methods(['GET'])
def view_all_users(request):
    users = User.objects.all()
    serialized_users = serializers.serialize('json', users)
    print('user', serialized_users)
    return JsonResponse(serialized_users)


@require_http_methods(['PUT'])
def edit_user(request):
    return

@require_http_methods(['DELETE'])
def remove_user(request):
    return

