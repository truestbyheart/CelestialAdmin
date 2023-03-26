from django.contrib.auth.forms import AuthenticationForm


class CustomAdminLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customize the form fields if needed
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control form-control-lg'})
        self.fields['password'].widget.attrs.update({'placeholder': 'password', 'class': 'form-control form-control-lg'})
