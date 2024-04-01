from django.shortcuts import render,redirect
from .models import CarDetails,Registration

def home(request):
    return render(request,'home.html')

def main(request):
    return render(request,'main.html')

def detail(request,car_name):
    data = CarDetails.objects.get(car_name = car_name)
    
    return render(request,'see_details.html',{'data':data})


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        dateofbirth = request.POST['dateofbirth']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        obj = Registration()

        obj.Name = name
        obj.Gender = gender
        obj.Date_of_birth = dateofbirth
        obj.Phone = phone
        obj.Email = email
        obj.Password = password
        obj.save()
        return render(request,'home.html')
       
    return render (request,'register.html')

def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        datas = Registration.objects.get(Email = username)
        if (password == (datas.Password)):
            return render(request,'main.html',{'mydata':datas})
        else:
            return render(request,'home.html')
    else:
        return render(request,'home.html')
    
def passwordChange(request):
    if request.method == 'POST':
        userDatas = Registration.objects.all()
        user_email = request.POST.get('email')
        new_password = request.POST.get('newpassword')
        idList = []
        for data in userDatas:
            idList.append(data.Email)
        if user_email in idList:
            user_detail = Registration.objects.get(Email=user_email)
            user_detail.Password = new_password
            user_detail.save()
            successMessage = 'Password change successfully.'
            moveHomePage = 'Okey'
            return render(request,'password_change.html',{'message':successMessage,'moveHomePage':moveHomePage})
        else:
            wrong = 'Enter your correct mail id'
            return render(request,'password_change.html',{'message':wrong})
            
    else:
        return render(request, 'password_change.html')        


       

    




