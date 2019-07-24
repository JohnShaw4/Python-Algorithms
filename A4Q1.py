# John Shaw - jsha509 - 870608863
# Compsci220 - Assignment 4 - Question 1

while True:
    try:
        line1 = input()
        line2 = input()
    except EOFError:
        break
    class Node():
       def __init__(self, data):
           self.data = data
           self.childrenValues = []
       def Child(self, n):
           self.childrenValues.append(n)
       def Leaf(self):
           return len(self.childrenValues)==0
       def Val(self):
           if(self.Leaf()):
               return self.data
           elif(self.data=='+'):
               t = 0
               for child in self.childrenValues:
                   t += child.Val()
               return t
           elif(self.data=='*'):
               y = 1
               for child in self.childrenValues:
                   y *= child.Val()
               return y
    def IsInt(c):
       try:
           i = int(c)
           return i
       except:
           return c
    all = []
    all.append(line1)
    all.append(line2)
    for i in range(len(all)//2):
       predecessor = [int(x) for x in all[2*i].split(',')]
       nodevalue = [IsInt(x) for x in all[2*i+1].split(',')]
       node = [Node(nodevalue[i]) for i in range(len(nodevalue))]
       root = None
       for i in range(len(predecessor)):
           if(predecessor[i]==-1): root=node[i]; continue
           pred = node[predecessor[i]]
           pred.Child(node[i])
       print(root.Val())
