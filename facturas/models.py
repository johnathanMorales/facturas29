#Django
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class factura (models.Model):
    """Create anulation factura request"""
    billNumber = models.CharField(max_length=10, unique=True)
    reason = models.CharField(max_length=50, blank=False)
    comment = models.CharField(max_length=250, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    
    def __str__(self):
        """Return billnumber."""
        return 'Factura: {} ID: {}'.format(self.billNumber, self.id)
    