# ✈️ Blog de Viajes - Proyecto Final Coderhouse

Este es un proyecto web desarrollado con Python y Django que permite a una comunidad de viajeros compartir experiencias, crear blogs y comunicarse entre ellos.

## 🚀 Funcionalidades

* **Gestión de Usuarios:** Registro, Login, Logout y Edición de Perfil (con Avatar).
* **Blogs (Pages):** Crear, Leer, Editar y Borrar posteos (CRUD).
* **Texto Enriquecido:** Los blogs soportan formato (negrita, cursiva, etc.) gracias a CKEditor.
* **Mensajería Privada:** Los usuarios pueden enviarse mensajes entre sí.
* **Seguridad:** Vistas protegidas (solo usuarios logueados pueden editar o comentar).

## 🛠️ Tecnologías Utilizadas

* Python 3.11+
* Django
* Bootstrap 5 (Estilos)
* Pillow (Manejo de imágenes)
* Django-CKEditor (Editor de texto)

## ⚙️ Instalación y Ejecución

Si deseas clonar y correr este proyecto localmente:

1.  **Clonar el repositorio:**
    ```bash
    gh repo clone cnicolasreynoso-max/ProyectofinalReynosogit@github.com:cnicolasreynoso-max/ProyectofinalReynoso.git
    ```

2.  **Crear y activar un entorno virtual:**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Realizar migraciones:**
    ```bash
    python manage.py migrate
    ```

5.  **Correr el servidor:**
    ```bash
    python manage.py runserver
    ```

## 👤 Autor

* **Nombre:** Christian Reynoso
* **Curso:** Python  - Coderhouse