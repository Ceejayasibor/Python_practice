def capitalize_all(t):
    capitals = []
    for i in t:
        if isinstance(i, list):
            capitals.append(capitalize_all(i))
        else:
            capitals.append(i.capitalize())
    return capitals
t= ['boy', 'girl', 'man', ['goat', 'monkey']]
print(capitalize_all(t))


a= ['a', 'b', 'c', 'defghij', 'klmn', 'o']
b= ['eggs', ['apple', 'bat'], 'car']
c= ['house', ['car']]

if __name__ == '__main__':
    print(capitalize_all(a))
    print(capitalize_all(b))
    print(capitalize_all(c))
    
    
