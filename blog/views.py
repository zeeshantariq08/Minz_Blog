# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
posts= [

	{
		'author':"Zeeshan Tariq",
		"title":"Blog Post 1",
		"content":"First Post Content",
		"date":"August 20,2020",

	}

]




def about(request):
	return render(request,'blog/about.html')




def home(request):
	context = {
		'posts':posts
	}
	return render(request,'blog/home.html',context)



