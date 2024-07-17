"""
Crie seus próprios QR Codes  de manira simples e rápida
"""
# Os comando abaixo podem ser retirados do comentário e rodar na primeira execução do código ou copie e cole no terminal.

# pip install pyqrcode # bibioteca para gerar QR Code
# pip install Pillow # Python Imaging Library
# pip install pypng # biblioteca geradora de png


import pyqrcode
from PIL import Image

link = input(
    "Inisira o texto que quer tranformar em QR( também funciona com links): ")
qr_code = pyqrcode.create(link)
qr_code.png("qr_code.png", scale=5)  # caso necessário pode alterar a "scale"
Image.open("qr_code.png")
