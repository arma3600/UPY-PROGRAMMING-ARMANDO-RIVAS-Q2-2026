# INPUT
check = True
while check:
    try:
        verbo = input("Ingrese un verbo en infinitivo (ej. hablar, comer, vivir): ")
        
        if verbo != verbo.strip():
            raise ValueError("El verbo no debe tener espacios extra")
            
        if verbo != verbo.lower():
            raise ValueError("El verbo debe escribirse en minúsculas")
            
        if not verbo or not verbo.isalpha():
            raise ValueError("El verbo debe terminar en ar, er o ir")
            
        if len(verbo) < 3:
            raise KeyError("El verbo debe terminar en ar, er o ir")
            
        ending = verbo[-2:]
        valid_endings = ['ar', 'er', 'ir']
        
        if ending not in valid_endings:
            raise KeyError("El verbo debe terminar en ar, er o ir")
            
        check = False
        
    except (ValueError, KeyError) as e:
        if "escribirse en minúsculas" in str(e) or "espacios extra" in str(e):
            print(e)
        else:
            print("El verbo debe terminar en ar, er o ir")

# PROCESS
pronombres = ['Yo', 'Tú', 'Él', 'Nosotros', 'Vosotros', 'Ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

stem = verbo[:-2]
endings_list = terminaciones[ending]

# OUTPUT
for index, pronombre in enumerate(pronombres):
    terminacion = endings_list[index]
    print(f"{pronombre} {stem}{terminacion}")