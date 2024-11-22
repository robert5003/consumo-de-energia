from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Base de consejos para distintos electrodomésticos
energy_saving_tips = {
    "refrigerador": [
        "Mantén el refrigerador lejos de fuentes de calor como hornos o ventanas soleadas.",
        "Asegúrate de que las puertas del refrigerador estén bien selladas.",
        "No introduzcas alimentos calientes en el refrigerador, deja que enfríen primero."
    ],
    "aire acondicionado": [
        "Limpia o cambia los filtros regularmente.",
        "Mantén las puertas y ventanas cerradas mientras usas el aire acondicionado.",
        "Usa ventiladores para complementar el aire acondicionado y reducir su uso."
    ],
    "lavadora": [
        "Usa agua fría siempre que sea posible.",
        "Lava cargas completas en lugar de medias cargas para ahorrar energía.",
        "Limpia el filtro de la lavadora regularmente para mantenerla eficiente."
    ],
    "televisor": [
        "Apaga el televisor cuando no lo estés viendo.",
        "Usa configuraciones de brillo y contraste más bajas.",
        "Desenchufa el televisor si no lo usarás por un periodo prolongado."
    ],
    "computadora": [
        "Habilita el modo de suspensión o ahorro de energía.",
        "Apaga la computadora y el monitor cuando no estén en uso.",
        "Desconecta cargadores o periféricos innecesarios."
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        device_name = request.form['device_name'].lower()
        wattage = float(request.form['wattage'])
        hours_per_day = float(request.form['hours_per_day'])
        days_per_month = int(request.form['days_per_month'])

        # Calcular el consumo mensual en kWh
        monthly_consumption = (wattage * hours_per_day * days_per_month) / 1000

        tips = energy_saving_tips.get(device_name, ["Apaga los dispositivos cuando no estén en uso para ahorrar energía."])
        tip = random.choice(tips)

        return render_template(
            'result.html',
            device_name=device_name.capitalize(),
            monthly_consumption=monthly_consumption,
            tip=tip
        )
    except ValueError:
        return render_template('index.html', error="Por favor, ingresa valores válidos.")

if __name__ == '__main__':
    app.run(debug=True)
