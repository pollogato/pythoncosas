
###############################################################################
# Inspiración de: https://youtube.com/shorts/VAQYQUM3IpY?si=DU05Z2OfM2fw-fGf
###############################################################################

def encode(texto):
    with open('mensaje_codificado.code', 'w') as file:
        for a in texto.encode('utf-8'):
            bits = format(a, '08b')
            for bit in bits:
                if bit == '0':
                    file.write(" ")
                if bit == '1':
                    file.write("\t")
                    

def decode(file):
    with open(file, 'r') as f:
        data = f.read()
        for index in range(0,len(data),8):
            letra = ""
            for char in data[index:index+8]:
                if char == " ":
                    letra += '0'
                else:
                    letra += '1'
            letra = chr(int(letra, 2))
            print(letra, end = '')


#encode('Hola, soy pabo')

#decode('mensaje_codificado.code')

        