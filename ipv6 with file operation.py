'''IPv6 using file operation
 example-2001:0000:130F:0000:0000:09C0:876A:130B
  the alphabets used should be either capital or small letter
   hexa-decimal numbers is used in IPv6 '''


def ip_address():
    
    hextets=ip.split(':')
    if len(hextets)!=8:
        print('number of hextet must be 8')
        write.write('invalid,number of hextet must be 8\n\n')
        return
        
    up=False     
    low=False
    for hextet in hextets:
        if  not(hextet.isalnum()):
            print('IP address should not contain any special characters')
            
            write.write('invalid,IP address should not contain any special characters\n\n')
            return
            
        if hextet=='0':
            continue
        if len(hextet)!=4:
            print("each hextet should contain only 4 digits")
            write.write('invalid,each hextet should contain only 4 digits\n\n')
            return
        hex_values={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                        '8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}   
        pow=3
        sum=0
        for i in hextet:
            if i.isupper():
                up=True
            elif i.islower():
                low=True
            if up==True and low==True:
                print("characters present in IP address must be either capital or small letters")
                write.write('invalid,characters present in IP address must be either capital or small letters\n\n')
                return
                
            i=i.lower()
            
            if i not in hex_values:
                print("invalid IP address")
                write.write('invalid IP address\n\n')
                return
            cal=(hex_values[i]*(16**pow))
            sum=sum+cal
            pow=pow-1
            if sum>=0 or sum<=65535:
                continue
            else:
                print("invalid IP address")
                write.write('invalid IP address\n\n')
                return
                
    print('valid IP address')
    write.write('valid\n\n')
    return
    

input=open('IP Address input.txt')
for ip_add in input:
    ip=ip_add.strip()
    write=open ('validation.txt','a')
    write.write('IP Address : '+ip+'\n')
    print(ip.strip())
    ip_address()
    print()
input.close()
write.close()
