WEB Django con patrón MVT

URLs de pruebas:

- Main-desafio:

/desafio/

- Sección productos:

/desafio/usuarios/ 

en el mismo se encuentran botones que dirigen al registro(POST) y búsqueda(GET) de los mismos.

- **GET**:

/desafio/usuario/busqueda

En esta sección se encuntra un input dónde se escribe nombre y busca los usuarios registrados con el nombre, mostrando todas las coincidencias en la base de datos

- **POST**:

/desafio/publicaciones/

/desafio/productos/

/desafio/usuario/registro/

En estas tres secciones se encuentra un formulario con los datos que se necesitan para la creación de cada objeto. Una vez realizado el registro se realiza el POST impactando en la base de datos
