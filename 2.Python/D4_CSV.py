import csv

fp=open('./fcicCSVtest.csv','w')
wr = csv.writer(fp)
wr.writerow((1,2,3))
fp.close()