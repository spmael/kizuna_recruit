from django.urls import path

from apps.recruit.views import cv_create_view, cv_detail_view

app_name = "recruit"

urlpatterns = [
    path("", cv_create_view, name="cv_create"),
    path("cv/<int:cv_id>/", cv_detail_view, name="cv_detail"),
]
