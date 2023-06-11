# High-Speed-Network_and_Switching_mininet
High Speed Network and Switching 

* Module's Description:
The project will explore the architecture of network elements used in high speed networks, provide the survey of
modern network protocols and discuss issues that face network architects who design and manage carrier networks.
Concepts will be illustrated by examples from Linux Networking Stack.

* Aims of the module:
The exponential increase of Internet and multimedia applications has accelerated research, development and deployment 
of high-speed networks. The course will provide understanding of key issues in network and network 
elements architectures, protocols and algorithms used in high-speed networks with some emphasis on switching and traffic management.

* Mininet Project 

                  |      Software      |   Software-Tool                    |     Version     |
                  |--------------------|------------------------------------|-----------------|
                  |         OS         |  Ubuntu-Desktop                    |     18.04       |
                  |    Test Bed        |      Mininet                       |    2.3.1d6      |
                  |     Controller     |      RYU                           |     -----       |
                  |     Switch         |  Open-v-switch                     |    2.9.6        |
                  | Traffic Generator  |  IPerf                             |   2.0.10        |
                  |  Virtual Box       |  Box Oracle VM Virtual Box Manager |     7.0         |
                  
|      Hardware      |     Version      |
|--------------------|------------------|
|  CPU - Processor   | Intel Core - i9  |
|        RAM         |       8 GB       |
| Hard-Disk-Capacity |      100 GB      |



# Analysis of Multi-path Network
![image](https://github.com/shahaf2284/High-Speed-Network_and_Switching_mininet/assets/122786017/686caa44-875a-4cd8-8617-ffb36bb10cd3)

describes the traffic splitting and path selection of the functional components
of multipath forwarding. The splitting of the traffic into traffic units is done by the traffic
splitting components, where each of the path is taken individually, and the path selection
component is determined. In the path selection if the forwarding processor is busy then
the output link will be attached by each traffic unit in the input queue. Each of the
different models of multipath forwarding will perform the load distributions in numerous
manners. Due to the internal functional components there are different shortcomings and
advantages that each of the models exhibit, like the path selection and traffic splitting

# Design Specification
In this section we will describe the high-level-diagram of this research implementation.
To start the maximum-flow approach we need all the paths of the network as input.
When the maximum-flow approach starts BFS (Breadth-First-Search) checks the level of
multipath network graph, by doing this we will get to know the value of every node to
find the short distance from source node. And the edges from the level graph do multiple
iterations of DFS (Depth-First-Search) approach from source to destination until there
are no augmented paths possible, then the maximum flow is found. Once we received
the maximum flow-value RYU-Controller sets that as constant value for maximum paths
which is used for multipath routing. Through this approach we can improve the through-put(bandwidth). The below defines the high-level execution of this project.

![image](https://github.com/shahaf2284/High-Speed-Network_and_Switching_mininet/assets/122786017/ba046bf3-4547-4edb-9da1-27a6be7c4b42)



