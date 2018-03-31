file = open('shop.txt','r',encoding='utf-8')

leastProduct = 99999
leastLine = []

for line in file:
    listValues = line.split(',')
    if int(listValues[4]) < int(leastProduct):
        leastProduct = int(listValues[4])
        leastLine = listValues
        
    
print(leastLine)
