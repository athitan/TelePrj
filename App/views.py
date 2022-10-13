# Create your views here.
import random

from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

#from django.contrib.auth.decorators import login_required
# Create your views here.
from App.forms import CreateUserForm

import datetime


# from django.shortcuts import get_object_or_404
# from .forms import blogForm,blogForm3,blogForm2,blogForm4
# from .models import Blog2,Blog3,Blog4,Blog5
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000/home1')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            request.session['name'] = username
            print(request.session['name'])
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # login(request)
                request.session['name'] = username
                return redirect('http://127.0.0.1:8000/home1')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout(request):
    request.session['name'] = None
    return redirect("http://localhost:4200/home1/")

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

def home1(request):
        return render(request, 'home1.html')
#def prepaid(request):
    #return render(request, 'prepaid.html')
from App.models import prepaid,recs,postpaids,postrecs,postpayment1,Feedback,payment1,Queries,prepayment
from App.forms import pForm,recf,postForm,postm,pm1,pm

def show(request):
    obj=prepaid.objects.all()
    return render(request,"show.html",{'obj':obj})
def new(request):
    context={}
    form=pForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"new.html",{'form':form})
def update(request,id):
    obj=get_object_or_404(prepaid,id=id)
    form=pForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"update.html",{'form':form})
def delete(request,id):
    obj=prepaid.objects.get(id=id)
    obj.delete()
    return redirect("/show")
def adlogin(request):
    if request.method == 'POST':
        aname = request.POST['aname']
        pwd = request.POST['pwd']
        if pwd == 'root123!':
            return redirect("/show")
        else:
            messages.info(request, 'password is incorrect')
    context = {}
    return render(request, 'accounts/adlogin.html', context)

def prepaidd(request):
    if (request.session['name'] != None):
        items = prepaid.objects.all()
        return render(request, "prepaid.html", {'items':items})
    else:
        return redirect("http://localhost:8000/login/")


def buy(request):
    if (request.session['name'] != None):
        obj=prepayment.objects.all
    return render(request, 'buy.html',{'obj':obj})
def buy1(request):
    if (request.session['name'] != None):
        return render(request, 'buy1.html')
def buy2(request):
    if (request.session['name'] != None):
        obj = prepayment.objects.all
        return render(request, 'buy2.html',{'obj':obj})
def buy3(request):
    if (request.session['name'] != None):
        obj=postpayment1.objects.all
        return render(request, 'buy3.html',{'obj':obj})
def buy4(request):
    if (request.session['name'] != None):
        obj = postpayment1.objects.all
        return render(request, 'buy2.html',{'obj':obj})
def credit(request):
    return render(request, 'credit.html')
def about(request):
    return render(request, 'about.html')
def credit4(request):
    return render(request, 'credit4.html')
def new4(request):
    context={}
    form=postm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit")
    return render(request,"new4.html",{'form':form})

# def new1(request):
#     context={}
#     form=pm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("/fun")
#     return render(request,"new1.html",{'form':form})

def new5(request):
    context={}
    form=postm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit4")
    return render(request,"new5.html",{'form':form})

def new2(request):
    context={}
    form=pm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit2")
    return render(request,"new2.html",{'form':form})

def new6(request):
    context={}
    form=postm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit6")
    return render(request,"new6.html",{'form':form})


def new3(request):
    context={}
    form=recf(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit")
    return render(request,"new3.html",{'form':form})

def postpaidd(request):
    if (request.session['name'] != None):
        items = postpaids.objects.all()
        return render(request, "postpaid.html", {'items':items})
    else:
        return redirect("http://localhost:8000/login/")

def show1(request):
    obj1=recs.objects.all()
    return render(request,"show1.html",{'obj1':obj1})

def show3(request):
    obj1=postrecs.objects.all()
    return render(request,"show3.html",{'obj1':obj1})

def mobilenumbergeneration(request):
    cname1=request.POST['cname']
    address1=request.POST['address']
    email1 = request.POST['email']
    mobile1=random.randrange(1000000000,1999999999)
    obj1=recs(cname=cname1,address=address1,email=email1,mobile=mobile1)
    obj1.save()
    return render(request,'buy2.html',{'mobile1':mobile1})

def postpaidmobilenumbergeneration(request):
    cname1=request.POST['cname']
    address1=request.POST['address']
    email1 = request.POST['email']
    Amount1 = request.POST['Amount']
    mobile1=random.randrange(1000000000,1999999999)
    date1 = datetime.datetime.now()
    obj1=postrecs(cname=cname1,address=address1,email=email1,Amount=Amount1,mobile=mobile1,date=date1)
    obj1.save()
    return render(request,'buy4.html',{'mobile1':mobile1})



def credit1(request):
    obj=recs.objects.all()
    return render(request,"credit1.html",{'obj':obj})

def credit6(request):
    obj=postrecs.objects.all()
    return render(request,"credit6.html",{'obj':obj})

def show2(request):
    obj1=postrecs.objects.all()
    return render(request,"show2.html",{'obj1':obj1})

def credit2(request):
    obj=postrecs.objects.all()
    return render(request,"credit2.html",{'obj':obj})

def credit3(request):
    return render(request, "credit3.html")

def credit5(request):
    return render(request, "credit5.html")

def success(request):
    return render(request, "success.html")

# def credit7(request):
#     return render(request, "credit7.html")

# def fun(request):
#     got = prepayment.objects.filter(cname=request.session['name'])
#     if(got.count()==1):
#         return render(request,"credit.html",{'o':got})
#     else:
#         return render(request, "credit3.html",{'o':got})

def fun1(request):
    obj1=postrecs.objects.all()
    obj=postpayment1.objects.all()
    userPhone = request.POST.get('mobile')
    got = postrecs.objects.filter(mobile= userPhone).count()
    if(got==1):
        return render(request,"credit4.html")
    else:
        return render(request, "credit5.html")

def RenderFeed1(request):
    return render(request, "feed.html")

def AddFeed(request):
    name = request.POST.get('name')
    feed = request.POST.get('feed')
    Feedback.objects.create(name=name,feed=feed)
    return redirect("/success")

def AddFeed1(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    query = request.POST.get('query')
    phone = request.POST.get('phone')
    Queries.objects.create(name=name,email=email,query=query,phone=phone)
    return HttpResponse("<h1>Queries Submitted Successfully</h1>")

def ShowFeed(request):
    data = Feedback.objects.all()
    return render(request,"shows.html",{"data":data})

# def ShowFeed(request):
#     data = Feedback.objects.all()
#     return render(request,"shows.html",{"data":data})

# def profilenew(request):
#     context={}
#     form=pm1(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("/check")
#     return render(request,"profilenew.html",{'form':form})




def myprofile(request):
    got = recs.objects.filter(cname=request.session['name'])
    p=prepayment.objects.filter(cname=request.session['name'])
    if (got.count() == 1):
        return render(request, "credit7.html", {'o': got,'p':p})
    else:
        got1 = postrecs.objects.filter(cname=request.session['name'])
        if (got1.count() == 1):
            return render(request, "credit9.html", {'o': got1})
        else:
            return render(request, "credit8.html")

# def profilenew1(request):
#     context={}
#     form=pm1(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect("/check1")
#     return render(request,"profilenew1.html",{'form':form})

def postpaidbillpayment(request):
    got = postrecs.objects.filter(cname=request.session['name'])
    if (got.count() == 1):
        return render(request, "credit10.html", {'o': got})
    else:
        return render(request, "credit12.html")

def RenderFeed(request):
    return render(request, "queries.html")


def new1(request,pp):
    context={}
    request.session['pname'] = pp
    form=pm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/credit")
    return render(request,"new1.html",{'form':form})

def fun(request):
    userPhone = request.POST.get('mobile')
    got = recs.objects.filter(mobile=userPhone).count()
    if(got==1):
        return render(request,"credit.html",{'o':got})
    else:
        return render(request, "credit3.html",{'o':got})



def Payment(request):
    cname1=request.POST['cname']
    pname1=request.POST['pname']
    Ano1=request.POST['Ano']
    edate1=request.POST['edate']
    cvv1=request.POST['cvv']
    mobile1=request.POST['mobile']
    date1 = datetime.datetime.now()
    obj1=prepayment(cname=cname1,pname=pname1,Ano=Ano1,edate=edate1,cvv=cvv1,mobile=mobile1,date=date1)
    obj1.save()
    uname = request.POST.get('cname')
    userPhone = request.POST.get('mobile')
    got = recs.objects.filter(mobile=userPhone).count()
    h = recs.objects.filter(cname=uname).count()
    if(got==1 and h==1):
        return render(request,"credit.html",{'o':got})
    else:
        return render(request, "credit3.html",{'o':got})

def Paid(request):
    cname1=request.POST['cname']
    Ano1 = request.POST['Ano']
    edate1 = request.POST['edate']
    cvv1 = request.POST['cvv']
    obj1=postpayment1(cname=cname1,Ano=Ano1,edate=edate1,cvv=cvv1)
    obj1.save()
    return render(request,'credit6.html')

def add5(request):
    cname1=request.POST['cname']
    Ano1=request.POST['Ano']
    edate1=request.POST['edate']
    cvv1=request.POST['cvv']
    obj1=postpayment1(cname=cname1,Ano=Ano1,edate=edate1,cvv=cvv1)
    obj1.save()
    return render(request,'credit6.html')

from django.shortcuts import render
from django.views.generic import TemplateView
from backend.chat import chat


class mainpage(TemplateView):
    Template_view = "index.html"

    def get(self, request):
        return render(request, self.Template_view)

    def post(self, request):
        if request.method == 'POST':
            user = request.POST.get('input', False)
            context = {"user": user, "bot": chat(request)}

        return render(request, self.Template_view, context)
