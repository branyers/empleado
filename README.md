# Employee Directory and API DRF
API para la creación de Empleados y Departamentos, así como de su visualización.

## Requisitos
Python 3.8 & 
PIP

## Instalación
Descarge o clone el repositorio, si decidió el método por descarga también deberá
descomprimir el proyecto.

Abre un consola que apunte al proyecto y realiza lo siguiente.
- Crear entorno virtual ***`python3 -m venv env`***

- Activar entorno virtual 
	* Unix y Mac ***`env\Scripts\activate.bat`***
	* Windows ***`env/bin/activate`***

- Instalar dependencias
	* ***`python -m pip install -r requirements.txt***
	
		
- Aplicar migraciones


    	python manage.py makemigrations
    	python manage.py migrate
    	python manage.py runserver

> Puedes detener el servidor con ctr + c

- crea un superusuario para las ultimas configuraciones
	En la consola con el servidor parado introduce el siguiente comando
> 	python manage.py createsuperuser
	e introduce tu username, email y password

- Pon en marcha el servidor y crea 2 grupos en el admin de Django:


        	python manage.py runserver
        	accede a admin ej. http://127.0.0.1:8000/admin/
        	Da click en add Group, como nombre al primer grupo es 'administrador'
        	guardalo y agrega otro que tenga como nombre 'usuario' y guardalo

 - Para ver la documetacin accede a 
`	http://127.0.0.1:8000/docs/
	o
	http://127.0.0.1:8000/redoc/`

### Gracias :D