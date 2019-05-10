from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField

User = get_user_model()


class SignupForm(UserCreationForm):
    username = forms.CharField(
        label="아이디",
        max_length=100,
        required=True
    )
    password1 = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
        help_text="8자리 이상",
    )
    password2 = forms.CharField(
        label="비밀번호 확인",
        widget=forms.PasswordInput,
        strip=False,
        help_text="이전에 입력한 비밀번호와 동일한 비밀번호를 입력",
    )

    error_messages = {
        'password_mismatch': "비밀번호 불일치",
    }

    class Meta:
        model = User
        fields = (
            'username',
            'password1',
            'password2',
        )


class SigninForm(AuthenticationForm):
    username = UsernameField(label="아이디", widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="비밀번호",
        strip=False,
        widget=forms.PasswordInput,
    )

    error_messages = {
        'invalid_login': "정확한  아이디와 비밀번호를 입력해주세요 "
    }
