#Bài 5:Tìm các số le trong mảng 
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result

def SoLe(a):
    
    for b in a:
        if b%2!=0:
            print(b)
    

n = int(input("Nhập số phần tử: "))
a = input_list(n)
print(a)
print(SoLe(a))