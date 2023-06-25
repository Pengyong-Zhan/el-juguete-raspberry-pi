from sense_hat import SenseHat
from time import sleep


sense = SenseHat()
yellow = (255, 255, 0)
blue = (0, 0, 255)


def show_msg(t):
  sense.show_message(t, text_colour=(yellow), back_colour=(blue))


def display(name, value):
  msg_txt = f'{name}, {value}'
  show_msg(msg_txt)


def main():
  sense.clear()

  pressure = str(round(sense.get_pressure(), 1))
  humidity = str(round(sense.get_humidity(), 1))
  temp = str(round(sense.get_temperature(), 1))

  show_msg("Hi, I'm your PA!")
  display('Pressure', pressure)
  sleep(1)
  display('Humidity', humidity)
  sleep(1)
  display('Temp', temp)
  sleep(1)
  sense.clear()


if __name__ == '__main__':
  main()
