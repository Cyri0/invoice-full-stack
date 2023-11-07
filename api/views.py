from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Invoice
from .serializers import InvoiceSerializer

@api_view(['GET'])
def getAllInvoices(request):
    invoices = Invoice.objects.all()
    ser = InvoiceSerializer(invoices, many = True)
    return Response(ser.data)