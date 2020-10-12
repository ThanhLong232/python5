#Bài 1:Tính tổng của mảng 1 chiều
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result

def tinhTong(a):
    b = 0
    for v in a:
        b+=v
    return b
n = int(input("Nhập số lượng phân tử:"))
a = input_list(n)
#c = tinhTong(a)
print(a)
print(tinhTong(a))



