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
    if  not(hextet.isalnum()):
        print('IP address should not contain any special characters')
        print("invalid IP address")
        sys.exit()
    if hextet=='0':
        continue
    if len(hextet)!=4:
        print("each hextet should contain only 4 digits")
        sys.exit()
    pow=3
    sum=0
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
        hex_values={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                    '8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
        if i not in hex_values:
            print("invalid IP address")
            sys.exit()
        
        cal=(hex_values[i]*(16**pow))
        #print(cal)
        sum=sum+cal
        pow=pow-1
    #print(sum)
        if sum>=0 or sum<=65535:
            continue
        else:
            print("invalid IP address")
            sys.exit()
print('valid IP address')






