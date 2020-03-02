#Python3
ax,ay,bx,by=input().split()
ax,ay,bx,by=int(ax),int(ay),int(bx),int(by)
n=input()
n=int(n)
points=[]
for i in range(n):
    px,py=input().split()
    px,py=int(px),int(py)
    points.append((px,py))

for j in range(len(points)):
    pax=points[j][0]-ax
    pay=points[j][1]-ay
    pbx=points[j][0]-bx
    pby=points[j][1]-by
    cross_prod=pax*pby-pbx*pay
    if(cross_prod>0):
        print("LEFT")
    elif(cross_prod<0):
        print("RIGHT")
    else:
        if(ax<bx):
            if((points[j][0]<ax) or (points[j][0]>bx)):
                print("ON_LINE")
            else:
                print("ON_SEGMENT")
        else:
            if((points[j][0]>ax) or (points[j][0]<bx)):
                print("ON_LINE")
            else:
                print("ON_SEGMENT")