from django.shortcuts import render
from django.views.generic import TemplateView


class LoginView():
    pass


class SignUpView():
    pass


class IndexView(TemplateView):
    template_name = 'basicapp/index.html'
