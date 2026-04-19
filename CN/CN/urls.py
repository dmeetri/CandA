from django.urls import path, include

urlpatterns = [
    path('CN/admin/', include('admin.urls')),
    path('system/', include('system.urls')),
]
