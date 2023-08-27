from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('hotels/<uuid:uid>/', views.hotels, name='hotels'),
    path('check_booking', views.check_booking),
    path('hoteldetail/<uuid:uid>/', views.hotel_detail, name='hoteldetail'),

    
    path('contact/', views.contact_view, name='contact'),
    path('payment/<uuid:uid>/', views.payment, name='payment'),
    # path('pay', views.pay, name='pay'),
    

]

