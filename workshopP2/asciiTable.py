value = 'Value'
character = 'Char'
print("{:^8s} {:^8s}" .format(value, character))
for i in range (0, 256):
    print("{:^8d} {:^8s}" .format(i, chr(i)))