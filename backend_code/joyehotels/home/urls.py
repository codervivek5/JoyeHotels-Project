from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('hotels/', views.hotels, name='hotels'),
    # path('contact/', views.contact, name='contact'),
    

]
static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)