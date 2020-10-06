kata=("where is waldo ? I think waldo is hiding behind the wall, we have to find waldo before the game is ended")
listkata=kata.split()
print(listkata)
index=[]
for i in range(len(listkata)):
    if listkata[i]=="waldo":
        index.append(i)
print(listkata)
print("ada", len(index),"kata waldo ditemukan pada index ke:", index)
