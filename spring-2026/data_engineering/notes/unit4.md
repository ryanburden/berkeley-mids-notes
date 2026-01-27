Containers vs VM
- VM (virtual machine)
    - Virtualization or emulation of a physical hardware computer
    - OS runs on a VM instead of a physical hardware computer
    - Multiple VMs can run on a single physical hardware computer

- Container
    - Virutalization or emulation of an OS
    - Some say lightweight VM
    - Most modern computing is done in these containers (or clusters of containers)

Multiples
- Multiple containers can run in the same VM
- Multiple VMs can run on the same physical hardware
    - on top of a hypervisor on top of the hardware (cloud-based VMs)
    - on top of the OS on top of the hardware (desktop VMs)

Containers can run in several places
- in a VM on top of a hypervisor
- on an OS on physical hardware (windows, mac)
- in a VM on an OS on hardware

Containers are the same everywhere
- emulation at the OS level removes dependencies of where they run

Overhead
- Containers add a software layer on top of the VMs
- Containers run slower than VMs w/o containers
- Consensus: overhead of containers in worth it, and benefits outweigh performance hit
- Performance hit is nowhere near the performance hit of a desktop GUI

SOA: Service-Oriented Architecture
- Most modern apps use SOA
- SOA typically involve large monolithic services due to prior technology limitations on hardware and software
- Modern technologies allow us to use smaller services

Microservices
- Smaller services
- Better performance (cpu, speed, memory)
- Easier to develop and maintain

Bug Worst Case
- the worst case is a bug that causes memory corruption
    - not bad enough to crash
    - data corruption errors might not be found for hours, days, or even weeks

Microservices Using Containers
- For each transaction (or login), give each customer their own private container
- When transaction ends, destroy container
- Equivalent to a reboot for each transaction or user
- Containers give a wall of separation between current users- added security
- Fresh container ensures that future users will not be impacted by past memory corruption

Microservices Use Cases

Bank Website
- customers login, access accounts, perform transactions, logout
- solution: create a private container for each user every time they login and destroy the container when they log out

Point of Sale
- transaction: computerized cash register scans items, computes, processes paymoent
- solution: for each transation, create a container, execute transaction in the container, then destroy container when done.

Container Images

Analogy to Object-Oriented

- OOP
    - Object is an instane of a class
    - A class can have an unlimited number of objects
- VM
    - VM is an instance of a VM image
    - An image can have unlimited number of VM
- Containers
    - Container is an instance of a container image
    - An image can have an unlimited number of containers

Analogy to Class Hierarchies
- Class hierarchy in OOP
    - class can be the parent of other classes
    - class can be the child of other classes
- VM image hierarchy
    - VM image can be the parent of other VM images
    - VM image can be the child of other VM images
- Container image hierarchy
    - Container image can be the paretn of other container images
    - Container image can be the child of other container images

Container Image Building
- Scripted process
    - start with a container image
    - create a container from the image
    - customize the container
        - install software, change config, add users, groups, directories, files, permissions ...
    - create a new image from our customizations
- Base images are pure OSs