from django.shortcuts import render
from clientbook_app.models import Pelanggan 
from clientbook_app.forms import PelangganBaru

# Create your views here.
def index(request):
    return render(request, 'clientbook_app/index.html')

def pelanggan(request):
    pelanggan_list = Pelanggan.objects.order_by('nama_depan')
    pelanggan_dict = {'pelanggan':pelanggan_list}
    return render(request, 'clientbook_app/pelanggan.html', context=pelanggan_dict)

def clientbook(request):
    form = PelangganBaru()

    if request.method == "POST":
        form =PelangganBaru(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return pelanggan(request)
        else:
            print("Error: Formulir invalid")

    return render (request, 'clientbook_app/clientbook.html', {'form':form} )