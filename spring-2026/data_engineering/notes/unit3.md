Linux CLI

-OS: Operating system
-Examples
    - Windows, MacOS, Linux 

- OSs are layered
    - Kernel is the innermost layer
    - Desktop GUI is the outermost layer

- Peeling off layers
    - Linux can remove outer layers we don't need, most others OSs (Windows, Mac) cannot
    - Desktop GUI layer can put 50% or higher load on the OS
    - Removing desktop GUI can double or more performance. Useful for Cloud, VMs, containers, IoT

- Desktop GUI vs CLI
- Desktop GUI
    - easy to use
    - adds tremendous overhead- loss of performance
    - not scriptable
- CLI (command line interface)
    - hard to use
    - no loss of performance
    - highly scriptable

Linux CLI Business Cases

- Major Linux Distros (Distributions)
- GNU (GNUs not Unix) Linux
    - Red Hat
        - CentOS (community enterprise os, free version)
            - Amazon Linux
            - Oracle Linux
        - Fedora (experimental)
    - Debian
        - Ubuntu
        - Raspberry Pi OS, Various IoT

- Red Hat Branch
    - stable, large, corporate, servers, paid

- Debian
    - stable, lean
    - Ubuntu: Debian plus packages and drivers, good for desktop

- Use Cases
    - Fortune 500 company - RedHat, Desktop - Windows
    - Linux on the desktop - Ubuntu, has drivers for most devices
    - Linux VM that needs a GUI - Lubuntu (pared down version of Ubuntu)
    - Academic Research - Debian on servers, Ubuntu on desktop