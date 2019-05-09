from django.urls import path
from .views import Register, Profile, DeleteUser, update_profile
from django.contrib.auth import views as auth_views

app_name ='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', Register.as_view(), name="register"),
    path('profile/<username>/<int:pk>', Profile.as_view(), name="profile"),
    path("profile/<int:pk>/remove", DeleteUser.as_view(), name="remove"),
    path("profile/update_profile", update_profile, name="update_profile"),
]