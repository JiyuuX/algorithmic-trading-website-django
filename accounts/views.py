

from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.template import loader
from binance.enums import *
from binance.client import Client
from .models import *

from .forms import CreateUserForm,CustomerForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required


from .decorator import unauthenticated_user , allowed_users , admin_only

from django.contrib.auth.models import Group
from .models import Alimlar,Satimlar
import datetime
import websocket, json
import time
from decimal import *


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(

                user=user,
            )

            messages.success(request, ' Başarıyla kayıt olundu' + '\n' + 'Hosgeldin, ' + username )
            return render(request,'accounts/login.html')

    context = {'form':form}
    return render(request,'accounts/register.html', context)


def home(request):
    return render(request,'accounts/home.html')



@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('rabbit')
        else:
            messages.info(request, 'KullanıcıAdı veya Şifre Yanlış')

    context = {}
    return render(request,'accounts/login.html',context)


def logoutuser(request):
    logout(request)
    return redirect('home')




@login_required(login_url='login')
@admin_only
def rabbit(request):
    return render(request,'accounts/rabbit.html')


@login_required(login_url='login')
@allowed_users(allowed_roles='customer')
def profile(request):

    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method=='POST':
        form = CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()


    context = {'form':form}
    return render(request, 'accounts/profile.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles='customer')
def userPage(request):
    context={}
    return render(request, 'accounts/user.html',context)


def second_trade(request):
    context={}
    return render(request, 'accounts/second_trade.html', context)


def trade_log(request):
    b=Alimlar.objects.all()
    a=Satimlar.objects.all()
    context={ 'b':b,
              'a':a}

    return render(request, 'accounts/trade_log.html', context)

def delete_log(request):
    Alimlar.objects.all().delete()
    Satimlar.objects.all().delete()
    HttpResponse(request, 'accounts/delete_log.html')
    return render(request, 'accounts/trade_log.html')

#BINANCE API;
#SOCKET = "wss://stream.binance.com:9443/ws/btcusdt@trade"

client = Client("","")

def binance_alim(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('alim_degiskeni')
    front_end_adet = data.get('adet')
    front_end_adet2=float(front_end_adet)
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)
    print(front_end_adet)
    print(type(front_end_adet2))

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=0.0004,
    )

    tarih =datetime.datetime.now()
    Alimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)


    return HttpResponse('/')


def binance_satim(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('satis_degiskeni')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )


    tarih = datetime.datetime.now()
    Satimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')


def binance_alim2(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('alim2')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih =datetime.datetime.now()
    Alimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')


def binance_satim2(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('satim2')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih = datetime.datetime.now()
    Satimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')






def binance_alim3(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('alim3')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih =datetime.datetime.now()
    Alimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')


def binance_satim3(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('satim3')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih = datetime.datetime.now()
    Satimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')






def binance_alim4(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('alim4')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih =datetime.datetime.now()
    Alimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')


def binance_satim4(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('satim4')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )

    tarih = datetime.datetime.now()
    Satimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')



def binance_alim5(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('alim5')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )


    tarih =datetime.datetime.now()
    Alimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')


def binance_satim5(request):
    data = json.loads(request.body)
    binance_anlik_data = data.get('anlik_binance_deger')
    front_end_alim_degeri = data.get('satim5')
    front_end_adet = data.get('adet')
    print(data)
    print(binance_anlik_data)
    print(front_end_alim_degeri)

    client.create_order(
        symbol='BTCUSDT',
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=front_end_adet, )


    tarih = datetime.datetime.now()
    Satimlar.objects.create(adet=front_end_adet, fiyat=front_end_alim_degeri, tarih=tarih)

    return HttpResponse('/')





#GELISMIS ALIM SATIM KISMI;
#1
def gelismis_alim(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )


    return HttpResponse('/')


def gelismis_satim(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )

    return HttpResponse('/')
#-------------------------------------------
#2

def gelismis_alim2(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )

    return HttpResponse('/')


def gelismis_satim2(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )

    return HttpResponse('/')
#-------------------------------------------
#3
def gelismis_alim3(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )


    return HttpResponse('/')


def gelismis_satim3(request):
    data = json.loads(request.body)
    adet = data.get('adet')
    print(data)

    client.create_order(
        symbol='BTCTRY',
        side=SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=adet, )

    return HttpResponse('/')
#-------------------------------------------



"""
77 72 69 74 74 65 6E 20 62 79 20 62 75 72 61 6B 20
0A 62 69 74 63 6F 69 6E 20 77 69 6C 6C 20 62 65 20
61 62 6F 76 65 20 24 31 30 30 4B 20 6F 6E 65 20 64
61 79 20 0A 6C 65 74 27 73 20 67 6F 20 74 6F 20 6D
6F 6F 6E 20 74 68 61 6E 6B 20 79 6F 75 20 73 61 74
6F 73 68 69 0A 48 4F 44 4C 0A 31 34 2E 30 35 2E 32
30 32 32
"""








