function gira_a_destra (VELOCITA: number, TEMPO: number) {
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P14, VELOCITA)
    pins.analogWritePin(AnalogPin.P15, 0)
    pins.analogWritePin(AnalogPin.P16, 0)
    basic.pause(TEMPO)
}
function muovi_avanti (VELOCITA: number, TEMPO: number) {
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P14, VELOCITA)
    pins.analogWritePin(AnalogPin.P15, 0)
    pins.analogWritePin(AnalogPin.P16, VELOCITA)
    basic.pause(TEMPO)
}
function scrivi_su_oled (MESSAGGIO: string) {
    OLED12864_I2C.clear()
    OLED12864_I2C.showString(
    0,
    0,
    MESSAGGIO,
    1
    )
}
function muovi_indietro (VELOCITA: number, TEMPO: number) {
    pins.analogWritePin(AnalogPin.P13, VELOCITA)
    pins.analogWritePin(AnalogPin.P14, 0)
    pins.analogWritePin(AnalogPin.P15, VELOCITA)
    pins.analogWritePin(AnalogPin.P16, 0)
    basic.pause(TEMPO)
}
function gira_a_sinistra (VELOCITA: number, TEMPO: number) {
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P14, 0)
    pins.analogWritePin(AnalogPin.P15, 0)
    pins.analogWritePin(AnalogPin.P16, VELOCITA)
    basic.pause(TEMPO)
}
let velocita = 800
led.enable(true)
OLED12864_I2C.init(60)
OLED12864_I2C.showString(
0,
0,
"Sono acceso.",
1
)
basic.forever(function () {
    scrivi_su_oled("Vado Avanti")
    muovi_avanti(velocita, 3000)
    scrivi_su_oled("Giro a Destra")
    gira_a_destra(velocita, 1200)
})
