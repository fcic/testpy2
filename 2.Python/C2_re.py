import re
#sub() = replace


def match(regex,str):
  return re.findall(regex , str, re.M|re.I)

str="Cats are smarter than dogs";
#regex=r'(.*) are (.*?) .*';

matchObj=match(regex,str);  #re.match(regex, str, re.M|re.I);
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"6t