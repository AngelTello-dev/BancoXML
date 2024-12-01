from flask import Flask, render_template, request
import xml.etree.ElementTree as ET
from datetime import datetime

app = Flask(__name__)

# Cargar cuentas desde el XML
def cargar_cuentas():
    tree = ET.parse('cuentas.xml')
    root = tree.getroot()
    cuentas = []
    for cuenta in root.findall('cuenta'):
        tarjeta = cuenta.find('tarjeta').text
        fecha = cuenta.find('fecha').text
        nip = cuenta.find('nip').text
        intentos = int(cuenta.find('intentos').text)
        balance = float(cuenta.find('balance').text)
        limite = float(cuenta.find('limite').text)
        cuentas.append({
            'tarjeta': tarjeta,
            'fecha': fecha,
            'nip': nip,
            'intentos': intentos,
            'balance': balance,
            'limite': limite
        })
    return cuentas

# Guardar cuentas en el XML
def actualizar_xml(cuentas):
    root = ET.Element('cuentas')
    for cuenta in cuentas:
        cuenta_element = ET.SubElement(root, 'cuenta')
        ET.SubElement(cuenta_element, 'tarjeta').text = cuenta['tarjeta']
        ET.SubElement(cuenta_element, 'fecha').text = cuenta['fecha']
        ET.SubElement(cuenta_element, 'nip').text = cuenta['nip']
        ET.SubElement(cuenta_element, 'intentos').text = str(cuenta['intentos'])
        ET.SubElement(cuenta_element, 'balance').text = str(cuenta['balance'])
        ET.SubElement(cuenta_element, 'limite').text = str(cuenta['limite'])

    tree = ET.ElementTree(root)
    tree.write('cuentas.xml')

# Verificar si la tarjeta está registrada
def verificar_tarjeta(cuentas, tarjeta):
    for cuenta in cuentas:
        if cuenta['tarjeta'] == tarjeta:
            return cuenta
    return None

# Verificar si la tarjeta está vigente
def verificar_vigencia(cuenta):
    fecha_expiracion = datetime.strptime(cuenta['fecha'], '%Y-%m-%d')
    return fecha_expiracion >= datetime.now()

# Verificar NIP
def verificar_nip(cuenta, nip_ingresado):
    return cuenta['nip'] == nip_ingresado

# Realizar el retiro
def realizar_retiro(cuenta, monto):
    if cuenta['balance'] >= monto and monto <= cuenta['limite']:
        cuenta['balance'] -= monto
        return True
    return False

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def index():
    mensaje = None
    cuenta_info = None
    if request.method == 'POST':
        tarjeta = request.form.get('tarjeta')
        cuentas = cargar_cuentas()
        cuenta = verificar_tarjeta(cuentas, tarjeta)
        if cuenta:
            vigente = verificar_vigencia(cuenta)
            mensaje = "Tarjeta vigente." if vigente else "Tarjeta expirada."
            cuenta_info = cuenta
        else:
            mensaje = "Tarjeta no encontrada."
    return render_template('index.html', mensaje=mensaje, cuenta=cuenta_info)

# Ruta para verificar NIP y realizar retiros
@app.route('/operacion', methods=['GET', 'POST'])
def operacion():
    mensaje = None
    if request.method == 'POST':
        tarjeta = request.form.get('tarjeta')
        nip = request.form.get('nip')
        monto = float(request.form.get('monto', 0))
        cuentas = cargar_cuentas()
        cuenta = verificar_tarjeta(cuentas, tarjeta)
        if cuenta:
            if not verificar_vigencia(cuenta):
                mensaje = "La tarjeta está expirada."
            elif verificar_nip(cuenta, nip):
                if realizar_retiro(cuenta, monto):
                    mensaje = f"Retiro de {monto} autorizado. Nuevo balance: {cuenta['balance']}"
                    actualizar_xml(cuentas)
                else:
                    mensaje = "Saldo insuficiente o monto excede el límite."
            else:
                mensaje = "NIP incorrecto."
        else:
            mensaje = "Tarjeta no encontrada."
    return render_template('operacion.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
