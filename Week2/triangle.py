#Python3
ax,ay,bx,by,cx,cy=input().split()
ax,ay,bx,by,cx,cy=int(ax),int(ay),int(bx),int(by),int(cx),int(cy)
n=input()
n=int(n)
points=[]
border=False

for i in range(n):
    px,py=input().split()
    px,py=int(px),int(py)
    points.append((px,py))

for j in range(len(points)):
    pax=points[j][0]-ax
    pay=points[j][1]-ay
    pbx=points[j][0]-bx
    pby=points[j][1]-by
    pcx=points[j][0]-cx
    pcy=points[j][1]-cy
    cross_prod_pab=pax*pby-pbx*pay
    cross_prod_pca=pcx*pay-pax*pcy
    cross_prod_pbc=pbx*pcy-pcx*pby
    if(cross_prod_pab==0):
        border=True
        if((cross_prod_pca>0) and (cross_prod_pbc>0)):
            print("BORDER")
        elif((cross_prod_pca==0) or (cross_prod_pbc==0)):
            print("BORDER")
        elif((cross_prod_pca<0) and (cross_prod_pbc<0)):
            print("BORDER")
        else:
            print("OUTSIDE")
            
    elif(cross_prod_pbc==0):
        border=True
        if((cross_prod_pab>0) and (cross_prod_pca>0)):
            print("BORDER")
        elif((cross_prod_pab==0) or (cross_prod_pca==0)):
            print("BORDER")
        elif((cross_prod_pab<0) and (cross_prod_pca<0)):
            print("BORDER")
        else:
            print("OUTSIDE")
            
    elif(cross_prod_pca==0):
        border=True
        if((cross_prod_pab>0) and (cross_prod_pbc>0)):
            print("BORDER")
        elif((cross_prod_pab==0) or (cross_prod_pbc==0)):
            print("BORDER")
        elif((cross_prod_pab<0) and (cross_prod_pbc<0)):
            print("BORDER")
        else:
            print("OUTSIDE")
            
    if(not(border)):
        if((cross_prod_pab>0) and (cross_prod_pbc>0) and (cross_prod_pca>0)):
            print("INSIDE")
        elif((cross_prod_pab<0) and (cross_prod_pbc<0) and (cross_prod_pca<0)):
            print("INSIDE")
        else:
            print("OUTSIDE")
      
    border=False