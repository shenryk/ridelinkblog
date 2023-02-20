from django.urls import path
from .views import UserRegisterView , UserCreationForm 

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    # path('login/', UserLoginView.as_view(), name="login"),
    # path('profile/',views.profile,name="user-profile"),
]