from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("profile_form/", views.profileFormView, name="profile_form"),
    path("job/<int:id>/", views.userJob, name="user_job"),
    path("account", views.accounFormView, name="account"),
    path("<slug:slug>/", views.userProfile, name="user_profile"),
]
