def on_button_pressed_a():
    basic.clear_screen()
    basic.pause(5000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_string("" + str((RawPulseSensorSignal)))
input.on_button_pressed(Button.B, on_button_pressed_b)

RawPulseSensorSignal = 0
basic.show_string("PS")

def on_forever():
    global RawPulseSensorSignal
    RawPulseSensorSignal = pins.analog_read_pin(AnalogPin.P0)
    led.plot_bar_graph(RawPulseSensorSignal, 1023)
basic.forever(on_forever)
