input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    basic.pause(5000)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("" + RawPulseSensorSignal)
})
let RawPulseSensorSignal = 0
basic.showString("PS")
basic.forever(function () {
    RawPulseSensorSignal = pins.analogReadPin(AnalogPin.P0)
    led.plotBarGraph(
    RawPulseSensorSignal,
    1023
    )
})
