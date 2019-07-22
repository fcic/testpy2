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
print(rows)