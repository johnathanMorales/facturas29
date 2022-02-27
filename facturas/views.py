"""Facturas views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from facturas.forms import BillForm

# Models
from facturas.models import factura
# Create your views here.
@login_required
def new_bill(request):
    """Nueva factura para anular"""
    if request.method == 'POST':
        Form = BillForm(request.POST, request.FILES)
        if Form.is_valid():
            Form.save()
            return redirect('list_bill')
    else:
        Form = BillForm()
    return render(
        request=request,
        template_name='facturas/bill.html',
        context={
            'form': Form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
@login_required
def list_bill(request):
    """List existing bills."""
    bills = factura.objects.all().order_by('-created')

    return render(request, 'facturas/listbills.html', {'bills': bills})
