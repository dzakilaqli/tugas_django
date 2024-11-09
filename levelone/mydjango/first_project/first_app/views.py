from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import VehicleType, Vehicle, OwnershipRecord

# Create your views here.
def index(request):
    ownership_list = OwnershipRecord.objects.order_by("purchase_date")
    context = {"ownership_records": ownership_list}
    return render(request, "first_app/index.html", context=context)