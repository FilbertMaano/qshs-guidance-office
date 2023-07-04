from django.urls import path
from .views import GuidanceCalendarPageView, incidentReportPageView, DormitoryPageView, CollegeApplicationListView, CollegeApplicationDetailView

urlpatterns = [
    path("guidance_calendar/", GuidanceCalendarPageView.as_view(), name="guidance_calendar"),
    path("incident_report/", incidentReportPageView, name="incident_report"),
    path("dormitory/", DormitoryPageView.as_view(), name="dormitory"),
    path("college_application/", CollegeApplicationListView.as_view(), name="college_application_article_list"),
    path("college_application/<int:pk>/", CollegeApplicationDetailView.as_view(), name="college_application_article_detail"),
]
