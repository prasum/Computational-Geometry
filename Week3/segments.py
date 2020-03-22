#Using Python3
def check_segment(line1,line2):
    if(collinear(line1,line2)):
        if((line1[0][1]<=line2[0][1]<line1[1][1]) and (line2[0][1]<line1[1][1]<=line2[1][1])):
            
            return True
        elif((line1[0][1]<=line2[0][1]<line1[1][1]) and (line1[0][1]<line2[1][1]<=line1[1][1])):
            
            return True
        elif((line2[0][1]<=line1[0][1]<line2[1][1]) and (line1[0][1]<line2[1][1]<=line1[1][1])):
            
            return True
        elif((line2[0][1]<=line1[0][1]<line2[1][1]) and (line2[0][1]<line1[1][1]<=line2[1][1])):
            
            return True
        elif((line1[0][1]==line2[1][1]==line1[1][1]==line2[0][1])):
            if((line1[0][0]<=line2[0][0]<line1[1][0]) and (line2[0][0]<line1[1][0]<=line2[1][0])):
            
                return True
            elif((line1[0][0]<=line2[0][0]<line1[1][0]) and (line1[0][0]<line2[1][0]<=line1[1][0])):
            
                return True
            elif((line2[0][0]<=line1[0][0]<line2[1][0]) and (line1[0][0]<line2[1][0]<=line1[1][0])):
            
                return True
            elif((line2[0][0]<=line1[0][0]<line2[1][0]) and (line2[0][0]<line1[1][0]<=line2[1][0])):
            
                return True
            else:
                return False
        
         
        else:
            return False
        
    else:
        return False
  
def collinear(line1,line2):
    if((line1[0][0]-line2[0][0])*(line1[0][1]-line2[1][1])-(line1[0][1]-line2[0][1])*(line1[0][0]-line2[1][0])==0 and (line1[1][0]-line2[0][0])*(line1[1][1]-line2[1][1])-(line1[1][1]-line2[0][1])*(line1[1][0]-line2[1][0])==0):
        return True
    elif((line2[0][0]-line1[0][0])*(line2[0][1]-line1[1][1])-(line2[0][1]-line1[0][1])*(line2[0][0]-line1[1][0])==0 and (line2[1][0]-line1[0][0])*(line2[1][1]-line1[1][1])-(line2[1][1]-line1[0][1])*(line2[1][0]-line1[1][0])==0):
        return True
    else:
        return False

'''def check_point1(line1,line2):
    if(check_point2(line1,line2)):
        if((line2[0][0]-line1[0][0])*(line2[0][1]-line1[1][1])-(line2[0][1]-line1[0][1])*(line2[0][0]-line1[1][0])==0):
            print("The intersection point is" + " "+ "("+str(line2[0][0])+","+" "+str(line2[0][1])+")"+".")
            return True
        elif((line2[1][0]-line1[0][0])*(line2[1][1]-line1[1][1])-(line2[1][1]-line1[0][1])*(line2[1][0]-line1[1][0])==0):
            print("The intersection point is" + " "+ "("+str(line2[1][0])+","+" "+str(line2[1][1])+")"+".")
            return True
        elif((line1[0][0]-line2[0][0])*(line1[0][1]-line2[1][1])-(line1[0][1]-line2[0][1])*(line1[0][0]-line2[1][0])==0):
            print("The intersection point is" + " "+ "("+str(line1[0][0])+","+" "+str(line1[0][1])+")"+".")
            return True
        elif((line1[1][0]-line2[0][0])*(line1[1][1]-line2[1][1])-(line1[1][1]-line2[0][1])*(line1[1][0]-line2[1][0])==0):
            print("The intersection point is" + " "+ "("+str(line1[1][0])+","+" "+str(line1[1][1])+")"+".")
            return True
        else:
            return False
    else:
         return False
         '''

def sign(x):
    if(x>0):
         return 1
    elif(x==0):
        return 0
    elif(x<0):
         return -1
         
def check_point2(line1,line2):
    if(sign((line1[0][0]-line2[0][0])*(line1[0][1]-line2[1][1])-(line1[0][1]-line2[0][1])*(line1[0][0]-line2[1][0]))!=sign((line1[1][0]-line2[0][0])*(line1[1][1]-line2[1][1])-(line1[1][1]-line2[0][1])*(line1[1][0]-line2[1][0]))):
         if(sign((line2[0][0]-line1[0][0])*(line2[0][1]-line1[1][1])-(line2[0][1]-line1[0][1])*(line2[0][0]-line1[1][0]))!=sign((line2[1][0]-line1[0][0])*(line2[1][1]-line1[1][1])-(line2[1][1]-line1[0][1])*(line2[1][0]-line1[1][0]))):
            return True
         else:
            return False
    else:
         return False
    
         
         
def check_intersection(line1,line2):
    if((line1[0][0]==line2[0][0]) and (line1[0][1]==line2[0][1])):
        print("The intersection point is" + " "+ "("+str(line1[0][0])+","+" "+str(line1[0][1])+")"+".")
        return True
    elif((line1[0][0]==line2[1][0]) and (line1[0][1]==line2[1][1])):
        print("The intersection point is" + " "+ "("+str(line1[0][0])+","+" "+str(line1[0][1])+")"+".")
        return True
    elif((line1[1][0]==line2[0][0]) and (line1[1][1]==line2[0][1])):
        print("The intersection point is" + " "+ "("+str(line1[1][0])+","+" "+str(line1[1][1])+")"+".")
        return True
    elif((line1[1][0]==line2[1][0]) and (line1[1][1]==line2[1][1])):
        print("The intersection point is" + " "+ "("+str(line1[1][0])+","+" "+str(line1[1][1])+")"+".")
        return True
    elif(check_point2(line1,line2)):
        
        '''k1=(((line1[1][0]*line1[0][1])-(line1[0][0]*line1[1][1]))/(line1[1][0]-line1[0][0]))
        k2=(((line2[1][0]*line2[0][1])-(line2[0][0]*line2[1][1]))/(line2[1][0]-line2[0][0]))
        m1=(line1[1][1]-line1[0][1])/(line1[1][0]-line1[0][0])
        m2=(line2[1][1]-line2[0][1])/(line2[1][0]-line2[0][0])
        x=(k2-k1)//(m1-m2)
        y=(m2*k1-m1*k2)//(m2-m1)
        '''
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
    
        x=int(x)
        y=int(y)
        print("The intersection point is" + " "+ "("+str(x)+","+" "+str(y)+")"+".")
        return True
    else:
        return False
         
ax,ay,bx,by=input().split()
cx,cy,dx,dy=input().split()
ax,ay,bx,by=int(ax),int(ay),int(bx),int(by)
cx,cy,dx,dy=int(cx),int(cy),int(dx),int(dy)
line1=list()
line2=list()
if(ay<by):
    line1.append((ax,ay))
    line1.append((bx,by))
    
elif(ay==by):
    if(ax<bx):
        line1.append((ax,ay))
        line1.append((bx,by))
    else:
        line1.append((bx,by))
        line1.append((ax,ay))
else:
    line1.append((bx,by))
    line1.append((ax,ay))
    
if(cy<dy):
    line2.append((cx,cy))
    line2.append((dx,dy))
elif(cy==dy):
    if(cx<dx):
        line2.append((cx,cy))
        line2.append((dx,dy))
    else:
        line2.append((dx,dy))
        line2.append((cx,cy))
else:
    line2.append((dx,dy))
    line2.append((cx,cy))
    
ON_SEGMENT=False
ON_INTERSECTION=False

ON_SEGMENT=check_segment(line1,line2)
if(ON_SEGMENT):
    print("A common segment of non-zero length.")
else:
    ON_INTERSECTION=check_intersection(line1,line2)
    if(not ON_INTERSECTION):
         print("No common points.")
