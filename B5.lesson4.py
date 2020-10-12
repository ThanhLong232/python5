# Bài 4: Tìm giá trị nhỏ nhất
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result

def NhoNhat(a):
    min = a[0]
    for b in a:
        if min>b:
            min = b
    return min

n = int(input("Nhập số phần tử: "))
a = input_list(n)
print(a)
print(NhoNhat(a))