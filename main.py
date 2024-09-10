def gira_a_destra(VELOCITA: number, TEMPO: number):
    pins.analog_write_pin(AnalogPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P14, VELOCITA)
    pins.analog_write_pin(AnalogPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P16, 0)
    basic.pause(TEMPO)
def muovi_avanti(VELOCITA2: number, TEMPO2: number):
    pins.analog_write_pin(AnalogPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P14, VELOCITA2)
    pins.analog_write_pin(AnalogPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P16, VELOCITA2)
    basic.pause(TEMPO2)
def scrivi_su_oled(MESSAGGIO: str):
    OLED12864_I2C.clear()
    OLED12864_I2C.show_string(0, 0, MESSAGGIO, 1)
def muovi_indietro(VELOCITA3: number, TEMPO3: number):
    pins.analog_write_pin(AnalogPin.P13, VELOCITA3)
    pins.analog_write_pin(AnalogPin.P14, 0)
    pins.analog_write_pin(AnalogPin.P15, VELOCITA3)
    pins.analog_write_pin(AnalogPin.P16, 0)
    basic.pause(TEMPO3)
def gira_a_sinistra(VELOCITA4: number, TEMPO4: number):
    pins.analog_write_pin(AnalogPin.P13, 0)
    pins.analog_write_pin(AnalogPin.P14, 0)
    pins.analog_write_pin(AnalogPin.P15, 0)
    pins.analog_write_pin(AnalogPin.P16, VELOCITA4)
    basic.pause(TEMPO4)
velocita = 800
led.enable(True)
OLED12864_I2C.init(60)
OLED12864_I2C.show_string(0, 0, "Sono acceso.", 1)

def on_forever():
    scrivi_su_oled("Vado Avanti")
    muovi_avanti(velocita, 3000)
    scrivi_su_oled("Giro a Destra")
    gira_a_destra(velocita, 1500)
basic.forever(on_forever)
