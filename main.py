import WhasappWeb as wpp
import qrcode
import distribuidor

def generarqr(cqr):
    # Texto o enlace que deseas codificar en el QR
    data = cqr

    # Crear un objeto QRCode
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    # Agregar los datos al código QR
    qr.add_data(data)
    qr.make(fit=True)

    # Crear una imagen QR
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar la imagen QR
    img.save("codigo_qr.png")

def verificarconexion(cliente):
    if cliente == 'cliente conectado':
        print(cliente)

def escribir_en_consola(mensaje):
    wpp.proceso.stdin.write((mensaje + '\n').encode())
    wpp.proceso.stdin.flush()  # Asegurarse de que los datos se envíen inmediatamente

def procesarmensaje(mensaje):
    if mensaje == 'quiero ser bot':
        escritolibre = distribuidor.respuestas()
        if escritolibre:
            escribir_en_consola('./Serbot')
        print(mensaje)
    elif mensaje == './Serbot':
        escritolibre = distribuidor.respuestas()
        if escritolibre:
            escribir_en_consola('./Serbot')
        print(mensaje)

while True:
    
    respuesta = wpp.Whasapp()

    verificar = distribuidor.codeqr(respuesta)

    if verificar != None:

        generarqr(verificar)

    
    cliente = distribuidor.cliente(respuesta)

    if cliente != None:

        verificarconexion(cliente)

    mensaje = distribuidor.mensaje()

    if cliente != None:

        procesarmensaje(mensaje)