## Depto de Sistemas y Computación
## Ing. En Sistemas Computacionales
## SISTEMAS PROGRAMABLES 23a
## Autor (es): Emiliano García Cordero
## Repositorio: https://github.com/Capi2023/Practica2.1
## Fecha de revisión:   11/10/2023
## Objetivo: 2.1.1 Practica De inicio es la básico de Desplegar algo en pantalla, algunos quieren el logo de ISC, esta bien, otro texto simple, se agradece,  en el OLED DIsplay
##   

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Configuración de la pantalla OLED y pines I2C
pix_res_x = 128
pix_res_y = 64
scl_pin = 27
sda_pin = 26

def init_i2c(scl_pin, sda_pin):
    # Inicializa el dispositivo I2C
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
    return i2c_dev

def display(oled):
    oled.fill(0)  # Limpia la pantalla
    oled.text("Hola mundo", 0, 0)
    oled.show()

def main():
    i2c_dev = init_i2c(scl_pin, sda_pin)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    
    while True:
        display(oled)

if __name__ == '__main__':
    main()
