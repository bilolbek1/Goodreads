from django.urls import path
from .views import LoginView, RegisterView, ProfileView



urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile' )
]