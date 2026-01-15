from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from app_viajes.models import Posteo, Avatar, Destino, Mochilero, Mensaje 
from app_viajes.forms import PosteoForm, UserEditForm, DestinoForm, MochileroForm, MensajeForm, AvatarForm


# --- VISTAS GENERALES ---
def inicio(request):
    imagen_url = None
    if request.user.is_authenticated:
        try:
            imagen_url = request.user.avatar.imagen.url
        except:
            pass
    return render(request, "app_viajes/index.html", {"imagen_url": imagen_url})

def about(request):
    return render(request, "app_viajes/about.html")

# --- VISTAS DEL BLOG (PAGES) Usando Class Based Views ---
class PageList(ListView):
    model = Posteo
    template_name = "app_viajes/pages.html"
    context_object_name = "paginas"

class PageDetail(DetailView):
    model = Posteo
    template_name = "app_viajes/page_detail.html"

class PageCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    form_class = PosteoForm
    template_name = "app_viajes/page_form.html"
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PageUpdate(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = PosteoForm
    template_name = "app_viajes/page_form.html"
    success_url = reverse_lazy('pages')

class PageDelete(LoginRequiredMixin, DeleteView):
    model = Posteo
    template_name = "app_viajes/page_confirm_delete.html"
    success_url = reverse_lazy('pages')

# --- VISTAS DE AUTENTICACIÓN ---
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return redirect('Inicio')
            else:
                return render(request, "app_viajes/login.html", {"mensaje": "Datos incorrectos"})
    form = AuthenticationForm()
    return render(request, "app_viajes/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "app_viajes/index.html", {"mensaje": f"Usuario {username} creado"})
    form = UserCreationForm()
    return render(request, "app_viajes/registro.html", {"form": form})

@login_required
def editar_perfil(request):
    usuario = request.user
    # Busca el avatar del usuario, o crea uno vacío si no existe
    avatar, created = Avatar.objects.get_or_create(user=usuario)

    if request.method == 'POST':
        # Formulario de datos básicos (nombre, email)
        miFormulario = UserEditForm(request.POST, instance=usuario)
        # Formulario de datos extra (avatar, bio, link)
        avatarForm = AvatarForm(request.POST, request.FILES, instance=avatar)

        if miFormulario.is_valid() and avatarForm.is_valid():
            miFormulario.save()
            avatarForm.save()
            return render(request, "app_viajes/index.html", {"mensaje": "Perfil actualizado correctamente"})
    else:
        miFormulario = UserEditForm(instance=usuario)
        avatarForm = AvatarForm(instance=avatar)

    return render(request, "app_viajes/editar_perfil.html", {
        "form": miFormulario, 
        "avatar_form": avatarForm, 
        "avatar": avatar
    })

@login_required
def ver_perfil(request):
    # Buscar el avatar del usuario logueado
    avatar, created = Avatar.objects.get_or_create(user=request.user)
    return render(request, "app_viajes/perfil.html", {"avatar": avatar})

# --- VISTAS 2da PREENTREGA---

def crear_destino(request):
    if request.method == "POST":
        mi_formulario = DestinoForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            destino = Destino(ciudad=info["ciudad"], pais=info["pais"], descripcion=info["descripcion"])
            destino.save()
            return render(request, "app_viajes/index.html")
    else:
        mi_formulario = DestinoForm()
    return render(request, "app_viajes/form_destino.html", {"mi_formulario": mi_formulario})

def crear_mochilero(request):
    if request.method == "POST":
        mi_formulario = MochileroForm(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            mochilero = Mochilero(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            mochilero.save()
            return render(request, "app_viajes/index.html")
    else:
        mi_formulario = MochileroForm()
    return render(request, "app_viajes/form_mochilero.html", {"mi_formulario": mi_formulario})

def buscar_destino(request):
    if request.GET.get("ciudad"):
        ciudad_buscada = request.GET["ciudad"]
        destinos = Destino.objects.filter(ciudad__icontains=ciudad_buscada)
        return render(request, "app_viajes/resultado_busqueda.html", {"destinos": destinos, "ciudad": ciudad_buscada})
    else:
        return render(request, "app_viajes/buscar_destino.html")
    

    # --- VISTAS DE MENSAJERÍA ---

# Crear/Enviar Mensaje
class MensajeCreate(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = "app_viajes/mensaje_form.html"
    success_url = reverse_lazy('mensaje_list')

    def form_valid(self, form):
        # Asignamos automáticamente el 'emisor' como el usuario que está logueado
        form.instance.emisor = self.request.user
        return super().form_valid(form)

# Listar Mensajes Recibidos
class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = "app_viajes/mensaje_list.html"
    context_object_name = "mensajes"

    def get_queryset(self):
        # Filtramos para mostrar SOLO los mensajes donde 'receptor' soy yo
        return Mensaje.objects.filter(receptor=self.request.user).order_by('-fecha_envio')