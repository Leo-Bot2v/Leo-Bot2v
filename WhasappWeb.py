import subprocess as sb
import threading

response = ''
proceso = None  # Variable global para almacenar el objeto de proceso
comprobar = ''
def Whasappweb():
    global response, proceso
    
    comando = 'npm start'
    proceso = sb.Popen(comando, shell=True, stdout=sb.PIPE, stderr=sb.PIPE, bufsize=1, universal_newlines=True)
    
    while True:
        for linea in proceso.stdout:
            response = linea.strip()
        # Leer la salida de error
        for linea in proceso.stderr:
            response = linea.strip()

        # Leer las últimas líneas después de que el proceso haya terminado
        for linea in proceso.stdout:
            response = linea.strip()
        
        for linea in proceso.stderr:
            response = linea.strip()
        
        if proceso.poll() is not None:
            break


def Whasapp():
    global response, comprobar  # Use the global response variable
    comprobar = response
    while True:
        if response != '':
            comprobar = response
            return response
        elif comprobar != response and comprobar != '':
            comprobar = response
            return response

# Start the Whasappweb function in a separate thread
whasapp_thread = threading.Thread(target=Whasappweb)
whasapp_thread.start()


