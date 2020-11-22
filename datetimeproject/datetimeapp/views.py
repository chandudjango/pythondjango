from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    hr=int(date.strftime("%H"))
    s1='<h1>Hello guest'
    if hr<12:
        s1=s1+'good morning'
    elif hr<16:
        s1=s1+'good afternoon'
    elif hr<18:
        s1=s1+'good evening'
    elif hr<24:
        s1=s1+'midnight'
    s1=s1+'</h1><hr>'
    s1=s1+'<h1>The current date and time of server:'+str(date)+' </h1>'
    return HttpResponse(s1)
