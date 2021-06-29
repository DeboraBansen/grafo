class Graph():

  def __init__ (self,nvertices):
    self.N=nvertices
    self.graph=[[0 for column in range(nvertices)] for row in range(nvertices)]
    self.V=['0' for collumn in range(nvertices)]

  def nameVertex(self):
    for i in range(self.N):
      print("Qual o rotulo de vertice %i?"%(i))
      self.V[i]=input()


  def setEdge(self,u,v,w):
    self.graph[u][v]=w

  def loadEdges(self):
    for i in range(self.N):
      for j in range(self.N):
        if i!=j:
          print("Qual o peso entre %c e %c"%(self.V[i],self.V[j]))
          self.setEdge(i,j,input())
  
  def verificaAdjacencia(self):
    print("Qual vertices deseja saber a adjacencia?")
    n=input()
    m=input()
    for i in range(self.N):
      for j in range(self.N):
        if i!=j and self.graph[i][j]!=0:
          if self.V[i]==n and self.V[j]==m:
            print("os vertices %c e %c sao adjacentes com distancia= %c"%(self.V[i],self.V[j],self.graph[i][j]))

  def grauVertex(self):
    cont=0
    print("Qual o vertice que deseja saber o grau?")
    n=input()
    for i in range(self.N):
      for j in range(self.N):
        if i!=j and self.V[i]==n:
          if self.graph[i][j]!=0:
            cont=cont+1
    print("O grau do vertice %c = %i"%(n,cont))      
  
  def retornarArestas(self):
    cont=0
    for i in range(self.N):
      for j in range(self.N):
        if i!=j:#pra nao contar arestas repetidas seria melhor i>j
          if self.graph[i][j]!='0':
            cont=cont+1
    print("O grafo tem %i arestas"%(cont))      
  
  def verificaGrafoCompleto(self):
    cont=0
    for i in range(self.N):
      for j in range(self.N):
        if i!=j:
          if self.graph[i][j]=='0':
            cont=cont+1
    if cont==0:
      print("O grafo é completo")
    else:
      print("O grafo não é completo")  
     
  

print('Qual o numero de vertices?')    
n=int(input())
g=Graph(n)
g.nameVertex()
g.loadEdges()
#g.grauVertex()
#g.verificaAdjacencia()
#g.retornarArestas()
#g.verificaGrafoCompleto()
print(g.graph)
