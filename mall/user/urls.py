from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^login/$", views.user_login, name="login"),
    url(r"^register/$", views.register, name="register"),
    url(r"^user_logout/$", views.user_logout, name="user_logout"),

]