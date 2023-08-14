from django.shortcuts import render, redirect

def Index(request):
    return render(request, 'website/index.html')

def Contact(request):
    return render(request, 'website/contact.html')