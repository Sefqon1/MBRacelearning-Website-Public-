from django.urls import path
from .views import (
    HomePageView,
    contactView,
    successView,
    ImpressumView,
    DatenschutzView,
    BlogPageView,
    BlogPostView,
)

urlpatterns = [
    path("blogpost/<int:pk>/", BlogPostView.as_view(), name="blogpost"),
    path("blog/", BlogPageView.as_view(), name="blog"),
    path("datenschutz/", DatenschutzView.as_view(), name="datenschutz"),
    path("impressum/", ImpressumView.as_view(), name="impressum"),
    path("contact/", contactView, name="contact"),
    path("success/", successView, name="success"),
    path("", HomePageView.as_view(), name="home"),
]
