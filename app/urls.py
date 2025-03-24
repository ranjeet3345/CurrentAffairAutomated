# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.


from django.urls import path
from . import  views as app_view
from .forms import loginForm
from django.contrib.auth import views as auth_view  # Ensure this does not create a recursive import

urlpatterns = [
    path("",app_view.home,name="home"),
    path("login/", auth_view.LoginView.as_view(template_name="login.html",authentication_form=loginForm), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path(
        "password_change/", auth_view.PasswordChangeView.as_view(template_name="password_change.html"), name="password_change"
    ),
    path(
        "password_change_done",
        auth_view.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
        name="password_change_done",
    ),









    

]

