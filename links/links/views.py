from django.shortcuts import render

def welcome(request):
    return render(request,'welcome.html')

def logout(request):
    return  render(request,'logout.html')