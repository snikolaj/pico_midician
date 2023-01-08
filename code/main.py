import board
import busio

import time
import usb_midi
import adafruit_midi

from adafruit_midi.timing_clock import TimingClock
from adafruit_midi.channel_pressure import ChannelPressure
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.polyphonic_key_pressure import PolyphonicKeyPressure
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.start import Start
from adafruit_midi.stop import Stop
from adafruit_midi.system_exclusive import SystemExclusive
from adafruit_midi.midi_message import MIDIUnknownEvent

uart_1 = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=31250, timeout=0)
uart_2 = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=31250, timeout=0)

usb_midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0], in_channel=None, midi_out=usb_midi.ports[1], out_channel=0, in_buf_size=1024)

uart_midi_1 = adafruit_midi.MIDI(midi_in=uart_1, in_channel=0, midi_out=uart_1, out_channel=0, in_buf_size=1024)
uart_midi_2 = adafruit_midi.MIDI(midi_in=uart_2, in_channel=1, midi_out=uart_2, out_channel=1, in_buf_size=1024)

while True:
    usb_msg = usb_midi.receive()
    if usb_msg is not None and isinstance(usb_msg, MIDIUnknownEvent) is False:
        if usb_msg.channel == 0:
            print("Received on USB 1:", usb_msg, "at", time.monotonic())
            uart_midi_1.send(usb_msg)
        if usb_msg.channel == 1:
            print("Received on USB 2:", usb_msg, "at", time.monotonic())
            uart_midi_2.send(usb_msg)

    uart_msg_1 = uart_midi_1.receive()
    if uart_msg_1 is not None and isinstance(uart_msg_1, MIDIUnknownEvent) is False:
        print("Received on UART 1:", uart_msg_1, "at", time.monotonic())
        usb_midi.send(uart_msg_1)

    uart_msg_2 = uart_midi_2.receive()
    if uart_msg_2 is not None and isinstance(uart_msg_2, MIDIUnknownEvent) is False:
        print("Received on UART 2:", uart_msg_2, "at", time.monotonic())
        usb_midi.send(uart_msg_2)
