from jobs import views
from django.urls import path

app_name = "jobs"

urlpatterns = [
    path("job_form/", views.jobFormView, name="job_form"),
    path("update/<int:id>/", views.jobUpdateFormView, name="job_update_form"),
    path("delete/<int:pk>", views.DeleteJob.as_view(), name="delete"),
]
