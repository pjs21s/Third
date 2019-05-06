from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name ='accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', views.Register.as_view(), name="register"),
    path('profile/<username>/<int:pk>', views.Profile.as_view(), name="profile"),
    path("profile/<int:pk>/remove", views.DeleteUser.as_view(), name="remove"),
    path("profile/update_profile", views.update_profile, name="update_profile"),
]