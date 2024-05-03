![status:incomplete](https://img.shields.io/badge/status-incomplete-red)

# smog
<img src="smog-project.png" width="25%" height="25%">

smog is a quick-and-dirty private cloud builder/orchestration system.  Build a truth table of tenancies, synchronize them across local network devices and servers, and start empty containers in new namespaces.  Works with [loadstone](https://github.com/joeHeartsmith/loadstone) to peer your private cloud with public cloud providers in an ...interesting way.  (Right now, tenancies are VLAN-based (with a 1-to-1 VLAN-to-namespace mapping), and MAC NAT is applied to ferry traffic in from the public internet to individual service containers.)
