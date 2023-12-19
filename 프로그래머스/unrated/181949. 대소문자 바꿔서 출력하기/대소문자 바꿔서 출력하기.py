str = input()
print_string = ''
for s in str:
    if s.isupper():
        s = s.lower()
    else:
        s = s.upper()
    print_string += s
print(print_string)