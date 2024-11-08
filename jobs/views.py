from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView
from django.contrib import messages
# Create your views here.
from .models import Jobs

class JobListView(ListView):
    model = Jobs
    template_name = 'jobs/job_dashboard.html'
    context_object_name = 'jobs'
    ordering = ['date_posted']
    paginate_by = 2

    def get_queryset(self):
        return Jobs.objects.order_by('-date_posted')

class JobDetailsView(DetailView):
    model = Jobs
    template_name = 'jobs/job_details.html'
    context_object_name = 'job'

def JobCreateView(request):
    if request.method == "POST":
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        deal_payment = int(request.POST.get('deal_payment'))
        working_day = int(request.POST.get('working_day'))
        working_hours = int(request.POST.get('working_hours'))
        experience_year = int(request.POST.get('experience_year'))
        is_available = bool(request.POST.get('is_available'))

        job_post = Jobs.objects.create(
            job_title=job_title,
            job_description=job_description,
            location=location,
            deal_payment=deal_payment,
            working_day=working_day,
            working_hours=working_hours,
            is_available=is_available,
            experience_year=experience_year,
            posted_by=request.user,
        )
        if job_post is not None:
            return redirect('job-list')
        else:
            messages.error(request, 'Something went wrong for The Post')
    return render(request, 'jobs/create_job.html')


