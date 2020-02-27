from django.conf.urls import url
from . import views

urlpatterns = [
	 url('about/', views.about, name='about-blog'),
	 
     url('', views.home, name='blog-home'),

]