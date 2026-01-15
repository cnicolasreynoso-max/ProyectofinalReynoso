# TUPRIMERAPAGINA_REYNOSO

Proyecto Web en Django con temática "Blog de Viajes".

## Funcionalidades

1. **Herencia de Plantillas**: Se utiliza un `base.html` con barra de navegación verde.
2. **Modelos**:
   - `Destino`: Para cargar ciudades y países.
   - `Mochilero`: Para registrar usuarios.
   - `Posteo`: Para crear entradas de blog.
3. **Formularios**: Se pueden insertar datos en las tres clases.
4. **Búsqueda**: Se puede buscar en la base de datos por nombre de "Ciudad".

## Orden de pruebas

1. Ir a "Nuevo Destino" y cargar un par de ciudades.
2. Ir a "Buscar Destino" y probar buscando una ciudad existente y una que no exista.
3. Probar los formularios de "Registrar Mochilero" y "Nuevo Post" para verificar que guardan sin error (redireccionan al home).