#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call
import random

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8',link=TCLink)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)	
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.9', defaultRoute=None)

    info( '*** Add links\n')
    #net.addLink(h1, s1,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s1, s2,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s1, s3,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s1, s4,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s4, s7,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s3, s6,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s2, s5,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s5, s8,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s6, s9,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s7, s10,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s10, s11,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s8, s11,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s11, h2,cls=TCLink,bw=random.randint(minbw,maxbw))
    #net.addLink(s9, s11,cls=TCLink,bw=random.randint(minbw,maxbw))
	


 #------------------ CUSTOM BANDWIDTHS and delays PER LINK --------------------
# defining link options
    #    linkopt5 = dict(bw=5, delay='1ms', cls=TCLink)
     #   linkopt10 = dict(bw=10, delay='1ms', cls=TCLink)
      #  linkopt15 = dict(bw=15, delay='1ms', cls=TCLink)
       # linkopt50 = dict(bw=50, delay='1ms', cls=TCLink)
        #linkopt100 = dict(bw=100, delay='1ms', cls=TCLink)
		

        # adding links
        # sw1
        #net.addLink(sw1, s1, **linkopt100, port1=12000, port2=12001)
    net.addLink(h1, s1,bw=1000)
    net.addLink(s1, s2,bw=10)
    net.addLink(s1, s3,bw=10)
    net.addLink(s1, s4,bw=10)
    net.addLink(s4, s7,bw=10)
    net.addLink(s3, s6,bw=10)
    net.addLink(s2, s5,bw=10)
    net.addLink(s5, s8,bw=10)
    net.addLink(s6, s9,bw=10)
    net.addLink(s7, s10,bw=10)
    net.addLink(s10, s11,bw=10)
    net.addLink(s8, s11,bw=10)
    net.addLink(s11, h2,bw=1000)
    net.addLink(s9, s11,bw=10)
    net.addLink(h3, s1,bw=1000)
    net.addLink(h4, s1,bw=1000)





    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s7').start([c0])
    net.get('s2').start([c0])
    net.get('s8').start([c0])
    net.get('s10').start([c0])
    net.get('s1').start([c0])
    net.get('s9').start([c0])
    net.get('s11').start([c0])
    net.get('s6').start([c0])
    net.get('s4').start([c0])
    net.get('s3').start([c0])
    net.get('s5').start([c0])


    info( '*** Post configure switches and hosts\n')
    # h1.cmd('xterm')
    # h2.cmd('xterm')
    CLI(net)
    net.stop()

if __name__=='__main__':
    setLogLevel('info')
    myNetwork()
