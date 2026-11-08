def get_product(**datos):
    print(datos["id"], datos["name"])

get_product(id="85",
            name="Samsung",
            desc="Galaxy S26 Ultra")

# ** sirve para pasar un número variable de argumentos con nombre a una función