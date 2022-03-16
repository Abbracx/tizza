from django.urls import path
from user.views import SignUpView

urlpatterns = [
    path('register', SignUpView.as_view(), name='signup')
]
