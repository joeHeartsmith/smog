#!/usr/bin/env python3
import csv, re

VLAN = 0
VLAN_DESCRIPTION = 1
VLAN_IPV6 = 2
VLAN_IPV4 = 3

DEFAULT_IPV6_NET = "80"
DEFAULT_IPV4_NET = "24"

IPV6_RE =     re.compile("^([0-9A-Fa-f_]{0,4}[:])*[0-9A-Fa-f_]{0,4}$")
IPV6_NET_RE = re.compile("^([0-9A-Fa-f_]{0,4}[:])*[0-9A-Fa-f_]{0,4}[/]\d{1,3}$")
IPV4_RE =     re.compile("^\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}$")
IPV4_NET_RE = re.compile("^\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[/]\d{1,2}$")

VLAN_PLAN_FILE = "./netplan.csv"
csvfile = open(VLAN_PLAN_FILE, newline='')

# FIXME: add entries to XLS file for which interface on which device each VLAN will live
#        also add error-handling (i.e. 'if' an IP address exists, assign it)
def createVlanEntry(style, vlan, description, ipv4=None, ipv6=None, interface=None):
    if style == "cisco":
        print("vlan {} name {}".format(vlan, description))
        print("interface {}".format(interface))
        print("switchport access vlan {}".format(vlan))
        print("ipv6 address {}".format(ipv6))
        print("ipv4 address {}".format(ipv4))
        print("----------------------------------------------")


if csv.Sniffer().has_header(csvfile.read(1024)):
  csvfile.seek(0)
  csvfile.readline()
else:
  csvfile.seek(0)

vlanplan = csv.reader(csvfile)
for row in vlanplan:
    vlan = None
    desc = None
    ipv6 = None
    ipv4 = None

    try:
        if (int(row[VLAN]) >= 1 and int(row[VLAN]) <= 4094):
            vlan = row[VLAN]
    except:
        pass

    desc = row[VLAN_DESCRIPTION]

    if IPV6_RE.match(row[VLAN_IPV6]):
        ipv6 = row[VLAN_IPV6] + "/" + DEFAULT_IPV6_NET
    elif IPV6_NET_RE.match(row[VLAN_IPV6]):
        ipv6 = row[VLAN_IPV6]

    if IPV4_RE.match(row[VLAN_IPV4]):
        ipv4 = row[VLAN_IPV4] + "/" + DEFAULT_IPV4_NET
    elif IPV4_NET_RE.match(row[VLAN_IPV4]):
        ipv4 = row[VLAN_IPV4]


    if vlan != None:
        createVlanEntry("cisco", vlan, desc, ipv4, ipv6)
