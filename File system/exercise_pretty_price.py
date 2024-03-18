def pretty_price(precio_bruto, extension):
    if isinstance(extension, int):
        extension = extension * 0.01
    
    return int(precio_bruto) + extension

print(pretty_price(3.99,23))
print(pretty_price(5,0.88))
    
