# from ipaddress import IPv4Address
import ipaddress
#____________________________________________________________________________________________________________________

# CLASS C SEGMENT
file_a = open("Net.txt", "a")
#____________________________________________________________________________________________________________________
# INPUTS
num_of_departs = int(input("Enter how many Departments your Organization Has ? : "))
if num_of_departs % 2 == 1 or num_of_departs == 1:
    num_of_departs += 1

# Consisting Variables > Starting Address and Gap for Adding...
sub_mask = str(ipaddress.ip_address("192.168.0.0"))
ip_add = 256 / num_of_departs
flag = 0

# First FOR LOOP to Input The names and Host Computers in each department Iteratively...
maxi = []
for i in range(num_of_departs):
    dip_name = str(input("Enter the name of your Department : "))
    com_nos = int(input("How many Host Computers are in Use ? : "))
    maxi.append(com_nos)
    maximum_hosts = max(maxi)
    print()
# Primary Decision of Choosing the CLASS
    if  maximum_hosts < 256:
     flag = 1
    elif  maximum_hosts > 265:
        flag = 2
    else:
        flag = 3

# _________________________________________________________________________________________________________
# Checking for the Suitable Class (A or B or C)
# Class C
if flag == 1:
    print("Going with CLASS C 📍 ")
    given_address = str(ipaddress.ip_address(input("Enter the given IP Address : ")))
    tot = 0
# Creating Network Address
    if given_address == sub_mask:
         for i in range(int(num_of_departs)):
            sub_mask = ipaddress.IPv4Address('192.168.0.0') + tot
            tot = tot + int(ip_add)
            final = "Network Addresses " + " >>> " + str(sub_mask) + " " + "\n"
            file_a.write(str(final))

    else:
         file_a = open("Net.txt", "a")
         for i in range(int(num_of_departs)):
            sub_mask = ipaddress.IPv4Address(given_address) + tot
            tot = tot + int(ip_add)
            final = "Network Addresses " + " >>> " + str(sub_mask) + " " + "\n"
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
        final = "Broadcast Addresses " + " >>> " + str(br_add) + " " + '\n'
        file_a.write(str(final))

#print("Written to Net.txt File...")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# CLASS B

if flag == 2:
    print("Going with CLASS B 📍")
    print()
    given_address = str(ipaddress.ip_address(input("Enter the given IP Address : ")))
    broken_list = given_address.split(".")
    print('Broken list = ', broken_list)
    #__________________________________________________________________________________________________________
    #  Creating Network Address
