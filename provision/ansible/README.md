# Provisionamiento en Ansible

Para el provisionamiento se ha utilizado una máquina virtual **Ubuntu Server 18.04 LTS**. Se ha escogido dicha imagen debido a que no requerimos de elementos como interfaz gráfica ni navegadores, y sí que se requeriría de un soporte a largo plazo.

La aplicación ha sido desplegada en Azure en la dirección:

```
MV: 13.80.105.155
```

## Ejecución

Los pasos que se deben seguir para realizar el provisionamiento son:

Instalación de Python
```
sudo apt-get install python
```

Instalación de ansible
```
sudo apt-get install Ansible
```

Finalmente hay que ejecutar el playbook
```
ansible-playbook provision/ansible/playbook.yml
```

## Documentos

El primer documento definido es el `ansible.cfg` en el que definimos dónde se encuentra el fichero host así como indicar si queremos que se compruebe la clave del host.
```
[defaults]
host_key_checking = False
inventory = ./hosts
```

El siguiente documento, es el ya mencionado `hosts`. En este documento indicamos el nombre de la máquina, el puerto por el que se accederá mediante ssh y su dirección, así como la ubicación de la clave ssh privada.
```
[ubuntuserver]
xenahort ansible_ssh_port=22 ansible_ssh_host=13.80.142.56

[ubuntuserver:vars]
ansible_ssh_user=xenahort
ansible_ssh_private_key_file=~/ssh/key
```

El fichero `playbook.yml` que es el que ejecutamos para realizar el provisionamiento indicamos elementos como el hosts, el usuario de la máquina, si las tareas se realizarán como sudo y la ubicación de las tareas.
```
---
- hosts: xenahort
  user: xenahort
  become: yes
  roles:
  - common
```

Finalmente ha sido definido el fichero `/roles/common/tasks/main.yml` que indica las tareas de provisionamiento que se realizarán en la máquina remota.
```
---
- name: Actualizaciones
  apt: update_cache=yes

- name: Instalar git
  apt: name=git state=present

- name: Instalar Python python3
  apt: name=python3 state=present

- name: Installing pip3
  apt: name=python3-pip state=present

- name: Toca clonar el proyecto
  git:
    repo: https://github.com/xenahort/proyectoCloudComputing
    dest: "~/proyectoCloudComputing"

- name: Instalar fichero requirements
  shell: "pip3 install -r ~/proyectoCloudComputing/requirements.txt"

- name: Descarga de corpus punkt
  shell: "python3 -m nltk.downloader punkt"

- name: Descarga de corpus stopwords
  shell: "python3 -m nltk.downloader stopwords"

- name: Descarga de corpus maxent_treebank_pos_tagger
  shell: "python3 -m nltk.downloader maxent_treebank_pos_tagger"
```

## Comprobación del proyecto de [gomezportillo](https://github.com/gomezportillo)

Se ha comprobado el provisionamiento en una máquina virtual del proyecto [Apolo](https://github.com/gomezportillo/apolo). Para ello se han seguido los pasos indicados [aquí](https://github.com/gomezportillo/apolo/blob/master/provision/README.md) con la única modificación de los datos referentes a la máquina virtual como usuario y dirección ip.

![Provisionamiento](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/apolo1.png)
![Prueba](https://github.com/xenahort/proyectoCloudComputing/blob/master/img/apolo2.png)

## Proyecto comprobado por [fpeiro](https://github.com/fpeiro)

El provisionamiento del servicio ha sido probado por [@fpeiro](https://github.com/fpeiro) verificando que las tareas se realizan
correctamente. Se muestra una captura del resultado obtenido:

![Despliegue-fpeiro](https://github.com/fpeiro/proyectoCloudComputing/blob/master/img/fpeiro-deploy.png)
