from django.shortcuts import render, HttpResponse,render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreatedonorForm, CreateseekerForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decoraters import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import User
from django.contrib import auth
from .models import donor, seeker, blooddonor, bloodseeker

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is home")

@unauthenticated_user
def registerdonor(request):
    form = CreatedonorForm()
    if(request.method == 'POST'):
        form = CreatedonorForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            group=Group.objects.get(name='donor')
            user.groups.add(group)
            # donor.objects.create(
            #     user=user
            # )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerdonor.html', context)
    # return HttpResponse("this is register")

@unauthenticated_user
def registerseeker(request):
    form = CreateseekerForm()
    if(request.method == 'POST'):
        form = CreateseekerForm(request.POST)
        if form.is_valid():
            user = form.save()
            # this is used for getting the username in views 
            username = form.cleaned_data.get('username')
            group=Group.objects.get(name='seeker')
            user.groups.add(group)
            # donor.objects.create(
            #     user=user
            # )

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    context = {'form':form}
    return render(request, 'registerseeker.html', context)
    # return HttpResponse("this is register")

@unauthenticated_user
def login_all(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/admindashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)
    # return HttpResponse("this is login page")

def logout_all(request):
    logout(request)
    return redirect('login')
    # return HttpResponse("this is logout") 

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("this is contact")

def gallery(request):
    return render(request, 'gallery.html')
    # return HttpResponse("this is gallery")

def news(request):
    return render(request, 'news.html')
    # return HttpResponse("this is news")

@login_required(login_url='login')
@admin_only
def admindashboard(request):
    dons=blooddonor.objects.all()
    seeks=bloodseeker.objects.all()
    d=donor.objects.all()
    s=seeker.objects.all()

    total_donors= dons.count()
    total_seekers= seeks.count()
    td= d.count()
    ts= s.count()
    context={'dons':dons, 'seeks':seeks,'td':td, 'ts':ts, 'total_donors':total_donors, 'total_seekers':total_seekers}
    return render(request, 'admindashboard.html', context)
    # return HttpResponse("this is admindashboard") 

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donordashboard(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        blood = request.POST['blood'] 
        desc = request.POST['message'] 

        details=blooddonor(name=name, email=email, phone=phone, blood=blood, desc=desc)

        details.save()
        # return render(request, 'donordashboard.html')
    # 
    dons=blooddonor.objects.all()
    seeks=bloodseeker.objects.all()
    d=donor.objects.all()
    s=seeker.objects.all()

    total_donors= dons.count()
    total_seekers= seeks.count()
    td= d.count()
    ts= s.count()
    
    context={'dons':dons, 'seeks':seeks,'td':td, 'ts':ts, 'total_donors':total_donors, 'total_seekers':total_seekers}
    return render(request, 'donordashboard.html', context)
    # return HttpResponse("this is donordashboard") 

@login_required(login_url='login')
@allowed_users(allowed_roles=['seeker'])
def seekerdashboard(request):
    if request.method == 'POST':
        name = request.POST['name'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        blood = request.POST['blood'] 
        desc = request.POST['message'] 

        details=bloodseeker(name=name, email=email, phone=phone, blood=blood, desc=desc)

        details.save()
        # return render(request, 'donordashboard.html')
    # 
    dons=blooddonor.objects.all()
    seeks=bloodseeker.objects.all()
    d=donor.objects.all()
    s=seeker.objects.all()

    total_donors= dons.count()
    total_seekers= seeks.count()
    td= d.count()
    ts= s.count()
    context={'dons':dons, 'seeks':seeks,'td':td, 'ts':ts, 'total_donors':total_donors, 'total_seekers':total_seekers}
    return render(request, 'seekerdashboard.html', context)
    # return HttpResponse("this is seekerdashboard") 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
@admin_only
def adminaction(request):
    return render(request, 'adminaction.html')
    # return HttpResponse("this is adminaction") 

@login_required(login_url='login')
@allowed_users(allowed_roles=['seeker'])
def seekerprofile(request):
    try:
        detail=seeker.objects.get(user=request.user)
        context={'detail':detail}
        return render(request, 'seekerprofile.html', context)
    except:
        return HttpResponse("You have to first update profile information.")

@login_required(login_url='login')
@allowed_users(allowed_roles=['donor'])
def donorprofile(request):
    try:
        detail=donor.objects.get(user=request.user)
        context={'detail':detail}
        return render(request, 'donorprofile.html', context)
    except:
        return HttpResponse("You have to first update profile information.")


# @allowed_users(allowed_roles=['donor'])
def donordetails(request):
    if request.method == 'POST':
        dname = request.POST['dname'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        address = request.POST['address'] 
        city = request.POST['city'] 
        desc = request.POST['message']
        usser=request.user
        # donor.objects.create(
        #     user=usser
        # )

        details=donor(user=usser, dname=dname, email=email, phone=phone, address=address, city=city, desc=desc)

        details.save()
       
        return redirect('donordashboard')
    return render(request, 'donordetails.html')
    # return HttpResponse("this is donordetails") 


# @allowed_users(allowed_roles=['seeker'])
def seekerdetails(request):
    if request.method == 'POST':
        dname = request.POST['dname'] 
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        address = request.POST['address'] 
        city = request.POST['city'] 
        desc = request.POST['message']
        usser=request.user        

        details=seeker(user=usser, dname=dname, email=email, phone=phone, address=address, city=city, desc=desc)

        details.save()
        return redirect('seekerdashboard')

    return render(request, 'seekerdetails.html')
    # return HttpResponse("this is seekerdetails") 


