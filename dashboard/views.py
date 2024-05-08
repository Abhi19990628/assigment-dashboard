from django.shortcuts import render
from django.http import JsonResponse
from .models import DataPoint

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def dashboard_data(request):
    data = DataPoint.objects.all().values()
    return JsonResponse(list(data), safe=False)
