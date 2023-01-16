from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework.views import APIView

# Create your views here.

def home(request):
    return render(request,'authentication/home.html',context={

    })

class SignIn(APIView):
    def get(self,request):
        return render(request,'authentication/signin.html/')
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        # email = "tanvir@gmail.com"

        user = authenticate(email = email,password = password)
        if user is not None:
            login(request,user= user)
            return render(request,'authentication/home.html',context={
                'user':user
            })

        else:
            messages.error(request,"invalid")
            return redirect('home')


# def signin(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         # email = "tanvir@gmail.com"

#         user = authenticate(email = email,password = password)
#         if user is not None:
#             login(request,user= user)
#             return render(request,'authentication/home.html',context={
#                 'user':user
#             })

#         else:
#             messages.error(request,"invalid")
#             return redirect('home')
#     else:
#         return render(request,'authentication/signin.html/')

class SignUp(APIView):
    def post(self,request):
        username = request.POST['username']
        firstName = request.POST['firstname']
        lastName = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        rePass = request.POST['re_pass']
        
        if password != rePass:
            messages.error(request,"passwords didn't match")
            return render(request,'authentication/home.html')
        else:
            newUser = User.objects.create_user(username,email,password)
            newUser.first_name = firstName
            newUser.last_name = lastName
            newUser.save()
            messages.success(request,"created your account")
            return redirect('signin')

    def get(self,request):
        return render(request,'authentication/signup.html')




# def signup(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         firstName = request.POST['firstname']
#         lastName = request.POST['lastname']
#         email = request.POST['email']
#         password = request.POST['password']
#         rePass = request.POST['re_pass']
        


#         if password != rePass:
#             messages.error(request,"passwords didn't match")
#             return render(request,'authentication/home.html')
#         else:
#             newUser = User.objects.create_user(username,email,password)
#             newUser.first_name = firstName
#             newUser.last_name = lastName
#             newUser.save()
#             messages.success(request,"created your account")
#             return redirect('signin')

        
#     else:
#         return render(request,'authentication/signup.html')


        
    # return render(request,'authentication/signup.html')
def signout(request):
    logout(request)
    return render(request,'authentication/home.html')