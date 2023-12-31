from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}), label='Логин')
    password = forms.CharField(
        label=('Пароль'),
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class UserSignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(), label='Логин')
    email = forms.CharField(widget=forms.EmailInput(), label='Email')
    password1 = forms.CharField(
        label=('Пароль'),
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label=('Еще раз'),
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self):
        user = super(UserSignupForm, self).save(self.request)
        group = Group.objects.get(name='NEW_USERS')
        group.user_set.add(user)
        return user
