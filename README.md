# pico_midician

This is a simple Raspberry Pi Pico-powered MIDI-USB converter, with more features to come. [Details outlined in this blog post.](https://snikolaj.github.io/electronics-projects/2023/01/08/usb-to-midi.html)

It features two MIDI outputs with a spec-compliant schematic and simple programming/connections, simply using CircuitPython and Adafruit MIDI.

The circuit can be improved by replacing the transistors with simple buffers, you can get away with almost no resistors!

Theory of operation for the code: MIDI data is sent through USB and UART, then parsed by the library, and the main loop checks if messages have been received on all three interfaces.
The UART MIDIs are connected to channels 1 and 2 and the board automatically handles routing. 
The optocouplers are there as part of the [standard MIDI input circuit](https://learn.sparkfun.com/tutorials/midi-tutorial/hardware--electronic-implementation), but the transistors are set up as simple LED drivers - MIDI compliant as well. This is important because improper MIDI could theoretically damage something down the line, and synthesizers are usually extremely expensive.
I want to add a small display and buttons, so that it can function as a SysEx librarian, chord machine and sequencer, but there's time for all of that.
