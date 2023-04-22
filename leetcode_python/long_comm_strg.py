a=["flower","flow","flight"]
b=""
#if len(a)==0:
  #  break
current=a[0]
for i in range(1,len(a)):
    if len(current)==0:
        break
    for j in range(1,len(a[i])):
        if j<len(current) and current[j] == a[i][j]:
            b +=current[j]
        else:
            break

        current =b

print(current)
