with open("two_cities_ascii.txt", 'r') as inf:
    new = ''.join([chr(255-ord(ch)) for ch in inf.read()][::-1])
    print(new)
