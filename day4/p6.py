input_str = 'A@bcd1abx'
digits = []
for char in input_str:
    if char.isdigit():
       digits.append(char)
new_one = list(set(digits))
digits.sort(reverse = True)
digits_big = ''.join(digits)
biggest_num =  int(digits_big)
print(f'the resultant is {biggest_num}')