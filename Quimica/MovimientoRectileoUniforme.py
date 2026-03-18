def menu_principal():
    print("\n--- CALCULADORA DE FÍSICA ---")
    print("1. Movimiento Rectilíneo Uniforme (MRU)")
    print("2. Movimiento Rectilíneo Uniformemente Acelerado (MRUA)")
    print("3. Salir")
    return input("Selecciona una opción: ")

def ejecutar_mru():
    print("\n[ MRU: d = v * t ]")
    print("Si no conoces el valor solo (presiona Enter) escribe la variable que quieres calcular.")
    
    try:
        d = input("Distancia (m): ")
        v = input("Velocidad (m/s): ")
        t = input("Tiempo (s): ")

        if not d: # Calcular distancia
            res = float(v) * float(t)
            print(f">> La Distancia es: {res} m")
        elif not v: # Calcular velocidad
            res = float(d) / float(t)
            print(f">> La Velocidad es: {res} m/s")
        elif not t: # Calcular tiempo
            res = float(d) / float(v)
            print(f">> El Tiempo es: {res} s")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    except ZeroDivisionError:
        print("Error: El tiempo o la velocidad no pueden ser cero.")

def ejecutar_mrua():
    print("\n[ MRUA: vf = vi + a*t  |  d = vi*t + 0.5*a*t^2 ]")
    print("1. Calcular Velocidad Final (vf)")
    print("2. Calcular Distancia (d)")
    opcion = input("¿Qué deseas calcular?: ")

    try:
        vi = float(input("Velocidad inicial (m/s): "))
        a = float(input("Aceleración (m/s²): "))
        t = float(input("Tiempo (s): "))

        if opcion == "1":
            vf = vi + (a * t)
            print(f">> La Velocidad Final es: {vf} m/s")
        elif opcion == "2":
            d = (vi * t) + (0.5 * a * (t**2))
            print(f">> La Distancia recorrida es: {d} m")
    except ValueError:
        print("Error: Por favor ingresa datos numéricos.")

# Bucle principal
while True:
    opc = menu_principal()
    if opc == "1":
        ejecutar_mru()
    elif opc == "2":
        ejecutar_mrua()
    elif opc == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
