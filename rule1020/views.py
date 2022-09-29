
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Barangay, Emp, Municipality, User_office
from .forms import CreateEmployer
from django.contrib import messages
from django import forms
from django.db.models import Sum, Count, Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from xhtml2pdf import pisa


@login_required(login_url='user_login')
def dashboard(request):
   
    total_num_estabs = Emp.objects.count()
    labor_union = Emp.objects.all().aggregate(Count('labor_union'))['labor_union__count'] or 0.00
    subcontractors = Emp.objects.all().aggregate(Count('total_number_of_subcontactors'))['total_number_of_subcontactors__count'] or 0.00
    total_subcontractors = Emp.objects.all().aggregate(Sum('total_number_of_subcontracted_employees'))['total_number_of_subcontracted_employees__sum'] or 0.00
    total_num_workers= Emp.objects.all().aggregate(Sum('total_employment'))['total_employment__sum'] or 0.00
    male= Emp.objects.all().aggregate(Sum('male'))['male__sum'] or 0.00
    female= Emp.objects.all().aggregate(Sum('female'))['female__sum'] or 0.00
    regular= Emp.objects.all().aggregate(Sum('regular'))['regular__sum'] or 0.00
    non_regular= Emp.objects.all().aggregate(Sum('non_regular'))['non_regular__sum'] or 0.00
    alien = Emp.objects.all().aggregate(Sum('alien'))['alien__sum'] or 0.00
    abra= Emp.objects.filter(province='1').count()
    abra_count=int(abra)
    apayao= Emp.objects.filter(province='2').count()
    apayao_count=int(apayao)
    bbfo= Emp.objects.filter(province='3').count()
    bbfo_count=int(bbfo)
    ifugao= Emp.objects.filter(province='4').count()
    ifugao_count=int(ifugao)
    kalinga= Emp.objects.filter(province='5').count()
    kalinga_count=int(kalinga)
    mp= Emp.objects.filter(province='6').count()
    mp_count=int(mp)
    

    qs = Emp.objects.values('main_economic_activity').annotate(count=Count('main_economic_activity'))
   
    province_list=[
      abra_count,
      apayao_count,
      bbfo_count,
      ifugao_count,
      kalinga_count,
      mp_count
    ]


    context = { 
    
    'qs':qs,
  
    'total_num_estabs': total_num_estabs,
    'total_num_workers': total_num_workers,
    'male': male,
    'female': female,
    'regular': regular,
    'non_regular': non_regular,
    'alien':alien,
    'subcontractors':subcontractors,
    'total_subcontractors':total_subcontractors,
    'labor_union':labor_union,
    'apayao_count': apayao_count,
    'province_list':province_list,
    
    }
    return render(request, 'rule1020/dashboard.html', context)

@login_required(login_url='user_login')
def render_pdf_view(request,id):
    info_print = Emp.objects.get(id=id)

    template_path = 'rule1020/pdf1.html'
    context = {'info_print':info_print}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response,)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='user_login')
def data_list(request):
  
  d_list=Emp.objects.filter(province='3')
  
  context={'d_list': d_list}    
  return render(request, 'rule1020/add1020form.html', context)    

@login_required(login_url='/rule1020/user_login/') 
def addemployer(request):
  form = CreateEmployer()
 
  if request.method == 'POST':
        form = CreateEmployer(request.POST)
        if form.is_valid():
            form.save()
         
            return redirect('data_list')
        else:
            messages.error(request, 'An error occurred during registration')
  return render(request, 'rule1020/addemployer.html', {'form': form})

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('data_list')
    else:
      messages.error(request, 'Username OR password does not exist')  
  return render(request, 'rule1020/login_user.html')

@login_required(login_url='user_login')
def updates_emp(request,id):
  info_edit = Emp.objects.get(id=id)
  form = CreateEmployer(instance=info_edit)
  if request.method == 'POST':
        p_form = CreateEmployer(request.POST,
                                   request.FILES,
                                   instance=info_edit)
        if  p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('data_list')
        else:
             p_form -= CreateEmployer(instance=info_edit)

  context = {'form': form, 'info_edit': info_edit }        
  return render(request, 'rule1020/update_emp.html', context)


@login_required(login_url='user_login')
def deleteEmp(request, id):
    Info_del = Emp.objects.get(id=id)

    if request.method == 'POST':
        Info_del.delete()
        return redirect('data_list')
    return render(request, 'rule1020/deleteEmp.html', {'obj': Info_del})

def load_municipalities(request):
    province_id = request.GET.get('province')    
    municipalities = Municipality.objects.filter(province_id=province_id).order_by('name')
    context = {'municipalities': municipalities}
    return render(request, 'rule1020/municipality.html', context)

def load_barangay(request):
    municipality_id = request.GET.get('municipality')    
    barangay = Barangay.objects.filter(municipality_id=municipality_id).order_by('name')
    context = {'barangay': barangay}
    return render(request, 'rule1020/barangay.html', context)

def chart(request):
    return render(request, 'rule1020/chart.html',)

