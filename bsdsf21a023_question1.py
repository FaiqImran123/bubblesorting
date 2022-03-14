array =[15,16,6,8]
a =0
i =0
n =4
while a<4:
    i =0
    while i<3:
        if array[i]>array[i+1]:
            t =array[i]
            array[i]=array[i+1]
            array[i+1]=t
            
        else:
            pass
        i =i+1    
    a =a+1
print(array)    