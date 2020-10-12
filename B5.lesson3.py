# bài 3: Tìm giá trị lớn nhất
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result

def LonNhat(a):
    max = a[0]
    for b in a:
        if max<b:
            max = b
    return max

n = int(input("Nhập số phần tử: "))
a = input_list(n)
print(a)
print(LonNhat(a))