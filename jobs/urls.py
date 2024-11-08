
from django.urls import path, include
from . import views
from .views import JobListView,JobDetailsView, JobCreateView


urlpatterns = [
    path('',JobListView.as_view(),name='job-list'),
    path('new/',JobCreateView,name='job-create'),
    path('<int:pk>/',JobDetailsView.as_view(),name='job-details'),
]
