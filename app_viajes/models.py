from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField

class Destino(models.Model):
    ciudad = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.ciudad} ({self.pais})"

class Mochilero(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para las "Pages" o Blogs
class Posteo(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=100, null=True, blank=True) 
    texto_corto = models.CharField(max_length=250) 
    cuerpo = RichTextField(null=True, blank=True) 
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 
    fecha_publicacion = models.DateField(auto_now_add=True) 
    imagen = models.ImageField(upload_to='posteos', null=True, blank=True) 

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

# Modelo para cumplir con "Profile" y gestionar la imagen del usuario
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    biografia = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Avatar de {self.user.username}"

# MOdelo para cumplir con "Messages"
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emisor")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receptor")
    texto = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emisor} para {self.receptor}"