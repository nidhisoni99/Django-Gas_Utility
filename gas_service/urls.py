from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = 'gas_service'

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_service_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('service/<int:pk>/', views.service_request_detail, name='service_request_detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)