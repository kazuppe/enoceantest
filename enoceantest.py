import serial
import platform

pf = platform.system()
if pf == 'Darwin':
    DEVICE = '/dev/tty.usbserial-FT2LMD98'  # For Mac
elif pf == 'Linux':
    DEVICE = '/dev/ttyUSB0'
elif pf == 'Windows':
    DEVICE = "COM7"
else:
    print('Not support OS. Bye.')

ser = serial.Serial(DEVICE,57600,timeout=1)

while True:
  try:
    c = ser.read()
    if c != b'U':   # Not SYNC
        continue    # Get next packet.
    else:
        clist = ['55']  # Sync(0x55)
        c = ser.read(15)
        [clist.append(format(i, '02X')) for i in c]
        print(clist)
  except KeyboardInterrupt:
    ser.flush()
    ser.close()
    exit()
