fd = open ("compareALL.dat","r")    #open file
count=-1;   Name=[]; SEQ1=[]; SEQ2=[]; 
for line in fd:   
   count=count+1
   if count%3==0: 
      Name.append(line)
   if count%3==1: 
      SEQ1.append(line)
   if count%3==2: 
      SEQ2.append(line)

aminoacid=["A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"]
for v in range (0, len(aminoacid)):
    amino=aminoacid[v]
    delta=[]
    fw = open (amino+".txt","w")
    fm = open (amino+"delta.txt","w")
    def split(word): 
        return [char for char in word]     
    for e in range (0, len(Name)):
        GLY1=0.0; GLY2=0.0;
        s1=split(SEQ1[e]); s2=split(SEQ2[e]);
      # print s1, s2, len(s1), len(s2)
        if(len(s1)*0.1*10/len(s2)<=1.05 and len(s1)*0.1*10/len(s2)>=0.95):     
           for a in range(0,len(s1)):    
               if s1[a]==amino:
                  GLY1=GLY1+1
           for b in range(0,len(s2)):    
               if s2[b]==amino:
                  GLY2=GLY2+1
           fw.write(str(GLY1/len(s1))+' '+str(GLY2/len(s2))+' '+str(Name[e])+' '+str('\n'))    
           delta.append((GLY1/len(s1)-GLY2/len(s2))*100)
    #print delta
    print len(delta)
########################################################################
    Dict=[]
    for l in range (0, 9):
        XL=l*0.25-1.125; XH=l*0.25-1.125+0.25; Point=0
        if (l==0 ):
            for p in range (0, len(delta)):
                if (delta[p]<XH):
                      Point=Point+1.00; 
            Dict.append(Point)
        elif(l==8):
            for p in range (0, len(delta)):
                if (delta[p]>=XL):
                      Point=Point+1.00; 
            Dict.append(Point)
        else: 
            for p in range (0, len(delta)):
                if (delta[p]>=XL and delta[p]<XH):
                      Point=Point+1.00; 
            Dict.append(Point)

        fm.write(str(l*0.25-1.0)+' '+str(Dict[l]))
        fm.write('\n')
          
