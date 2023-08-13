from django.db import models
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('gas_leak', 'Gas Leak'),
        ('gas_supply', 'Gas Supply Issue'),
        ('maintenance', 'Maintenance Request'),
    ]
    
    status = models.CharField(max_length=20, default='pending')
    service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
    details = models.TextField()
    attachment = models.FileField(upload_to='service_attachments/', blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.service_type} - {self.status}"
