#Ejecucion: sudo mn --custom topologia1.py --topo MyTopo --controller remote --switch ovsk --mac
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.net import Mininet


class MyTopo(Topo):

    "Topologia dos caminos"

    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        #net = Mininet(controller = RemoteController)
        #net.addController('c0')
        
        #hosts
        h1 = self.addHost( 'h1', mac = '00:00:00:00:00:01')
        h2 = self.addHost( 'h2', mac = '00:00:00:00:00:02')
        h3 = self.addHost( 'h3', mac = '00:00:00:00:00:03')
        h4 = self.addHost( 'h4', mac = '00:00:00:00:00:04')
        h5 = self.addHost( 'h5', mac = '00:00:00:00:00:05')
        h6 = self.addHost( 'h6', mac = '00:00:00:00:00:06')
        h7 = self.addHost( 'h7', mac = '00:00:00:00:00:07')
        h8 = self.addHost( 'h8', mac = '00:00:00:00:00:08')

        #switches
        s1 = self.addSwitch( 's1', dpid = '1')
        s2 = self.addSwitch( 's2', dpid = '2')
        s3 = self.addSwitch( 's3', dpid = '3')
        s4 = self.addSwitch( 's4', dpid = '4')
        s5 = self.addSwitch( 's5', dpid = '5')


        #links 
        self.addLink(s1, s2, 1, 2)
        self.addLink(s2, s3, 3, 4)
        self.addLink(s3, s4, 5, 6)
        self.addLink(s4, s5, 7, 8)
        self.addLink(s5, s1, 9, 10)
        self.addLink(s4, s1, 11, 12)

        #links switch 1
        self.addLink(s1, h1, 13, 14)
        self.addLink(s1, h2, 15, 16)
        #links switch 2
        self.addLink(s2, h3, 17, 18)
        self.addLink(s2, h4, 19, 20)
        #links switch 3
        self.addLink(s3, h5, 21, 22)
        self.addLink(s3, h6, 23, 24)
        #links switch 5
        self.addLink(s5, h7, 25, 26)
        self.addLink(s5, h8, 27, 28)

topos = {'MyTopo': (lambda: MyTopo())}
