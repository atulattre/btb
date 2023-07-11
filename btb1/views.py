from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import User1,Image,Rd
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'home.html')



def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def signuppage(request):
    if request.method=='POST':
        username=request.POST.get('username')
       
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
       
        
        if password!=confirm_password:
            return HttpResponse("password and confirm password are different")
        elif password==confirm_password:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            new_user=User1(username=username,email=email,)
            new_user.save()
            
            return redirect('loginpage')
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse('An exception occured!Try again')
        

    return render(request,'signup.html')

def prd(request):
    return render(request,'give_flat.html')

def give_flat(request):
    if request.method=='POST':
        
        username=request.user
        building_name=request.POST.get('building_name')
        room_number=request.POST.get('room_number')
        room_type=request.POST.get('room_type')
        space=request.POST.get('space')
        images=request.POST.getlist('images')
        
        comments=request.POST.get('comments')
        new_rd=Rd(username=username,building_name=building_name,room_number=room_number,room_type=room_type,space=space,comments=comments)
        
        new_rd.save()
        new_rd.images.set(images)
        return HttpResponse("Your details are posted")

def cp(request):      #cp=complete profile
    if request.method=='POST':
        username=request.user
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
       
        student_id=request.POST.get('student_id')
        phone=request.POST.get('phone')
        course=request.POST.get('course')
        branch=request.POST.get('branch')
        year=request.POST.get('year')
        if password!=confirm_password:
            return HttpResponse("password and confirm password are different")
        elif password==confirm_password:
            my_user=User.objects.create_user(username,email,password)
            my_user.save()
            new_user=User1(username=username,firstname=firstname,lastname=lastname,email=email,student_id=student_id,phone=phone,course=course,branch=branch,year=year)
            new_user.save()
            
            return redirect('loginpage')
    elif request.method=='GET':
        return render(request,'signup.html')
    else:
        return HttpResponse('An exception occured!Try again')
        

    return render(request,'signup.html')
        







