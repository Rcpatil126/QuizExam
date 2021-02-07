from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method== "POST":
        user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if User is not None:
           auth.login(request, user)
           return redirect(contact)
        else:
            return render(request,'home.html',{'error':" Invalid Details please Try again!!!"});
    else:
        return render( request,'home.html');



# def login(request):
#     if request.method == "POST":
#         user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#         if user is not None:
#             auth.login(request, user)
#             return redirect(contact)
#         else:
#             return render(request, 'home.html', {'error': " password not match  "})
#     else:
#         return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['passwordagin']:
         try:
           
                user = User.objects.get(username=request.POST['username'])
                return render (request, 'register.html',{'error':"name already taken"})
         except User.DoesNotExist:
                 user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                 return redirect(home)
        else:

          return render(request,'register.html',{'error':"wrong details"})
    else:
         return render(request,'register.html')
# def signup(request):
#     if request.method == "POST":
#         if request.POST['password'] == request.POST['passwordagain']:

#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'register.html', {'error': "username alredy taken "})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
#                 return redirect(home)

#         else:
#             return render(request, 'register.html', {'error': " password not match  "})
#     else:
#         return render(request, 'register.html')








def logout(request):
     auth.login(request)
     return redirect(home)


def contact(request):
        if request.method == "POST":
            return render(request, 'home2.html')
        else:
            return render(request , 'home1.html')

