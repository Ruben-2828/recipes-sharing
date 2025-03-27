from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("users_app:login")
    template_name = "users/registration.html"


class LogoutConfirm(LoginRequiredMixin, TemplateView):
    template_name = "users/logout_confirm.html"
