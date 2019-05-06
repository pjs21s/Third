from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username','email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "아이디"
        self.fields["email"].label = "이메일 주소"
        self.fields["password1"].label = "비밀번호"
        self.fields["password2"].label = "비밀번호 확인"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("bio", "lang")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bio"].label = "자기소개"
        self.fields["lang"].label = "언어"