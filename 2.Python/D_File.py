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

write2('./fcictest.txt','aaaaa\n')
#print( read('./fcictest.txt'))
rows=read('./fcictest.txt').split('\n')
for  r in rows:
    print(r)
