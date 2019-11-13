# ¿Qué es Docker?

Docker es una plataforma para desarrolladores y administradores de sistemas para desarrollar, implementar y ejecutar aplicaciones con contenedores. El uso de contenedores de Linux para implementar aplicaciones se denomina contenedorización. Los contenedores no son nuevos, pero su uso para implementar aplicaciones fácilmente sí lo es. [Fuente](https://docs.docker.com/get-started/)

La contenedorización es cada vez más popular porque los contenedores son:

+ Flexible: Incluso las aplicaciones más complejas se pueden transportar en contenedores.
+ Ligero: los contenedores aprovechan y comparten el núcleo del host.
+ Intercambiable: puede implementar actualizaciones y actualizaciones sobre la marcha.
+ Portátil: puede compilar localmente, implementarlo en la nube y ejecutar en cualquier lugar.
+ Escalable: puede aumentar y distribuir automáticamente réplicas de contenedores.
+ Apilable: puede apilar servicios verticalmente y sobre la marcha.

***

# Instalar Docker

Antes de instalar Docker CE por primera vez en una nueva máquina host, debe configurar el repositorio de Docker. Después, puede instalar y actualizar Docker desde el repositorio. [Fuente](https://docs.docker.com/install/linux/docker-ce/ubuntu/)

1. Actualizar el índice del paquete ```apt```:
```
$ sudo apt-get update
```

2. Instalar paquetes para permitir que ```apt``` use un repositorio sobre HTTPS::
```
$ sudo apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

3. Agregar la llave GPG oficial de Docker:
```
$ sudo apt-key fingerprint 0EBFCD88
```

4. Configurar el repositorio estable:
```
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

5. Actualizar el índice del paquete apt e instalar la última versión de Docker CE:
```
$ sudo apt-get update
$ sudo apt-get install docker-ce
```

Para comprobar que se ha instalado correctamente se ejecutará la imagen ```hello-world```:
![img](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/pruebaDocker.png)


## Desplegar contenedor de Hub Docker

1. Iniciar servicio docker
```
sudo service docker start
```

2. Descargar y ejecutar docker
```
sudo docker run xenahort/proyectocc bash
```

La imagen del docker no se encontrará localmente, así que se descargará de forma automática.

![img](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/dockerhub.png)


## Desplegar contenedor en Azure

A través de la consola de Azure se ejecuta el siguiente comando:
```
az webapp create --resource-group cloud-shell-storage-westeurope && \
--plan plan-CC && \
--name proyectocloudcomputing && \
--deployment-container-image-name xenahort/proyectocc
```

Los parámetros empleados son:
- Grupo de recursos: cloud-shell-storage-westeurope
- Plan:  plan-CC
- Nombre: proyectocloudcomputing
- Nombre de la imagen del contenedor: xenahort/proyectocc

~~Por conflictos con la suscripción de Azure se realizará el despliegue en Heroku.~~

En caso de error en Azure porque la suscripción esté deshabilitada se puede cambiar con el comando:

```
az account set --subscription "nombre de la suscripcion"
```

Tras el cambio de suscripción se ha desplegado la aplicación en la siguiente dirección:

```
Contenedor: http://proyectocloudcomputing.azurewebsites.net
```
```
DockerHub: https://hub.docker.com/r/xenahort/proyectocc
```

## Desplegar contenedor en Heroku

Para el despliegue en Heroku se ha creado el fichero ```heroku.yml``` a partir de la información encontrada en la [web de Heroku](https://devcenter.heroku.com/categories/deploying-with-docker).

```
build:
  docker:
    release:
       dockerfile: Dockerfile
       target: builder
    web: Dockerfile
    worker: worker/Dockerfile
```

En el fichero ```heroku.yml``` se especifica que solo se usa la salida de la etapa ```build``` como la imagen de lanzamiento.

- build: Especifica el ```Dockerfile``` para construir.

Para desplegar el Docker se deberá colocar la pila de la aplicación en contenedor y subirla a Heroku.

```
$ heroku stack:set container
$ git push heroku master
```

![img](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/heroku-docker1.png)
![img](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/heroku-docker2.png)

## Fichero Dockerfile

El fichero Dockerfile está compuesto de las siguientes [instrucciones](https://docs.docker.com/engine/reference/builder/):

- La instrucción ```FROM``` especifica la imagen base a partir de la cual se está construyendo. Se ha seleccionado Alpine Linux ya que es mucho más pequeño que la mayoría de las imágenes de la base de distribución (~ 5MB), y por lo tanto conduce a imágenes mucho más delgadas en general. [Fuente](https://hub.docker.com/_/python/)

```
FROM python:3.6-alpine
```

- La instrucción ```MAINTAINER``` establece el campo ```Autor``` de la imagen generada.

```
MAINTAINER Juan Carlos Serrano Pérez <juan.carlos.wow.95@gmail.com>
```

- La instrucción ```WORKDIR``` establece el directorio de trabajo para las instrucciones ```RUN```, ```CMD```, ```ENTRYPOINT```, ```COPY``` y ```ADD``` que lo siguen en el ```Dockerfile```.

```
WORKDIR /app/docker
```

- La instrucción ```COPY``` copia los archivos o directorios nuevos desde ```<src>``` y los agrega al sistema de archivos del contenedor en la ruta ```<dest>```.

```
COPY . .
```

- La instrucción ```RUN``` ejecutará cualquier comando en una nueva capa encima de la imagen actual y confirmará los resultados. La imagen confirmada resultante se utilizará para el siguiente paso en el ```Dockerfile```.

```
RUN pip install -r requirements.txt && \
    python -m nltk.downloader punkt && \
    python -m nltk.downloader stopwords && \
    python -m nltk.downloader maxent_treebank_pos_tagger
```

- La instrucción ```EXPOSE``` informa a Docker que el contenedor escucha en los puertos de red especificados en el tiempo de ejecución.

```
EXPOSE 80
```

- La instrucción ```CMD``` su objetivo es proporcionar valores predeterminados para un contenedor en ejecución, como puede ser un ejecutable.

```
CMD ["python", "app.py"]
```
