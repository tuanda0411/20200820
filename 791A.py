# khởi tạo 2 biến đọc giá trị truyền vào
# map de ep kieu du lieu la int
a, b = map(int, input().split())
i = 0
while a <= b: 
    a = a*3
    b = b*2
    i = i+1
print(i)
