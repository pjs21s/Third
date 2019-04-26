from . import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, logout
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
class Register(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/register.html"

class Profile(generic.DetailView):
    model = User
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/profile.html"

class DeleteUser(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("accounts:login")
    template_name = "accounts/user_confirm_delete.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.pk)

class ModifyUser(generic.UpdateView):
    model = User
    fields =['email']
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, '성공적으로 변경되었습니다.')
            return redirect('accounts:login')
        else:
            messages.error(request, '문제가 있습니다.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })