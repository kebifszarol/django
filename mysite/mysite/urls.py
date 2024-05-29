from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
