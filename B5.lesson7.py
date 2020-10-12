#Bài 7:Tính tổng các số nguyên tố trong mảng
def input_list(n):
    result = []
    for i in range(n):
        x = int(input(f"Enter item[{i}]: "))
        result.append(x)
    return result
def KT_SNT(k,a):
    count = 0
    for i in range(2,len(a)):
        if k%i==0:
            count+=1
    if count==1:
        return True
    return False
