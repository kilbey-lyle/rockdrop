from django.shortcuts import render

# Create your views here.

def index(request):
    '''A view to show welcome page'''
    return render(request, 'welcome/index.html')