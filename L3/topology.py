#Ejecucion: sudo mn --custom topologia1.py --topo MyTopo --controller remote --switch ovsk --mac
from mininet.topo import Topo
#from mininet.node import RemoteController
#from mininet.net import Mininet


class MyTopo(Topo):

    "Topologia numero 1"

    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        #net = Mininet(controller = RemoteController)
        #net.addController('c0')
        #Hosts y switches
        
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05')
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06')
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07')
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08')
        s1 = self.addSwitch( 's1', dpid = '1')
        s2 = self.addSwitch( 's2', dpid = '2')
        s3 = self.addSwitch( 's3', dpid = '3')
        s4 = self.addSwitch( 's4', dpid = '4')

        #Anadir links 
        self.addLink( h1, s1, 1, 2)
        self.addLink( h2, s1, 4, 3)
        self.addLink( s1, s2, 5, 6)
        self.addLink( h3, s2, 8, 7)
        self.addLink( h4, s2, 10, 9)
        self.addLink( s2, s3, 11, 12)
        self.addLink( h5, s3, 14, 13)
        self.addLink( h6, s3, 16, 15)
        self.addLink( s3, s4, 17, 18)
        self.addLink( h7, s4, 22, 21)
        self.addLink( h8, s4, 20, 19)
        self.addLink( s4, s1, 23, 24)

topos = {'MyTopo': (lambda: MyTopo())}
