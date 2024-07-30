

ls = []
with open("base.txt" ,"r") as f:
   for i in f.read().split("\n"):
       ls.append(i.split(","))



