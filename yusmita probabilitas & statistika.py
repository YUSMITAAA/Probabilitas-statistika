nim = [0,1,2,2,2,3,6]
n = len(nim)
jumlahData = 0
for i in nim :
    jumlahData += i

print("nim = 0,1,2,2,2,3,6")
print("hasil jumlah nim : ",jumlahData)
print("n : ",n)

#nilai mean
x = jumlahData / n
print("nilai mean : ", x)
print("--------------------------------")

#nilai median
if n %2 == 0:
    median = nim[int(rumusMedian)]
else :
    rumusMedian = (n+1)/2
    #GENAP
    pass
print("nim : ",nim)
print("nilai median : ",rumusMedian)
print("--------------------------------")

#nilai modus
nim = [0,1,2,2,2,3,6]
n = None
jumlahData = 0

for i in nim:
    count= nim.count(i)
    if count > jumlahData:
        n = i
        jumlahData = count
print("nim : ",nim)
print("nilai modus : ",n)
print("------------selesai-------------")


    
