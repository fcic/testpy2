import sys

def fcic(str):
  #print('hello world '+str);
  return 'hello world2 '+str;

#fcic('fcic');

#cmd input parameters
#print(str(sys.argv[1])); #str(sys.argv)

#print(len(sys.argv));

# for i in range(0,len(sys.argv)):
#   print(str(sys.argv[i]));

row = ['fcic','ob','peter']
# print(row)
#print(','.join(row))
rows = []
rows.append(','.join(row))
rows.append(','.join(row))
# print(rows)

ar = ['num:{}'.format(i) for i in range(1,20)]
print(ar)
# ['num:1', 'num:2', 'num:3', 'num:4', 'num:5', 'num:6', 'num:7', 'num:8', 'num:9', 'num:10', 'num:11', 'num:12', 'num:13', 'num:14', 'num:15', 'num:16', 'num:17', 'num:18', 'num:19']

#swich case
def Swcase(var):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
    }.get(var,'error') 

print(Swcase('a'))
