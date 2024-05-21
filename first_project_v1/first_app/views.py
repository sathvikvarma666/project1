from django.shortcuts import render
from django.http import  HttpResponse
from first_app.forms import UserForm,UserProfileInfoForm
from first_app.models import UserProfileInfo


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls  import reverse
from django.contrib.auth.decorators import login_required



def index(request):
   my_dict = {"insert_me" : "Hey I'm Expermineting Relative urls in this project!"}
   return render(request,"first_app/index.html",context=my_dict)

def base(request):
   my_dict = {"find_me" : "I'm being edited from first_app/views.py!"}
   return render(request,"first_app/base.html",context=my_dict)

def other(request):
   my_dict = {"other_me" : "I'm being edited from first_app/views.py!" , "other_2" : "rcb rocks"}
   return render(request,"first_app/other.html",context=my_dict)

def relative(request):
   my_dict = {"relative_me" : "I'm being edited from first_app/views.py!"}
   return render(request,"first_app/relative_url.html",context=my_dict)

def register(request):
   # sourcery skip: extract-method, inline-immediately-returned-variable
   registered = False 
   
   if request.method == "POST" :
      user_form = UserForm(data=request.POST)
      profile_form = UserProfileInfoForm(data=request.POST)

      if user_form.is_valid() and profile_form.is_valid():
         user = user_form.save()
         user.set_password(user.password)
         user.save()
         profile = profile_form.save(commit = False)
         profile.user =user

         if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

         profile.save()

         registered = True
      else:
         print(user_form.errors,profile_form.errors)
   else:
      user_form = UserForm()
      profile_form = UserProfileInfoForm()

   return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})



         
def user_login(request):
   # sourcery skip: last-if-guard, remove-unnecessary-else, swap-if-else-branches, use-fstring-for-formatting, use-named-expression

   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')
   
      user = authenticate(username=username,password=password)

      if user:
         if user.is_active:
            login(request,user)
            print("usr : {}".format(user.is_authenticated))
            return HttpResponseRedirect(reverse('index'))
         else:
            return HttpResponse("Acount Not Active ")
      else:
         print("Someone Tried to login and failes")
         print("3 username : {} and password : {}".format(username,password) )
         return HttpResponse("Acount Does Not Exist")
   else:
      return render(request, 'first_app/login.html')

@login_required
def user_log_out(request):
   logout(request)
   return HttpResponseRedirect(reverse('index'))

      

            





      






