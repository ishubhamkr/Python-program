lst = []
  
n = int(input())  #input number of names
  
for i in range(0, n):
    ele = str(input())
    lst.append(ele)


lst=[nls.capitalize() for nls in lst ]
print(lst)