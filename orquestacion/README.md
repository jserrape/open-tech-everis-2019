# Orquestación

## Instalar Vagrant

Para [instalar](https://www.comoinstalarlinux.com/como-instalar-vagrant-en-ubuntu-16-04-y-linux-mint-18/) Vagrant, en primer lugar se deber descargar la versión .deb se su [página web](https://www.vagrantup.com/downloads.html). En este caso la versión más reciente es la versión 2.2.2. Una vez descargarda se instalará de la siguiente forma:

```
$ sudo dpkg -i vagrant_2.2.2_x86_64.deb
```

## Crear una aplicación de Azure Active Directory (AAD)

Para el desarrollo de la siguente parte del hito se ha basado en la información encontrada en el siguiente [repositorio](https://github.com/Azure/vagrant-azure) de GitHub de Azure.

En primer lugar hay que iniciar sesión de Azure con `az login`.

En segundo lugar ejecutaremos en comando `az account list --query "[?isDefault].id" -o ts` para obtener el parámetro `AZURE_SUBSCRIPTION_ID`.

Finalmente con el comando `az ad sp create-for-rbac` se obtendrán los parámetros `AZURE_TENANT_ID`, `AZURE_CLIENT_ID` y `AZURE_CLIENT_SECRET`.

*Los anteriores parámetros son almacenados como variables de entorno para evitar subirlas a GitHub.*

## Configuración de Vagrantfile

Los elementos del fichero Vagrantfile que han sido tenidos en cuenta son:
1. Location: eastus. Como se ha argumentado en hitos anteriores se ha escogido esta localización por temas de rapidez.
2. Imagen: 18.04-LTS. Nuevamente se ha escogido esta imagen por todas las ventajas que ofrece para un servidor una imagen LTS. Con el comendo `az vm image list --output table` se pueden obtener un lista de las distintas imagenes y el urn necesario.

Se ha realizado una instalación básica, en el siguiente [enlace](https://github.com/Azure/vagrant-azure) se pueden encontrar otros parámetros adicionales.

## Ejecución de Vagrant

Para ejecutar Vagrant deberemos instalar la `dummy.box` de Azure e instalar el plugin.

```
$ vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
$ vagrant plugin install vagrant-azure
```

Una vez instalado todo lo necesario y creado el fichero Vagrantfile se ejecuta Vagrant:
```
$ vagrant up --provider=azure
```

El proyecto se encuentra en la ip:

```
Despliegue Vagrant: 13.94.149.242
```

## Proyecto comprobado por [fpeiro](https://github.com/fpeiro)

El sistema de orquestación implementado por [@xenahort](https://github.com/xenahort) ha sido probado por [@fpeiro](https://github.com/fpeiro) verificando que los resultados obtenidos son los correctos. A continuación se muestra una prueba de su ejecución:

![Vagrant-fpeiro](https://github.com/fpeiro/proyectoCloudComputing/blob/master/img/vagrant-fpeiro.png)

## Comprobación de proyecto de [gomezportillo](https://github.com/gomezportillo)

Se ha comprobado el sistema de orquestación implementado por [@gomezportillo](https://github.com/gomezportillo) verificando que los resultados obtenidos son los correctos. A continuación se muestra una prueba de su ejecución:

![Vagrant-gomezportillo](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/vagrant-gomezportillo.png)
