from django import forms
from clientbook_app.models import Pelanggan

class PelangganBaru(forms.ModelForm):
    class Meta():
        model = Pelanggan
        fields = '__all__'