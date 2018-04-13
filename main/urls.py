from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),  # задаем имя, чтобы в дальнейшем обращаться через него
]