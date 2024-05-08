from django.urls import path
from .views import dashboard, dashboard_data

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard_data/', dashboard_data, name='dashboard_data'),
]
# urls.py

