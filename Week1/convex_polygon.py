#Python3
m=input()
m=int(m)
vertices=[]
edges=[]
border=False
poly_points=input().split()
for k in range(0,2*m-1,2):
    vertices.append((int(poly_points[k]),int(poly_points[k+1])))

for t in range(m-1):
    edges.append([vertices[t],vertices[t+1]])

edges.append([vertices[m-1],vertices[0]])


n=input()
n=int(n)
points=[]
count=0
for i in range(n):
    px,py=input().split()
    px,py=int(px),int(py)
    points.append((px,py))
    
for j in range(len(points)):
    
    for u in range(len(vertices)):
        if((points[j][0]==vertices[u][0]) and (points[j][1]==vertices[u][1])):
            border=True
            
            
        
    for s in range(len(edges)):
        if(edges[s][1][1]<edges[s][0][1]):
            ax=edges[s][1][0]
            ay=edges[s][1][1]
            bx=edges[s][0][0]
            by=edges[s][0][1]
        elif(edges[s][0][1]<edges[s][1][1]):
            bx=edges[s][1][0]
            by=edges[s][1][1]
            ax=edges[s][0][0]
            ay=edges[s][0][1]
        else:
            ax=edges[s][1][0]
            ay=edges[s][1][1]
            bx=edges[s][0][0]
            by=edges[s][0][1]
        pax=points[j][0]-ax
        pay=points[j][1]-ay
        pbx=points[j][0]-bx
        pby=points[j][1]-by
        cross_prod=pax*pby-pbx*pay
        if(cross_prod==0 and ((ax<points[j][0]<bx) or (bx<points[j][0]<ax)) and ((ay<points[j][1]<by) or (by<points[j][1]<ay))):
            border=True
  
        if(cross_prod<0):
            if((ay<points[j][1]<by)or(by<points[j][1]<ay)):
                count=count+1
              
            if((ay==points[j][1])):
                    if((ay<by)):
                        count=count+1
                        
            if((by==points[j][1])):
                if((by<ay)):
                    count=count+1
                    
                    
                
    if(border):
        print("BORDER")
    else:    
        if(count%2==0):
            print("OUTSIDE")
        else:
            print("INSIDE")
        
    count=0
    border=False