# Proyecto de Verificación y Gestión de Cuentas

Este proyecto permite la verificación de tarjetas bancarias y la gestión de cuentas de usuarios mediante un sistema de autenticación por NIP y operaciones de retiro.

## Descripción

El sistema tiene la capacidad de almacenar varias cuentas, cada una asociada con una tarjeta, fecha de expiración, NIP, intentos fallidos, balance actual y límite de crédito. Los usuarios pueden verificar sus tarjetas, acceder a los detalles de su cuenta y realizar operaciones de retiro.

## Tecnologías utilizadas

- **HTML**: Para la interfaz de usuario.
- **CSS**: Para la presentación visual de las páginas.
- **XML**: Para almacenar y organizar los datos de las cuentas de manera estructurada.
- **Python/Flask** (si es que se usa un backend): Para manejar las peticiones del usuario y realizar las operaciones de verificación.

## Instalación

Para ejecutar este proyecto, sigue los pasos a continuación:

1. **Requisitos previos**:
   - Tener instalado **Python 3.x** en tu sistema.
   - Tener instalada la librería **Flask**. Si no la tienes, puedes instalarla ejecutando:
     ```bash
     pip install Flask
     ```

2. **Ejecutar el servidor**:
   - Entra en la carpeta del proyecto y ejecuta el siguiente comando:
     ```bash
     python app.py
     ```
   - Esto iniciará el servidor en `http://localhost:5000`.

3. **Acceder al proyecto**:
   - Abre tu navegador y ve a `http://localhost:5000` para interactuar con el sistema de verificación y gestión de cuentas.

## Uso

- **Verificar una tarjeta**:
   - En la página de inicio, ingresa el número de la tarjeta que deseas verificar. Si la tarjeta es válida, se mostrarán los detalles de la cuenta asociada.

- **Operaciones de retiro**:
   - Una vez que la tarjeta haya sido verificada, podrás ingresar el NIP y el monto que deseas retirar. El sistema validará si el monto es suficiente y si el NIP es correcto.

## Formato de datos XML

El sistema utiliza un archivo XML para almacenar las cuentas de los usuarios. A continuación se muestra un ejemplo del formato de los datos:

```xml
<cuentas>
    <cuenta>
        <tarjeta>1234567890</tarjeta>
        <fecha>2024-12-31</fecha>
        <nip>1234</nip>
        <intentos>0</intentos>
        <balance>2000.0</balance>
        <limite>1000.0</limite>
    </cuenta>
    <cuenta>
        <tarjeta>9876543210</tarjeta>
        <fecha>2023-12-31</fecha>
        <nip>4321</nip>
        <intentos>0</intentos>
        <balance>1000.0</balance>
        <limite>500.0</limite>
    </cuenta>
    <cuenta>
        <tarjeta>5555555555</tarjeta>
        <fecha>2024-12-31</fecha>
        <nip>5678</nip>
        <intentos>0</intentos>
        <balance>0.0</balance>
        <limite>300.0</limite>
    </cuenta>
    <cuenta>
        <tarjeta>1111111111</tarjeta>
        <fecha>2024-11-30</fecha>
        <nip>9999</nip>
        <intentos>0</intentos>
        <balance>5000.0</balance>
        <limite>1000.0</limite>
    </cuenta>
</cuentas>

```

## Desarollador

Ingeniero Tello Montes De Oca Angel Antonio

Matricula 19-003-0125

