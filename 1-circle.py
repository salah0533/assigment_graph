edj_list=list()
vertices,edjes=input().split()
vertices=int(vertices)
edjes=int(edjes)
for i in range(edjes):
  m,n=input().split()
  m=int(m)
  n=int(n)
  edj_list.append([m,n])
star,end=input().split()
star=int(star)
end=int(end)  

adj_list={}
visit={}
cycle_list=list()
b=0
for i in range(vertices):
  adj_list[i+1]=[]
#conversion diagram to adjacent list  
for e in edj_list:
  adj_list[e[0]].append(e[1])

def dfs(u):
    global b
    visit[u]='t'
    if u in cycle_list:
        b=1
        return
    else:
        cycle_list.append(u)
    for e in adj_list[u]:
            dfs(e)
    cycle_list=list()        

for i in adj_list.keys():
    if b==0:
        if visit[i]=='f':
            dfs(i)
        else :break    
        
print(b)
      
