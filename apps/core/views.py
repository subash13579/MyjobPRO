from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage

from apps.job.models import Job
from apps.userprofile.models import Userprofile

import requests
import json


def frontpage(request):
    jobs = Job.objects.all()
    p = Paginator(jobs, 7)
    page_no = request.GET.get('page',1)
    try:
        page = p.page(page_no)
    except EmptyPage:
        page = p.page(1)
    # task_url = "https://v13.teamproit.com/api/resource/Task?fields=[%22name%22,%22subject%22,%22status%22,%22category%22,%22gulf_experience%22,%22working_days%22,%22transportation%22,%22accommodation%22,%22contract_period__month%22,%22vac%22,%22qualification_type%22,%22service%22,%22territory%22,%22description%22,%22customer%22,%22project%22,%22currency%22,%22amount%22,%22amount%22,%22job_category%22,%22creation%22,%22minimum_experience%22,%22maximum_experience%22,%22qualification%22,%22specialization%22,%22salary_type%22,%22from%22,%22to%22,%22contract_period_year%22,%22joining_ticket%22,%22food%22,%22leave%22,%22visa_type%22,%22nationality%22,%22over_time%22,%22any_other_allowance%22]&&filters=[[%22status%22,%22!=%22,%22Completed%22],[%22status%22,%22!=%22,%22Cancelled%22],[%22status%22,%22!=%22,%22Hold%22],[%22service%22,%22in%22,[%22REC-D%22,%22REC-I%22]]]&&limit_page_length=5000"
    # response = requests.request("GET", task_url)
    # byte_str = response.content
    # dict_str = byte_str.decode("UTF-8")
    # job_response = json.loads(dict_str)
    # for j in job_response["data"]:
    #     a = Job(title =j["subject"],task_id = j["name"],territory = j["territory"], customer = j["customer"], status = j["status"], vacancies = j["vac"], qualification_type = j["qualification_type"], specialization = j["specialization"], category = j["category"], min_exp = j["minimum_experience"], max_exp = j["maximum_experience"], gulf_exp = j["gulf_experience"], salary_type = j["salary_type"], from_amount = j["from"], to_amount = j["to"], amount = j["amount"], description = j["description"], working_hours = j["working_days"], transportation = j["transportation"], contract_period_yr = j["contract_period_year"],contract_period_mn = j["contract_period__month"], joining_ticket = j["joining_ticket"], food = j["food"], accommodation = j["accommodation"], leave = j["leave"], visa_type = j["visa_type"], nationality = j["nationality"], overtime = j["over_time"], any_other_allowance = j["any_other_allowance"],created_by = request.user)
    #     a.save()
    return render(request, 'core/frontpage.html',{'jobs': page})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'jobseeker')
            username = request.POST.get('username')

            if account_type == 'employer':
                userprofile = Userprofile.objects.create(user=user,username=username,is_employer=True)
                user.userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user,username=username)
                user.userprofile.save()

            login(request,user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html',{'form':form})

def search_result_view(request):
    """
        User can search job with multiple fields
    """

    job_list = Job.objects.all()

    # Keywords
    if 'job_title_or_company_name' in request.GET:
        job_title_or_company_name = request.GET['job_title_or_company_name']

        if job_title_or_company_name:
            job_list = job_list.filter(title__icontains=job_title_or_company_name) | job_list.filter(
                customer__icontains=job_title_or_company_name)

    # location
    if 'territory' in request.GET:
        territory = request.GET['territory']
        if territory:
            job_list = job_list.filter(territory__icontains=territory)

    context = {

        'page_obj': job_list,

    }
    # return render(request, 'job/result.html', context)
    return render(request, 'core/frontpage.html',{'jobs': job_list})
