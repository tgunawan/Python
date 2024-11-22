# display list
list2D=[
    [1,2,3,4],
    [4,5,6],
    [7,8,9]]

row=3
column=3
fastList=[['O']*column for _ in range(row)]

print(len(list2D[0]))
print(len(fastList))
print('----------')
for i in range(len(list2D)):
    for j in range(len(list2D[i])):
        print(list2D[i][j],end=' ')
    print('')

print('----------')
#------------------- elemen
print(list2D[1][2])
list2D[1][2]=20
print(list2D[1][2])
print('----------')

# list2D.pop(1)
list2D[1].remove(5)
# list2D.remove([4,5,6])
print(list2D)
print('----------')
list2D.append([10,11,12])
