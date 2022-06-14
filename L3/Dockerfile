FROM ubuntu

USER root
WORKDIR /root

COPY ENTRYPOINT.sh /

#instalar python
RUN apt-get update && apt-get install -y \
    dnsutils \
    ifupdown \
    iproute2 \
    iptables \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    python3.9 \
    git \
&& rm -rf /var/lib/apt/lists/* \
&& touch /etc/network/interfaces \
&& chmod +x /ENTRYPOINT.sh

#intalacion de POX
WORKDIR /home/tarea3
RUN git clone http://github.com/noxrepo/pox && apt-get remove git -y

#directorio de trabajo (ejecucion del programa)
WORKDIR /home/tarea3/pox/

#carpeta del codigo
RUN mkdir pox/tarea3

EXPOSE 6633 6653 6640

ENTRYPOINT ["/ENTRYPOINT.sh"]


