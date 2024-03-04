camel_style = input("Верблюжий стиль: ")
snake_style = ""

for c in camel_style:
    if c.isupper():
        snake_style += "_" + c.lower()
    else:
        snake_style += c

print( snake_style)
