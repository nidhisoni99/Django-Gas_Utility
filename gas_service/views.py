from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'gas_service/base.html')
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return redirect('gas_service/submit_request.html')
            return redirect('gas_service:submit_request')  # Use the namespaced URL name here
    else:
        form = ServiceRequestForm()
    return render(request, 'gas_service/submit_request.html', {'form': form})

def track_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'gas_service/track_requests.html', {'requests': requests})


def service_request_detail(request, pk):
    request_obj = get_object_or_404(ServiceRequest, pk=pk)

    if request.method == 'POST':
        if 'mark_resolved' in request.POST:
            request_obj.resolved = True
            request_obj.save()
            return redirect('gas_service:track_requests')

    return render(request, 'gas_service/service_request_detail.html', {'request_obj': request_obj})


def service_request_detail(request, request_id):
    try:
        request_obj = ServiceRequest.objects.get(id=request_id, user=request.user)
    except ServiceRequest.DoesNotExist:
        # Handle case where request doesn't exist or doesn't belong to the user
        return HttpResponse("Service request not found")