from django.contrib import admin
from django.contrib.auth.views import LoginView
from core.forms import CustomAdminLoginForm


class CustomAdminLoginView(LoginView):
    form_class = CustomAdminLoginForm
    template_name = 'admin/login.html'


admin.site.login = CustomAdminLoginView.as_view()
