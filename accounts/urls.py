from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register , name='register'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('rabbit/', views.rabbit, name='rabbit'),

    path('profile/' , views.profile, name='profile'),

    path('trade_log', views.trade_log, name='trade_log'),

    path('second_trade', views.second_trade, name='second_trade'),

    path('user/', views.userPage, name='user-page'),

    path('delete_log/', views.delete_log, name='delete_log'),

    path('binance_alim/', views.binance_alim, name='binance_alim'),
    path('binance_satim/', views.binance_satim, name='binance_satim'),

    path('binance_alim2/', views.binance_alim2, name='binance_alim2'),
    path('binance_satim2/', views.binance_satim2, name='binance_satim2'),

    path('binance_alim3/', views.binance_alim3, name='binance_alim3'),
    path('binance_satim3/', views.binance_satim3, name='binance_satim3'),

    path('binance_alim4/', views.binance_alim4, name='binance_alim4'),
    path('binance_satim4/', views.binance_satim4, name='binance_satim4'),

    path('binance_alim5/', views.binance_alim5, name='binance_alim5'),
    path('binance_satim5/', views.binance_satim5, name='binance_satim5'),



    path('gelismis_alim/', views.gelismis_alim, name='gelismis_alim'),
    path('gelismis_satim/', views.gelismis_satim, name='gelismis_satim'),

    path('gelismis_alim2/', views.gelismis_alim2, name='gelismis_alim2'),
    path('gelismis_satim2/', views.gelismis_satim2, name='gelismis_satim2'),

    path('gelismis_alim3/', views.gelismis_alim3, name='gelismis_alim3'),
    path('gelismis_satim3/', views.gelismis_satim3, name='gelismis_satim3'),

]