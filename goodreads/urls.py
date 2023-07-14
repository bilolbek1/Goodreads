from .view import BaseView
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BaseView, name='base'),
    path('users/', include('users.urls')),
    path('books/', include('book.urls')),
]
