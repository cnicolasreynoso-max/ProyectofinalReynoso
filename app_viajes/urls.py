from django.urls import path
from django.contrib.auth.views import LogoutView
from app_viajes.views import *

urlpatterns = [
    # --- Rutas Generales ---
    path('', inicio, name="Inicio"),
    path('about/', about, name="About"),

    # --- Rutas del Blog (Pages) ---

    path('pages/', PageList.as_view(), name="pages"),
    path('pages/<int:pk>/', PageDetail.as_view(), name="page_detail"), # <int:pk> permite ver un post específico por su ID
    path('pages/crear/', PageCreate.as_view(), name="page_create"),
    path('pages/editar/<int:pk>/', PageUpdate.as_view(), name="page_update"),
    path('pages/borrar/<int:pk>/', PageDelete.as_view(), name="page_delete"),
    path('login/', login_request, name="login"),
    path('signup/', register, name="signup"),
    path('logout/', LogoutView.as_view(next_page='Inicio'), name="logout"),
    path('accounts/profile/', editar_perfil, name="editar_perfil"),
    path('crear-destino/', crear_destino, name="CrearDestino"),
    path('crear-mochilero/', crear_mochilero, name="CrearMochilero"),
    path('buscar-destino/', buscar_destino, name="BuscarDestino"),
    path('mensajes/', MensajeList.as_view(), name="mensaje_list"),
    path('mensajes/crear/', MensajeCreate.as_view(), name="mensaje_create"),
    path('perfil/', ver_perfil, name="ver_perfil"),
]