def cube_num(n):
    return n**3

num = int(input("Enter number to be cubed: "))
print(cube_num(num))

for i in range(10):
    print(f"Cube of {i} is {cube_num(i)}")
    
