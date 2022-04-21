from django.urls import path 

from user.views import ListUser, RegisterUser

urlpatterns = [

    path("signUp/", RegisterUser.as_view()),
    path("register/", ListUser.as_view()),
    #path("account/", )
]