from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import info,issue
from django.contrib.auth.decorators import login_required
from django.contrib import messages




def registeration(request):
    if request.method=="GET":
        return render(request,"registration.html")
    else:

        fname=request.POST.get('name')
        email=request.POST.get('email1')
        mobile=request.POST.get('number')
        address=request.POST.get('address')
        password1=request.POST.get('password')
        info(
            Name=fname,
            Email=email,
            Mobile=mobile,
            Address=address,
            Password=password1
        ).save()
        My_user=User.objects.create_user(username=email,email=email,password=password1)
        My_user.first_name=fname
        My_user.last_name=mobile
        My_user.save()
        return render(request,"reg_success.html")


def index(request):
    return render(request,"index.html")




def login_view(request):
    
    if request.method == 'POST':
        username1 = request.POST['Email']
        password1 = request.POST['Password']

        user = authenticate( username=username1, password=password1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request, 'Issue.html')
        else:
            messages.error(request,"*incorrect name or password")
            return redirect('index')
        

def log_out(request):
    logout(request)
    return render(request,'index.html')



@login_required (login_url='index')
def submission(request,):
    if request.method=="GET":
        return render(request,'submission.html')
    elif request.method == "POST":
        issue(
            Name=request.POST['name'],
            Mobile=request.POST['number'],
            concern=request.POST['consern'],
            query=request.POST['query'],
            feedback=request.POST['feedback']
        ).save()
        return render(request,'submission.html')

'''

def login_view(request):
    rows=info.objects.all()
    for row in rows:
        print(f"Name: {row.Name}, Email: {row.Email}, Mobile: {row.Mobile}, Address: {row.Address}, Password: {row.Password}")
        print("Executing SQL queries:")
        for query in connection.queries:
            print(query['sql'])
    
    # Continue with the rest of your view logic...
    return render(request, 'reg_success.html')
'''

