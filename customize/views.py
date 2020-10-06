from django.shortcuts import render,HttpResponse,redirect
from .models import Destination,Contact,Booking
from math import ceil
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

def index(request):
    allProds = []
    catprods = Destination.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Destination.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'index.html', params)
def searchMatch(query, item):
    '''return true onlyif query matches the item'''
    if query in item.desc.lower() or query in item.Destination_name.lower() or query in item.category.lower():
        return True
    else:    
        return False    
    
def search(request):
    query = request.GET.get('search')
    print(query )
    allProds = []
    catprods = Destination.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Destination.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

    params = {'allProds':allProds, "msg":""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg':"Please make sure  to enter relevant query"}
    return render(request, 'search.html', params)
    

def destination(request, myid):

    # Fetch the product using the id
    destination = Destination.objects.filter(id=myid)
    return render(request, 'destinations.html', {'destination':destination[0]})


def contact(request):
    thank =False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact.html', {'thank': thank})

def booking(request):
    thank =False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        departure = request.POST.get('departure', '')
        destination = request.POST.get('destination', '')
        number_of_guests = request.POST.get('number_of_guests', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        booking = Booking(name=name, email=email, departure=departure, destination=destination, number_of_guests= number_of_guests,  phone=phone, desc=desc)
        booking.save()
        thank = True
    return render(request, 'booking.html', {'thank': thank})


def about(request):
    return render(request, 'about.html')


def handleSignup(request):
    thank = False
    if request.method=='POST':
       fname = request.POST['fname']
       lname = request.POST['lname']
       username = request.POST['username']
       email = request.POST['email']
       pass1 = request.POST['pass1']
       pass2 = request.POST['pass2']
      #check Error
       if len(username) > 10:
            messages.error(request, 'Username must be under 10 characters')
            return redirect('index')
       if pass1 != pass2:
            messages.error(request, 'Password not match')
            return redirect('index')

     #create a user
       myuser = User.objects.create_user(username, email, pass1)
       myuser.first_name = fname
       myuser.last_name = lname
       myuser.save()
       messages.success(request, 'Your Account has been Successfully Created')
       return redirect('index')
    else:
        return HttpResponse('404 - Not Found')

def handleLogin(request):
    if request.method=='POST':
       loginusername = request.POST['loginusername']
       loginpassword = request.POST['loginpassword']
       user = authenticate(username=loginusername, password=loginpassword)
       if user is not None:
           login(request, user)
           messages.success(request, 'Successfully Logged In')
           return redirect('index')
       else:
           messages.error(request, 'Invalid Credentials, Please Try Again')
           return redirect('index')

    return HttpResponse('404 - Not Found')
def handleLogout(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('index')