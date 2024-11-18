from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home(): return render_template('index.html')


precio_tarro = 9000


# Ejercicio 1
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    # Inicializar valores
    nombre1 = request.form.get('nombre1', '')
    edad1 = request.form.get('edad1', '')
    tarro_pintura = request.form.get('tarro_pintura', '')

    if request.method == 'POST':
        # Campos del formulario
        nombre1 = (request.form['nombre1'])
        edad1 = int(request.form['edad1'])
        tarro_pintura = int(request.form['tarro_pintura'])

        # Calcular el total sin descuento
        total_sin_descuento = tarro_pintura * precio_tarro

        # Aplicar descuento según la edad
        if 18 <= edad1 <= 30:
            descuento = 0.15  # 15% de descuento
        elif edad1 > 30:
            descuento = 0.25  # 25% de descuento
        else:
            descuento = 0  # No hay descuento
        # Calcular descuento en pesos
        monto_descuento = total_sin_descuento * descuento
        # Calcular el total con descuento
        total_con_descuento = total_sin_descuento * (1 - descuento)

        # Mostrar los resultados
        if descuento > 0:
            resultado = f"Nombre del cliente: {nombre1}<br><br>"\
                        f"Total sin descuento: ${round(total_sin_descuento)}<br><br>"\
                        f"El descuento es: ${round(monto_descuento)}<br><br>"\
                        f"El total a pagar es de: {round(total_con_descuento)}<br><br>"
        else:
            resultado = f"Nombre del cliente: {nombre1}<br><br>"\
                        f"Total sin descuento: ${round(total_sin_descuento)}<br><br>"\
                        f"El descuento es: ${round(monto_descuento)}<br><br>"\
                        f"El total a pagar es de: ${round(total_sin_descuento)}<br><br>"

    return render_template('ejercicio1.html',
                           resultado=resultado, nombre1=nombre1, edad1=edad1, tarro_pintura=tarro_pintura)


# Diccionario para usuarios y contraseñas
usuarios = {
    "juan": "admin",
    "pepe": "user"
}


# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = ""
    usuario_ingresado = "" 
    contrasena_ingresada = ""
    if request.method == 'POST':
        # Campos del formulario
        usuario_ingresado = (request.form['usuario'])
        contrasena_ingresada = (request.form['contrasena'])

        if usuario_ingresado in usuarios and usuarios[usuario_ingresado] == contrasena_ingresada:
            if usuario_ingresado == "juan":
                mensaje = f"Bienvenido administrador {usuario_ingresado}"
            elif usuario_ingresado == "pepe":
                mensaje = f"Bienvenido usuario {usuario_ingresado}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje,
                           usuario=usuario_ingresado, contrasena=contrasena_ingresada)


if __name__ == '__main__':
    app.run(debug=True)
