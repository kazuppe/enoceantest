import serial

DEVICE = '/dev/tty.usbserial-FT2LMD98'  # For Mac
# DEVICE = '/dev/ttyUSB0'    # For Raspberry Pi
# DEVICE = 'COM7'    # For Windwos

ser = serial.Serial(DEVICE,57600,timeout=1)

while True:
  try:
    c = ser.read()
    if c != b'U':   # Not SYNC
        continue    # Get next packet.
    else:
        clist = [85]
        c = ser.read(15)
        [clist.append(i) for i in c]
        print(clist)
  except KeyboardInterrupt:
    ser.flush()
    ser.close()
    exit()
