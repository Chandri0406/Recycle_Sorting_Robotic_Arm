#This code is for micropython file
import machine
import ubinascii

uart = machine.UART(1, baudrate=9600, tx=machine.Pin(12), rx=machine.Pin(13))

def send_data(data):
    uart.write(ubinascii.hexlify(data))