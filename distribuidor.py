def codeqr(palabra):
    if "qr: " in palabra:
        return palabra.replace('qr: ', '').replace(' ', '')
    else:
        return None
    
def cliente(palabra):
    if "Client is ready!" in palabra:
        return 'cliente conectado'
    else:
        return None
    
def mensaje(palabra = ''):
    if "mensaje: " in palabra:
        return palabra.replace('mensaje: ', '')
    else:
        return None
    
def respuestas(palabra = ''):
    if "respuesta: " in palabra:
        return palabra.replace('respuesta: ', '')
    else:
        return None