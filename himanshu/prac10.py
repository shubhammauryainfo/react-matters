class FileSystem(object):
   def __init__(self):
      self.d = {}
   def create(self, p, v):
      p = p.split("/")
      x = self.d
      for i in range(1,len(p)-1):
         if p[i] not in x:
            return False
         x = x[p[i]][1]
      if p[-1] in x:
         return False
      x[p[-1]] = [v,{}]
      return True
   def get(self, p):
      x = self.d
      p = p.split("/")
      for i in range(1,len(p)-1):
         if p[i] not in x:
            return -1
         x= x[p[i]][1]
      if p[-1] in x:
         return x[p[-1]][0]
      else:
         return -1
ob = FileSystem()
print(ob.create("/a", 1))
print(ob.get("/a"))
