from django.urls import path 

from user.views import UserSignUpView, UserLoginView

urlpatterns = [
    path("signUp/", UserSignUpView.as_view()),
    path("register/", UserLoginView.as_view()),
]