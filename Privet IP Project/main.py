
import ipaddress
# INPUTS
# from ipaddress import IPv4Address
file_a = open("Net.txt", "a")
num_of_departs = int(input("Enter how many Departments your Organization Has ? : "))
print()
loop = num_of_departs
for i in range(loop):
    file_a = open("Net.txt", "a")
    dip_name = str(input("Enter the name of your Department : "))
    com_nos = int(input("How many Host Computers are in Use ? : "))
    print()
# check for an even number
if num_of_departs % 2 == 1 or num_of_departs == 1:
    print()
    print("SORRY...You only can Subnet by Even Counts...")
# ____________________________________________________________________________________________________________________
# CALCULATIONS if given privet IP == to Default
else:
    tot = 0
    ip_add = 256 / num_of_departs
    sub_mask = str(ipaddress.ip_address("192.168.0.0"))
    given_address = str(ipaddress.ip_address(input("Enter the given IP Address : ")))
    print()
    file_a = open("Net.txt", "a")
# Creating Network Address
    if given_address == sub_mask:
        for i in range(int(num_of_departs)):
            sub_mask = ipaddress.IPv4Address('192.168.0.0') + tot
            tot = tot + int(ip_add)
            final = "Network Addresses " + " >>> " + str(sub_mask) + " "+"\n"
            file_a.write(str(final))

    else:
        file_a = open("Net.txt", "a")
        for i in range(int(num_of_departs)):
            sub_mask = ipaddress.IPv4Address(given_address) + tot
            tot = tot + int(ip_add)
            final = "Network Addresses " + " >>> " + str(sub_mask) + " "+"\n"
            file_a.write(str(final))

    print()

    # Creating Broadcast address
    ip_add = 256 / num_of_departs
    tot = 0
    gap = ip_add - 1
    file_a = open("Net.txt", "a")
    for i in range(int(num_of_departs)):
        tot = tot + gap
        br_add = ipaddress.IPv4Address(given_address) + int(tot)
        if i == 0:
            gap = ip_add
            br_add = ipaddress.IPv4Address(given_address) + int(tot)
        final = "Broadcast Addresses " + " >>> " + str(br_add) + " "+'\n'
        file_a.write(str(final))

    print()

