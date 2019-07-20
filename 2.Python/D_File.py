def write(file,content):   #override write
    f=open(file,'w+')
    f.write(content)
    f.close()

def write2(file,content):  #append write
    f=open(file,'a')
    f.write(content)
    f.close()

def read(file):
    f=open(file,'r')
    return f.read()

write2('./fcictest.txt','123123')
print( read('./fcictest.txt'))