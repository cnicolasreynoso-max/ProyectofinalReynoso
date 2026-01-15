from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_viajes.models import Posteo, Destino, Mochilero, Avatar, Mensaje

class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = '__all__'

class MochileroForm(forms.ModelForm):
    class Meta:
        model = Mochilero
        fields = '__all__'

# Formulario para crear Posts (Pages)
class PosteoForm(forms.ModelForm):
    class Meta:
        model = Posteo
        # Excluimos autor y fecha porque los ponemos automáticamente en la vista
        fields = ['titulo', 'subtitulo', 'texto_corto', 'cuerpo', 'imagen']

# Formulario personalizado para editar perfil (incluyendo Avatar)
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email'] # <--- ¡Solo estos 3!
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo Electrónico',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

# Formulario para mensajeria
class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['receptor', 'texto']
        labels = {
            'receptor': 'Destinatario',
            'texto': 'Escribe tu mensaje'
        }
        widgets = {
            'texto': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receptor': forms.Select(attrs={'class': 'form-select'}),
        }

#Formulario para editar biografia
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen', 'biografia', 'link', 'fecha_nacimiento']
        labels = {
            'imagen': 'Foto de Perfil',
            'biografia': 'Sobre mí',
            'link': 'Sitio Web / Red Social',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widgets = {
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }