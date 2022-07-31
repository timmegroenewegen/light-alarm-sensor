def on_button_pressed_a():
    basic.show_number(input.light_level())
input.on_button_pressed(Button.A, on_button_pressed_a)

radio.set_group(5)

def on_forever():
    if input.light_level() > 50:
        radio.send_string("lights on")
    else:
        radio.send_string("lights off")
    basic.pause(10000)
basic.forever(on_forever)
