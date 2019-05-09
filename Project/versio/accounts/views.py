from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, logout
from django.views.generic import CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserCreateForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from posts.models import Post
# Create your views here.
class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"

class Profile(DetailView):
    model = User
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/profile.html"

class DeleteUser(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/user_confirm_delete.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.pk)

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserCreateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
