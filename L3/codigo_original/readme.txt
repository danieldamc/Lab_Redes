#comandos desde linux (ubuntu 22.04)

deben tener instalado previamente docker, el tutorial de la documentacion oficial deja todo ok, recomiendo que sigan los pasos 1 y 2
de la postinstalacion para que no tengan que usar sudo a cada rato, pero es opcional

#este comando crea la imagen con todo lo necesario para la tarea
docker build -t tarea3 .

#para ver la imagen de docker
docker images

#ejecuta y crea el contenedor, ejecutenlo en la carpeta raiz de su tarea
docker run -it --rm --privileged -e DISPLAY \
             --name tarea3\
             -v /tmp/.X11-unix:/tmp/.X11-unix \
             -v /lib/modules:/lib/modules \
             -v "$(pwd)/tarea3/":/home/tarea3/pox/pox/tarea3/:ro \
             -v "$(pwd)/topologia/":/home/tarea3/pox/pox/topology/:ro \
             tarea3

#pox
#en la consola usada en el paso anterior ejecuten este comando cuando tengan o quiran probar sus controladores

python3 pox.py log.level --DEBUG misc.full_payload tarea3.l2_learning openflow.discovery openflow.spanning_tree --no-flood --hold-down

#mininet
#en una consola a parte ejecuten los siguientes comandos para la parte de mininet

docker exec -it tarea3 bash
cd pox/topology
mn --custom topology.py --topo MyTopo --mac --controller remote --switch ovsk

#notas

guarden el codigo de sus controladores en una carpeta llamada "tarea3" y las topologias en la carpeta "topologia".