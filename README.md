# Practica2.1
Foto de prueba practica hola mundo en pantalla oled

# CÓDIGO
```python
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

```

![](imagenes/20231010_144851.jpg)

# CÓDIGO
```python
## Depto de Sistemas y Computación
## Ing. En Sistemas Computacionales
## SISTEMAS PROGRAMABLES 23a
## Autor (es): Emiliano García Cordero
## Repositorio: https://github.com/Capi2023/Practica2.1
## Fecha de revisión:   11/10/2023
## Objetivo: 2.1.2  Desplegar la hora de Internet en la Pico usando su Wifi integrada para que interrogue un servidor NTP Time Server, en el OLED DIsplay
##   

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import utime
import ntptime

# Configuración de la pantalla OLED y pines I2C
pix_res_x = 128
pix_res_y = 64
scl_pin = 27
sda_pin = 26

def init_i2c(scl_pin, sda_pin):
    # Inicializa el dispositivo I2C
    i2c_dev = I2C(1, scl=Pin(scl_pin), sda=Pin(sda_pin), freq=400000)
    return i2c_dev

def update_time():
    try:
        # Sincroniza la hora con un servidor NTP (usando el servidor predeterminado)
        ntptime.host = 'time.google.com'
        print("Hora actual actualizada desde Internet:", utime.localtime())
    except OSError as e:
        print("Error al sincronizar la hora desde Internet:", e)

def display_time(oled, time_data):
    oled.fill(0)  # Limpia la pantalla
    oled.text("Hora actual:", 0, 0)
    oled.text("{:02d}:{:02d}:{:02d}".format(time_data[3], time_data[4], time_data[5]), 0, 16)
    oled.show()

def main():
    i2c_dev = init_i2c(scl_pin, sda_pin)
    oled = SSD1306_I2C(pix_res_x, pix_res_y, i2c_dev)
    
    while True:
        update_time()  # Actualiza la hora desde Internet
        current_time = utime.localtime()
        
        # Muestra la hora en la pantalla OLED
        display_time(oled, current_time)
        
        # Espera 1 segundo antes de actualizar la hora nuevamente
        utime.sleep(1)

if __name__ == '__main__':
    main()

```

Foto de prueba practica para hola mundo y hora en pantalla oled

![](imagenes/20231010_143056.jpg)
