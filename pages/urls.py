from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    ServicesPageView,
    contactPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("contact/", contactPageView, name="contact"),
]
