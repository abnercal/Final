from django import forms
from .models import Compra, Producto, Usuario

class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ('usuario', 'producto', 'cantidad')



def __init__ (self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        self.fields["producto"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["producto"].help_text = "Ingrese las marcas"
        self.fields["producto"].queryset = Actor.objects.all()
