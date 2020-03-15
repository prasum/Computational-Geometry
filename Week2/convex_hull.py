#Python3
class Comp(object):
    def __init__(self, tup):
        self.tup = tup

    def __lt__(self, other):  # sorted works even if only __lt__ is implemented.
        # If the difference is less or equal the offset of the second item compare the third
        if (self.tup[0]==other.tup[0]):
            return self.tup[1] < other.tup[1]
        # otherwise compare them as usual
        else:
            return self.tup[0]<other.tup[0]

def first_three(a):
    if(len(a)>2):
        ax=a[-3][0]
        ay=a[-3][1]
        px=a[-2][0]
        py=a[-2][1]
        bx=a[-1][0]
        by=a[-1][1]
        cross_prod=(px-ax)*(by-py)-(py-ay)*(bx-px)
        if(cross_prod<=0):
            return True
        else:
            return False
    else:
        return False
    
def last_three(a):
    if(len(a)>2):
        ax=a[-3][0]
        ay=a[-3][1]
        px=a[-2][0]
        py=a[-2][1]
        bx=a[-1][0]
        by=a[-1][1]
        cross_prod=(px-ax)*(by-py)-(py-ay)*(bx-px)
        if(cross_prod>=0):
            return True
        else:
            return False
    else:
        return False
n=input()
n=int(n)
vertices=[]
upper=[]
edges=[]
count=0
merge_str=""
poly_points=input().split()
for k in range(0,2*n-1,2):
    vertices.append((int(poly_points[k]),int(poly_points[k+1])))

vertices=sorted(vertices,key=Comp)
#print(vertices)
p1=vertices[0]
p2=vertices[1]
upper.append(p1)
upper.append(p2)
for i in range(2,len(vertices)):
    upper.append(vertices[i])
    while(len(upper)>2 and last_three(upper)):
        del upper[-2]
        
#print(upper)
#diff_vertices=list(set(vertices)-set(upper))
#print(diff_vertices)
#diff_vertices=sorted(diff_vertices,key=Comp)
lower=[]
p1=vertices[0]
p2=vertices[1]
lower.append(p1)
lower.append(p2)
for i in range(2,len(vertices)):
    lower.append(vertices[i])
    while(len(lower)>2 and first_three(lower)):
        del lower[-2]

#print(lower)
merge_list=[]
for i in range(len(lower)):
    if(lower[i] not in upper):
        merge_list.append(lower[i])
for i in range(len(upper)-1,-1,-1):
    merge_list.append(upper[i])
    
print(len(merge_list))
for i in range(len(merge_list)):
    merge_str+=str(merge_list[i][0])
    merge_str+=" "
    merge_str+=str(merge_list[i][1])
    if(i!=len(merge_list)-1):
        merge_str+=" "
#print(merge_list)
print(merge_str)
'''for i in range(len(vertices)):
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

'''