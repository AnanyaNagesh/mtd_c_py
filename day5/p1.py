def my_func(lenght, breadth):
    lenght += 1
    return length*breadth
length = int(input("Enter length of th Rectangle: "))
breadth = int(input("Enter breadth of th Rectangle: "))
area = my_func(length, breadth)
print(f'Area of the rectangle = {area}') 