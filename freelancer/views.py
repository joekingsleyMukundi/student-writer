from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date


from client.models import Jobs
# Create your views here.
@login_required(login_url='login')
def availablejobs(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/available-jobs.html')

@login_required(login_url='login')
def completedjobs(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/completed-jobs.html')


@login_required(login_url='login')
def disputedjobs(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/disputed-jobs.html')


@login_required(login_url='login')
def myJobs(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/my-jobs.html')

@login_required(login_url='login')
def profile(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/profile.html')

@login_required(login_url='login')
def setting(request):
  if request.user.is_admin:
    return redirect('admindashboard')
  return render(request, 'freelancer/settings.html')

@login_required(login_url='login')
def jobdescription(request, id):
  if request.user.is_admin:
    return redirect('admindashboard')
  if id is None:
    message.error(request,"no job was found")
    return redirect('freelanceravailablejobs')
  job = Jobs.objects.get(id = id)
  # remaining_time = job.created_at - job.due_date;
  context={
    'job': job,
    # 'remtime': remaining_time,
  }
  return render(request, 'freelancer/job-description.html',context)