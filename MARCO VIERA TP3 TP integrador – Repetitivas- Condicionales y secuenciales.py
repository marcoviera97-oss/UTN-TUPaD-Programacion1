#actividad 1

# 1. Validación del nombre 
nombre = input("Ingrese el nombre del cliente: ")
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Ingrese el nombre del cliente: ")
# 2. Validación de cantidad 
cant_input = input("Cantidad de productos a comprar: ")
while not cant_input.isdigit() or int(cant_input) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cant_input = input("Cantidad de productos a comprar: ")
cantidad = int(cant_input)
# Acumuladores
total_sin_desc = 0
total_con_desc = 0
# 3. Ciclo de productos
for i in range(1, cantidad + 1):
    # Validar precio
    p_input = input(f"Producto {i} - Precio: ")
    while not p_input.isdigit():
        print("Error: Ingrese un precio válido (solo números).")
        p_input = input(f"Producto {i} - Precio: ")
    precio = int(p_input)
    total_sin_desc += precio
    # Validar descuento S/N
    tiene_desc = input(f"Producto {i} - ¿Tiene descuento? (S/N): ").lower()
    while tiene_desc not in ['s', 'n'] or tiene_desc == "":
        print("Error: Ingrese 'S' para sí o 'N' para no.")
        tiene_desc = input(f"Producto {i} - ¿Tiene descuento? (S/N): ").lower()
    # Lógica de descuento
    if tiene_desc == 's':
        precio_final = precio * 0.90
    else:
        precio_final = precio
    total_con_desc += precio_final
# 4. Cálculos finales
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cantidad
# Salida de resultados
print(f"\n--- Resumen de Compra ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#actividad 2

# 1. Credenciales iniciales
user_db = "alumno"
pass_db = "python123"
intentos = 0
acceso = False
# 2. Lógica de Login 
while intentos < 3:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    user_input = input("Usuario: ")
    pass_input = input("Clave: ")
    if user_input == user_db and pass_input == pass_db:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
# 3. Verificación de bloqueo
if not acceso:
    print("\nCuenta bloqueada.")
else:
    # 4. Menú repetitivo
    while True:
        print("\n--- MENÚ DEL CAMPUS ---")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")
        opcion = input("Opción: ")
        # 5. Validación de menú
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        opcion = int(opcion)
        if not (1 <= opcion <= 4):
            print("Error: opción fuera de rango.")
            continue
        # Lógica del menú
        if opcion == 1:
            print("Estado: Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave (mín. 6 caracteres): ")
            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirme su nueva clave: ")
                if nueva_clave == confirmacion:
                    pass_db = nueva_clave
                    print("Clave actualizada con éxito.")
                else:
                    print("Error: las claves no coinciden.")
        elif opcion == 3:
            print("Frase del día: 'Import antigravity' y a volar. ¡Seguí programando!")
        elif opcion == 4:
            print("Cerrando sesión...")
            break


#actividad 3

# 1. Variables de estado (Simulando la base de datos)
lunes1 = "" ; lunes2 = "" ; lunes3 = "" ; lunes4 = ""
martes1 = "" ; martes2 = "" ; martes3 = ""
# Validación del Operador
operador = input("Nombre del operador: ")
while not operador.isalpha():
    operador = input("Error. Ingrese nombre (solo letras): ")

while True:
    print(f"\n--- SISTEMA DE TURNOS (Operador: {operador}) ---")
    print("1. Reservar  2. Cancelar  3. Ver Agenda  4. Resumen  5. Salir")
    op = input("Opción: ")

    if op == "1":
        dia = input("Día (1=Lunes, 2=Martes): ")
        if dia == "1" or dia == "2":
            paciente = input("Nombre del paciente: ")
            while not paciente.isalpha():
                paciente = input("Error. Nombre solo letras: ")

            if dia == "1":
                # Validar si ya existe en Lunes
                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene turno el Lunes.")
                # Buscar primer espacio libre
                elif lunes1 == "": lunes1 = paciente ; print("Turno 1 Lunes reservado.")
                elif lunes2 == "": lunes2 = paciente ; print("Turno 2 Lunes reservado.")
                elif lunes3 == "": lunes3 = paciente ; print("Turno 3 Lunes reservado.")
                elif lunes4 == "": lunes4 = paciente ; print("Turno 4 Lunes reservado.")
                else: print("Sin cupos para el Lunes.")
            else:
                # Validar si ya existe en Martes
                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print("Error: El paciente ya tiene turno el Martes.")
                elif martes1 == "": martes1 = paciente ; print("Turno 1 Martes reservado.")
                elif martes2 == "": martes2 = paciente ; print("Turno 2 Martes reservado.")
                elif martes3 == "": martes3 = paciente ; print("Turno 3 Martes reservado.")
                else: print("Sin cupos para el Martes.")

    elif op == "2":
        dia = input("Día para cancelar (1/2): ")
        paciente = input("Nombre a cancelar: ")
        if dia == "1":
            if lunes1 == paciente: lunes1 = "" ; print("Cancelado.")
            elif lunes2 == paciente: lunes2 = "" ; print("Cancelado.")
            elif lunes3 == paciente: lunes3 = "" ; print("Cancelado.")
            elif lunes4 == paciente: lunes4 = "" ; print("Cancelado.")
            else: print("Paciente no encontrado.")
        elif dia == "2":
            if martes1 == paciente: martes1 = "" ; print("Cancelado.")
            elif martes2 == paciente: martes2 = "" ; print("Cancelado.")
            elif martes3 == paciente: martes3 = "" ; print("Cancelado.")
            else: print("Paciente no encontrado.")
    elif op == "3":
        dia = input("Ver agenda (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Lunes: 1:[{lunes1 or 'libre'}] 2:[{lunes2 or 'libre'}] 3:[{lunes3 or 'libre'}] 4:[{lunes4 or 'libre'}]")
        elif dia == "2":
            print(f"Martes: 1:[{martes1 or 'libre'}] 2:[{martes2 or 'libre'}] 3:[{martes3 or 'libre'}]")
    elif op == "4":
        # Conteo manual
        ocu_l = (1 if lunes1 else 0) + (1 if lunes2 else 0) + (1 if lunes3 else 0) + (1 if lunes4 else 0)
        ocu_m = (1 if martes1 else 0) + (1 if martes2 else 0) + (1 if martes3 else 0)
        print(f"Lunes: {ocu_l} ocupados, {4 - ocu_l} libres.")
        print(f"Martes: {ocu_m} ocupados, {3 - ocu_m} libres.")
        if ocu_l > ocu_m: print("Día con más turnos: Lunes")
        elif ocu_m > ocu_l: print("Día con más turnos: Martes")
        else: print("Empate en cantidad de turnos.")
    elif op == "5":
        break

#actividad 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0  # Contador para regla anti-spam
# Validación del Agente
agente = input("Nombre del Agente: ")
while not agente.isalpha():
    agente = input("Error. Ingrese un nombre válido (letras): ")
print(f"\n¡Bienvenido Agente {agente}! La bóveda te espera.")
# 2. Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 ---")
    print(f"Alarma: {'ON' if alarma else 'OFF'} | Código: [{codigo_parcial}]")
    print("1. Forzar cerradura (-20E, -2T)")
    print("2. Hackear panel (-10E, -3T)")
    print("3. Descansar (+15E, -1T)")
    op = input("Acción: ")
    while not op.isdigit() or op not in ["1", "2", "3"]:
        op = input("Opción inválida. Elija 1, 2 o 3: ")
    # Lógica de acciones
    if op == "1":
        # Costo base
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        # Regla Anti-Spam
        if forzar_seguidos >= 3:
            alarma = True
            print("¡La cerradura se trabó por forzar demasiado! ALARMA ACTIVADA.")
        else:
            # Riesgo de alarma por baja energía
            if energia < 40:
                print("RIESGO DE ALARMA (Baja energía)")
                num = input("Elegí un número (1-3): ")
                while not num.isdigit() or num not in ["1", "2", "3"]:
                    num = input("Error. Elegí 1, 2 o 3: ")
                if num == "3":
                    alarma = True
                    print("¡Movimiento torpe! La alarma está sonando.")
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")
    elif op == "2":
        forzar_seguidos = 0 # Corta la racha
        energia -= 10
        tiempo -= 3
        print("Hackeando...")
        for i in range(1, 5):
            print(f"Progreso: {i*25}%")
            codigo_parcial += "A"
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡El código descifrado abrió una cerradura!")
    elif op == "3":
        forzar_seguidos = 0 # Corta la racha
        tiempo -= 1
        recuperacion = 15
        if alarma:
            recuperacion -= 10
            print("Descanso difícil por el ruido de la alarma...")
        energia += recuperacion
        if energia > 100: energia = 100
        print(f"Energía recuperada. Total: {energia}")
# 3. Condiciones de Fin de Juego
print("\n--- RESULTADO FINAL ---")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El Agente {agente} abrió la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó por la alarma. ¡Atrapado!")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energía.")
elif tiempo <= 0:
    print("DERROTA: Se acabó el tiempo.")


#actividad 5

# Paso 1: Configuración del Personaje
nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha() or nombre == "":
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")
# Paso 2: Inicialización de Estadísticas
vida_jugador = 100         
vida_enemigo = 100         
pociones = 3               
ataque_pesado_base = 15    
daño_enemigo_base = 12     
juego_activo = True        
print("\n=== INICIO DEL COMBATE ===")
# Paso 3: El Ciclo de Combate
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    opcion = input("Opción: ")
    # Validación del Menú
    while not opcion.isdigit() or opcion not in ["1", "2", "3"]:
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ")
    # Lógica de las Acciones del Jugador
    if opcion == "1":
        daño_final = float(ataque_pesado_base)
        # Lógica de Golpe Crítico
        if vida_enemigo < 20:
            daño_final = ataque_pesado_base * 1.5
            print("¡GOLPE CRÍTICO!")
        vida_enemigo -= int(daño_final)
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
    elif opcion == "2":
        print(">> ¡Inicias una ráfaga de golpes!")
        for i in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
    elif opcion == "3":
        if pociones > 0:
            vida_jugador += 30
            if vida_jugador > 100: vida_jugador = 100 
            pociones -= 1
            print(f"¡Te curaste! Vida actual: {vida_jugador}")
        else:
            print("¡No quedan pociones!")
    # Turno del Enemigo (solo si sigue vivo)
    if vida_enemigo > 0:
        vida_jugador -= daño_enemigo_base
        print(f">> ¡El enemigo te atacó por {daño_enemigo_base} puntos de daño!")
# Paso 4: Fin del Juego
print("\n=== RESULTADO FINAL ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")




