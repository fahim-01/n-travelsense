from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.index, name='index'),
   path("destinations/<int:myid>", views.destination, name="Destination"),
   path("contact/", views.contact, name="ContactUs"),
   path("booking/", views.booking, name="Booking"),
   path("about/", views.about, name="AboutUs"),
   path("search/", views.search, name="Search"),
   path("signup", views.handleSignup, name="handleSignup"),
   path("login", views.handleLogin, name="handleLogin"),
   path("logout", views.handleLogout, name="handleLogout"),
]


