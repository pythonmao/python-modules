import netaddr

ip = netaddr.IPAddress('10.0.2.15')
print ip.version
print repr(ip)
print ip

print str(ip)
print ip.format()
print int(ip)
print hex(ip)

ip = netaddr.IPNetwork('10.0.2.15/20')
print ip.network, ip.broadcast
print ip.netmask, ip.hostmask
print ip.size
print ip.ip.bits()
print ip.network.bits()
print ip.netmask.bits()
print ip.broadcast.bits()
list_ip = list(ip)
print len(list_ip)
