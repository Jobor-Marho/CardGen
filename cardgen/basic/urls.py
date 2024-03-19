from django.urls import path
from . import views

app_name = 'basicapp'

urlpatterns = [
    path('', views.home, name='index'),
    path('auth/', views.verifyAuth, name='verifyauth'),
    path('build/', views.buidEpin, name='buildepin'),
    path('format/', views.formatCard, name='format'),
    path('print/<str:epin>', views.printCard, name='print'),
    path('login/', views.signIn, name='signin'),
    path('signup/', views.signUp, name='register'),
    path('logout/', views.signOut, name='signout'),
]