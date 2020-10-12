#Bài 6: Tìm các số chan trong mảng
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result

def SoChan(a):
    
    for b in a:
        if b%2==0:
            print(b)
    

n = int(input("Nhập số phần tử: "))
a = input_list(n)
print(a)
print(SoChan(a))