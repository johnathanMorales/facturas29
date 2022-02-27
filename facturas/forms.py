"""bills forms."""

# Django
from django import forms

# Models
from facturas.models import factura


class BillForm(forms.ModelForm):
    """bill model form."""

    class Meta:
        """Form settings."""

        model = factura
        fields = ('billNumber', 'reason', 'comment')
