![status:incomplete](https://img.shields.io/badge/status-incomplete-red)

# smog
<img src="smog-project.png" width="25%" height="25%">

smog is a quick-and-dirty private cloud builder/orchestration system.  Build a truth table of tenancies, synchronize them across local network devices and servers, and start empty containers in new namespaces.  Works with [loadstone](https://github.com/joeHeartsmith/loadstone) to peer your private cloud with public cloud providers.  (Right now, tenancies are VLAN-based (with a 1-to-1 VLAN-to-namespace mapping), and MAC NAT is applied to ferry traffic in from the public internet to individual service containers.)  Also works with a TLS-terminating proxy so that traffic may be filtered by an inline IPS.
Honestly, this is just how I orchestrate my homelab, and it's built specifially for that, but could also work in a more generic capacity (i.e. if you have a list of VLANs, you could synchronize that information across a Linux router and a Cisco switch if that's all you were after).

