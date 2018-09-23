from django.shortcuts import render

def home_page(request):
    return render(request, 'cvapp/home_page.html', {})
