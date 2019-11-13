#!/bin/bash

# Crea el grupo de recursos llamado acopioM
az group create --name acopioM --location uksouth

#Crea una maquina en el grupo de recursos generado anteriormente con nombre maquinaHito4, genero las claves ssh aqui
#Extrae la ip del campo .publicIpAddress del fichero generado anteriormente
#Para extraer el parametro publicIpAddress del JSON se ha basado en el comentario de Brian Campbell del post https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools
ip=$(az vm create --resource-group acopioM --name maquinaHito4 --image UbuntuLTS --generate-ssh-keys | jq -r '.publicIpAddress')

#Abro los puertos ssh y http
az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name SSH_rule \
    --protocol tcp \
    --priority 320 \
    --destination-port-range 22 \
    --access allow >/dev/null

az network nsg rule create --resource-group acopioM --nsg-name maquinaHito4 --name HTTP_rule \
    --protocol tcp \
    --priority 300 \
    --destination-port-range 80 \
    --access allow >/dev/null

#Añado la clave publica
az vm user update --resource-group acopioM -n maquinaHito4 -u xenahort --ssh-key-value "$(< $HOME/.ssh/id_rsa.pub)"z

#Clono el proyecto
git clone https://github.com/xenahort/proyectoCloudComputing
cd proyectoCloudComputing/provision/ansible/

#Modifico el fichero hosts
echo "[ubuntuserver]\nxenahort ansible_ssh_port=22 ansible_ssh_host=$ip\n[ubuntuserver:vars]\nansible_ssh_user=xenahort\nansible_ssh_private_key_file=$HOME/.ssh/id_rsa" > hosts

#Finalmente hay que ejecutar el playbook
ansible-playbook playbook.yml