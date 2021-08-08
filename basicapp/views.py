from django.views.generic import FormView
from django.http import Http404, JsonResponse
from django.contrib.auth.views import LoginView as AuthLogin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.template.loader import render_to_string
from django.urls import reverse


class LoginView(AuthLogin):
    def get(self, request, *args, **kwargs):
        return Http404


class SignUpView(LoginView):
    form_class = UserCreationForm


class IndexView(FormView):
    template_name = 'basicapp/index.html'

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['login_form'] = AuthenticationForm()
        kwargs['signup_form'] = UserCreationForm()
        return kwargs


class ToDoView(FormView):
    form_class = ToDoForm

    def get(self, request, *args, **kwargs):
        kwargs = self.get_context_data()
        form = kwargs['form']
        return self.render_to_string(form)

    def render_to_string(self, form):
        return JsonResponse({'form': render_to_string('basicapp/form.html',
                                                      {'form': form,
                                                       'action': reverse('basicapp:to-do-view')},
                                                      request=self.request)
                             })

    def form_invalid(self, form):
        return self.render_to_string(form)

    def form_valid(self, form):
        return JsonResponse({'message': 'task created'})
