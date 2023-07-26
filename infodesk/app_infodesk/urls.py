from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post, login, register, profile

urlpatterns = [
    path("", index, name="main_page"),
    path("top-sellers/", top_sellers, name="top_sellers"),
    path("advertisement-post/", advertisement_post, name="advertisement-post"),
    path("advertisement/", advertisement, name="advertisement"),
    path("login/", login, name="login"),
    path("profile/", profile, name="profile"),
    path("register/", register, name="register"),
]