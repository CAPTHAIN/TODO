from django.conf.urls.static import static
from django.urls import path

from TODO import settings
from .views import *
from rest_framework import routers
from .api import TodoViewSet


router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')

urlpatterns = [
    path('', main, name='home'),
    path('add_page', AddTodo.as_view(), name='add_page'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', RegisterUser.as_view(), name='register'),
    path('logout', logout_user, name='logout'),
    path('update/<int:pk>/', TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
] + router.urls
