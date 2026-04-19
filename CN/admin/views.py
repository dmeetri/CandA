from django.shortcuts import render

def dashboard(request):
    return render(request, 'admin/index.html')
