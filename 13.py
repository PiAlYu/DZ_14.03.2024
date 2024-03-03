from ipaddress import *

mask = ip_address('255.255.252.0')
print(2 ** (f'{mask:b}'.count('0') - 1) - 2)
