title: OpendDaylight con Docker en un RPI
date: 2016-07-13 08:13
modified: 2016-07-13 08:13
category: P#7@ Unix
tags: odl, rpi
slug: odl-rpi
authors: kmoragas
summary: El siguiente documento trata de un intento de instalar OpenDaylight como un SDN Controller sobre un Raspberry PI utilizando Docker, gracias a la distribución HypriotOS.

El siguiente documento trata de un intento de instalar OpenDaylight como un SDN Controller sobre un Raspberry PI utilizando Docker, gracias a la distribución HypriotOS.

## Creación de SWAP

Para este caso se recomienda tener 1 GB de Swap con la idea de tener varios servicios en el RPI. Para ello se puede crear un archivo de SWAP sobre el filesyste:

```
sudo dd if=/dev/zero of=/var/swap.bin bs=1024 count=1048576
mkswap /var/swap.bin
chown root:root /var/swap.bin
chmod 0600 /var/swap.bin
swapon  /var/swap.bin
```


## Imagen de OpenDaylight

1. Primero es necesario crear un repostirio en GitHub. En mi caso será en esta dirección `https://github.com/kmoragas/docker`. Este repo se utilizará luego para llamarlo desde Docker-Hub (solo que hay problemas dependiendo de la arquitectura). 

2. Clonamos el repo en HypriotOS con el usuario `pirate` 

```
$ git clone https://github.com/kmoragas/docker.git
```


3. Creamos un Dockerfile en `/home/pirate/docker/odl-rpi/Dockerfile` con la siguiente información (también es posible obtener una versión más actualizada en el repo de github):

```
#
# OpenDaylight Karaf Beryllium 0.4.2 Dockerfile
#

# Se obtiene la imagen base, para el caso de RPI 
# es necesario que esta imagen sea para ARM
FROM resin/rpi-raspbian:jessie

# Autor original
#MAINTAINER  Docker INS <docker@ins.hsr.ch>

# Autor
MAINTAINER  kmoragas 

# Actualiza la información de apt
# Instalar OpenJDK 7 in headless mode
# Instalar wget
# Descargar distribution-karaf-0.2.0-Helium.tar.gz
# Instalar (unzip) OpenDaylight
RUN apt-get update && \
    apt-get -y install openjdk-7-jre-headless \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "Download distribution-karaf-0.4.2-Beryllium.tar.gz and install" && \
    wget -q -O /opt/odl.tar.gz "https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.4.2-Beryllium-SR2/distribution-karaf-0.4.2-Beryllium-SR2.tar.gz" && \
    tar -C /opt -xzf /opt/odl.tar.gz && \
    rm /opt/odl.tar.gz

# Establecer la varaible de ambiente JAVA_HOME
# Además verificar que sea java para ARM

ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-armhf/


# Bajar el máximo de la memoria a 256MB
# De lo contrario no se puede instanciar java. 
# Pues por defecto Karaf pone el límite máximo en 512M
ENV JAVA_MAX_MEM 256M

# Puertos OpenDaylight
# 162 - SNMP4SDN
# 179 - BGP
# 1088 - JMX access
# 1790 - BGP/PCEP
# 1830 - Netconf
# 2400 - OSGi console
# 2550 - ODL Clustering
# 2551 - ODL Clustering
# 2552 - ODL Clustering
# 4189 - PCEP
# 4342 - Lisp Flow Mapping
# 5005 - JConsole
# 5666 - ODL Internal clustering RPC
# 6633 - OpenFlow
# 6640 - OVSDB
# 6653 - OpenFlow
# 7800 - ODL Clustering
# 8000 - Java debug access
# 8080 - OpenDaylight web portal
# 8101 - KarafSSH
# 8181 - MD-SAL RESTConf and DLUX
# 8383 - Netconf
# 12001 - ODL Clustering
EXPOSE 6633 8080 8101 8181


# Definir el Directorio de Trabajo
WORKDIR /opt/distribution-karaf-0.4.2-Beryllium-SR2/bin


# Define el comando por defecto
CMD ["./karaf","server"]

```


4. Creamos un repositorio en `https://hub.docker.com` llamado odl-rpi


5. Luego corremos el Dockerfile utilizando:

```
$ cd /home/pirate/docker/odl-rpi/
$ docker build -t kmoragas/odl-rpi .
```


6. Después de unos cuantos minutos (30 min dependiendo de la conexión a internet). Podemos verificar nuestra imagen local:

```
$ docker images
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
odl-rpi                         latest              3ff5c4eb99cd        14 hours ago        518.4 MB
```

7. Podemos poner a correr la imagen con:

```
$ docker run -it kmoragas/odl-rpi
```

8. Si queremos exponer otros puertos:

```
docker run -p 127.0.0.1:$HOSTPORT:$CONTAINERPORT --name CONTAINER -t someimage
```

## Configuración de OpenDaylight

Para mostrar todas las posible plugins para instalar se puede utilizar el siguiente comando:

```
feature:list
```

Para mostrar solo los componentes instalados:

```
feature:list -i
```

### DLUX

DLUX es la interfaz web para la administración de ODL.

1. Para instalar DLUX desde la terminal de karaf:

```
feature:install odl-dlux-core  odl-dlux-node  odl-dlux-yangui  odl-dlux
```

2. Luego es posible ingresar a: `http://<your-karaf-ip>:8181/index.html ` utilizando el usuario __admin__ y la contraseña __admin__

# Conclusiones

- Es posible instalar ODL sobre HypriotOS el inconveniente es que algunos componentes como DLUX no están compilados para ARM. Como se muestra abajo.

```
Error executing command: Can't install feature odl-dlux-core/0.0.0: 
Could not start bundle mvn:org.fusesource.leveldbjni/leveldbjni-all/1.8-odl in feature(s) odl-akka-leveldb-0.7: The bundle "org.fusesource.leveldbjni.leveldbjni-all_1.8.0 [295]" could not be resolved. Reason: No match found for native code: META-INF/native/windows32/leveldbjni.dll; processor=x86; osname=Win32, META-INF/native/windows64/leveldbjni.dll; processor=x86-64; osname=Win32, META-INF/native/osx/libleveldbjni.jnilib; processor=x86; osname=macosx, META-INF/native/osx/libleveldbjni.jnilib; processor=x86-64; osname=macosx, META-INF/native/linux32/libleveldbjni.so; processor=x86; osname=Linux, META-INF/native/linux64/libleveldbjni.so; processor=x86-64; osname=Linux, META-INF/native/sunos64/amd64/libleveldbjni.so; processor=x86-64; osname=SunOS, META-INF/native/sunos64/sparcv9/libleveldbjni.so; processor=sparcv9; osname=SunOS
```


- Además ODL es muy pesado para solo 1GB de RAM, y tiende a comportarse muy lento. 
