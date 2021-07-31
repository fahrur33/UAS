print("pilih metode pencarian: ")
print ("1. sequential search")
print("2. binary search")

i = input("masukkan pilihan anda dengan tekan 1/2: ")

if i=="1":
    
    def sequential(data,nilai):
        a = 0
        temp = False
        while a < len(data) :
            if data[a] == nilai:
                temp = True
                break
            else:
                a += 1
        
        if temp:
            print ("nilai", nilai,"ada")
        else:
            print ("nilai", nilai,"tidak ada")
            
    import json
    i=open ("data.json","r")
    f= json.loads(i.read())
    print(f)
    i.close()
    i = int(input("mencari dengan sequential search: "))
    sequential (f,i)

elif i == "2":
    def a(b,c):
        d = 0
        e = len(b)-1
        f = False
        while d <= e:
            g=(d+e)//2
            if (b[g]==c):
                f = True
                break
            else:
                if (c<b[g]):
                    e=g-1
                else:
                    d=g+1
        if f:
            print ("nilai",c,"ditemukan")
        else:
            print ("nilai", c,"tidak ada")
        
    import json
    i=open ("data.json","r")
    f= json.loads(i.read())
    print(f)
    f.sort()
    f
    i.close()
    i = int(input("mencari dengan binary search: "))
    a(f,i)

else:
    print("pilihan salah")


