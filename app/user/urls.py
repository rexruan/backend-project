from django.urls import path

from .views import view_all_users, create_user, edit_user, remove_user, user_page

app_name = 'user'

urlpatterns = [
    path('', user_page),
    path('view-all', view_all_users),
    path('create', create_user),
    path('edit', edit_user),
    path('remove', remove_user),
]