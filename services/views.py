from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import IncidentReportForm
from .models import Article

class GuidanceCalendarPageView(LoginRequiredMixin, TemplateView):
    template_name = "guidance_calendar.html"

class DormitoryPageView(LoginRequiredMixin, TemplateView):
    template_name = "dormitory.html"


@login_required
def incidentReportPageView(request):
    if request.method == "GET":
        form = IncidentReportForm()
    else:
        form = IncidentReportForm(request.POST)
        if form.is_valid():
            subject = form.subject
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(subject, message, from_email, ["filbert.maano@gmail.com"])
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            return redirect("incident_report")
    return render(request, "incident_report.html", {"form": form})

class CollegeApplicationListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "college_application_article_list.html"

class CollegeApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = "college_application_article_detail.html"