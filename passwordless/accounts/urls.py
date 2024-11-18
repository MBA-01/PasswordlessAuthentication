
from django.urls import path
from .views import SignUpView

from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import RegistrationView, PasswordlessLoginView, PasswordfulLoginView

urlpatterns = [
    
    path("signup/", SignUpView.as_view(), name="signup"),
    path("registration2/", RegistrationView.as_view(), name="registration2"),
    path("passwordlesslogin/", PasswordlessLoginView.as_view(), name="passwordlesslogin"),
    path("passwordfullogin/", PasswordfulLoginView.as_view(), name="passwordfullogin"),
]
