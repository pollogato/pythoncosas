
import smtplib
# https://docs.python.org/3/library/smtplib.html

# Configuración del remitente y receptor
CORREO_REMITENTE = "tu_correo@dominio.com"
PASS = "tu contrasena"
CORREO_DESTINATARIO = "destinatario@dominio.com"

### OJO NUNCA SE RECOMIENDA PONER LAS CONTRASENAS EN EL MISMO CÓDIGO ###
### SI USAN SERVICIO DE GOOGLE DEBEN GENERAR UNA CONTRASENA PARA APP Y AUTORIZAR SU USO ###

# Encabezado de asunto
DE = "From: " + CORREO_REMITENTE + "\n"
PARA = "To: " + CORREO_DESTINATARIO + "\n"
ASUNTO = "Subject: Aqui va el asunto del correo\n"  


CUERPO = "sirve asunto \n Hola, este es un mensaje de prueba, " + \
        "me encuentro probando las funciones del modulo smtplib. \n" + \
        "Que tenga buenas tardes"


MENSAJE = DE + PARA + ASUNTO + "\n" + CUERPO


# Inicianizalndo paramametros correo
CORREO = smtplib.SMTP('smtp.gmail.com', 587)
CORREO.starttls()

CORREO.login(CORREO_REMITENTE , PASS)
CORREO.sendmail(CORREO_REMITENTE, CORREO_DESTINATARIO, MENSAJE)

CORREO.quit()