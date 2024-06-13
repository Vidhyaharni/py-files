'''IPv6
 example-2001:0000:130F:0000:0000:09C0:876A:130B
  the alphabets used should be either capital or small letter
   hexa-decimal numbers is used in IPv6 '''

import sys
ip=input('enter the IP address : ')
hextets=ip.split(':')
if len(hextets)!=8:
    print('number of hextet must be 8')
    sys.exit()
up=False     
low=False
for hextet in hextets:
    if  not(hextet.isalnum() or hextet.isnumeric() or hextet.isalpha()):
        print('IP address should not contain any special characters')
        print("invalid IP address")
        sys.exit()
    if len(hextet)!=4:
        print("each hextet should contain only 4 digits")
        sys.exit()
    for i in hextet:
        if i.isupper():
            up=True
        elif i.islower():
            low=True
        if up==True and low==True:
            print("characters present in IP address must be either capital or small letters")
            print("invalid IP address")
            sys.exit()
        i=i.lower()
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='a' or i=='b' or i=='c' or i=='d' or i=='e' or i=='f':
            continue   
        else:
            print("invalid IP address")
            sys.exit()
print('valid IP address')