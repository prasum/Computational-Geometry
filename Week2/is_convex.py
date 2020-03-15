#Python3
n=input()
n=int(n)
vertices=[]
edges=[]
count=0
poly_points=input().split()
for k in range(0,2*n-1,2):
    vertices.append((int(poly_points[k]),int(poly_points[k+1])))

for i in range(len(vertices)):
    if(i==len(vertices)-1):
        px=vertices[0][0]
        py=vertices[0][1]
        ax=vertices[i][0]
        ay=vertices[i][1]
        bx=vertices[1][0]
        by=vertices[1][1]
        cross_prod=(px-ax)*(py-by)-(py-ay)*(px-bx)
        if(cross_prod<0):
            count=count+1
            
    elif(i==len(vertices)-2):
        px=vertices[i+1][0]
        py=vertices[i+1][1]
        ax=vertices[i][0]
        ay=vertices[i][1]
        bx=vertices[0][0]
        by=vertices[0][1]
        cross_prod=(px-ax)*(py-by)-(py-ay)*(px-bx)
        if(cross_prod<0):
            count=count+1
            
    else:
        px=vertices[i+1][0]
        py=vertices[i+1][1]
        ax=vertices[i][0]
        ay=vertices[i][1]
        bx=vertices[i+2][0]
        by=vertices[i+2][1]
        cross_prod=(px-ax)*(py-by)-(py-ay)*(px-bx)
        if(cross_prod<0):
            count=count+1
            
if(count==n):
    print("CONVEX")
else:
    print("NOT_CONVEX")