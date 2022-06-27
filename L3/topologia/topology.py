# Ejecucion: sudo mn --custom topologia1.py --topo MyTopo --controller remote --switch ovsk --mac
from pydoc import cli
from mininet.topo import Topo
from mininet.node import RemoteController
from mininet.net import Mininet
from mininet.cli import CLI


class MyTopo(Topo):
    "Topologia Anillo simple"
    def __init__(self):
        "Creacion de topologia personalizada"
        Topo.__init__(self)
        net = Mininet(controller = RemoteController)
        net.addController('c0')
        
        # Hosts y switches
        h1 = self.addHost('h1', mac='00:00:00:00:00:01')
        h2 = self.addHost('h2', mac='00:00:00:00:00:02')
        h3 = self.addHost('h3', mac='00:00:00:00:00:03')
        h4 = self.addHost('h4', mac='00:00:00:00:00:04')
        h5 = self.addHost('h5', mac='00:00:00:00:00:05')
        h6 = self.addHost('h6', mac='00:00:00:00:00:06')
        h7 = self.addHost('h7', mac='00:00:00:00:00:07')
        h8 = self.addHost('h8', mac='00:00:00:00:00:08')
        h9 = self.addHost('h9', mac='00:00:00:00:00:09')
        h10 = self.addHost('h10', mac='00:00:00:00:00:0A')
        s1 = self.addSwitch('s1', dpid='1')
        s2 = self.addSwitch('s2', dpid='2')
        s3 = self.addSwitch('s3', dpid='3')
        s4 = self.addSwitch('s4', dpid='4')
        s5 = self.addSwitch('s5', dpid='5')

        # Add links
        # Links switch - switch
        self.addLink(s1, s2, 1, 2)
        self.addLink(s2, s3, 3, 4)
        self.addLink(s3, s5, 5, 6)
        self.addLink(s5, s4, 7, 8)
        self.addLink(s4, s1, 9, 10)
        # Links switch - host
        # Switch 1
        self.addLink(s1, h1, 11, 12)
        self.addLink(s1, h2, 13, 14)
        # Switch 2
        self.addLink(s2, h3, 15, 16)
        self.addLink(s2, h4, 17, 18)
        # Switch 3
        self.addLink(s3, h5, 19, 20)
        self.addLink(s3, h6, 21, 22)
        # Switch 5
        self.addLink(s5, h9, 23, 24)
        self.addLink(s5, h10, 25, 26)
        # Switch 4
        self.addLink(s4, h7, 27, 28)
        self.addLink(s4, h8, 29, 30)

        # Start
        #net.build()
        #net.start()
        #CLI(net)
        #net.stop()


topos = {'MyTopo': (lambda: MyTopo())}
