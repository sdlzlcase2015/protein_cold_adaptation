import linecache
import fileinput
import re
start=[]; end=[]; point=[]
protein=[]; SEQ=[];
fp = open ("zebra.fasta","r")    #open file
count=-1; m=-1; n=-1; o=0; indicator=0;num=0
var=None
for line in fp: 
   count=count+1
   if (">tr|") in line: 
       SEQ.append(var)
       m=1; start.append(count);point.append(0);     
       subStr = re.findall(r'DANRE (.+?) OS=',line)[0]
       F1=subStr.replace('-', ' ')
       F2=F1.replace('_', ' ')
       F3=F2.replace(':', ' ')
       protein.append(F3)
       var=''  
   elif (">sp|") in line: 
       SEQ.append(var)
       m=1; start.append(count);point.append(0);     
       subStr = re.findall(r'DANRE (.+?) OS=',line)[0]
       F1=subStr.replace('-', ' ')
       F2=F1.replace('_', ' ')
       F3=F2.replace(':', ' ')
       protein.append(F3)
       var=''  
   else:
       var=var+line[0:(len(line)-1)]
   del line
  # print o, num

del count, n, fp

start2=[]; end2=[]; point2=[]
protein2=[]; SEQ2=[];
fh = open ("human.fasta","r")    #open file 
count2=-1; m2=-1; n2=-1; o2=0; indicator2=0;num2=0
var2=None 
for line2 in fh: 
   coun2=count2+1
   if (">tr|") in line2: 
      SEQ2.append(var2)
      m2=1; start2.append(count2);point2.append(0);     
      subStr2 = re.findall(r'HUMAN (.+?) OS=',line2)[0]
      F1=subStr2.replace('-', ' ')
      F2=F1.replace('_', ' ')
      F3=F2.replace(':', ' ')
      protein2.append(F3)
      var2=''  
   elif (">sp|") in line2: 
      SEQ2.append(var2)
      m2=1; start2.append(count2);point2.append(0);     
      subStr2 = re.findall(r'HUMAN (.+?) OS=',line2)[0]
      F1=subStr2.replace('-', ' ')
      F2=F1.replace('_', ' ')
      F3=F2.replace(':', ' ')
      protein2.append(F3)
      var2=''  
   else:
       var2=var2+line2[0:(len(line2)-1)]
   del line2

del count2, n2, fh

print protein[0], SEQ[1], len(protein), len(SEQ)
print protein2[0], SEQ2[1], len(protein2)


fdata = open ("compareALL.dat","w")
countM=0;
for idnum in range (0, len(protein)):
   indicator=0
   X=str(protein[idnum]);  
   for j in range (0, len(protein)):
      if (j!=idnum and protein[j]==X):
         indicator=1
         break
   if indicator==0:
        for idnum2 in range (0, len(protein2)):    
            if (protein2[idnum2].lower()==X.lower()):
                countM=countM+1
                fdata.write(protein[idnum]+'\n')
                fdata.write(SEQ[idnum+1]+'\n')
                fdata.write(SEQ2[idnum2+1]+'\n')
                print idnum, countM, X
                break
print countM


