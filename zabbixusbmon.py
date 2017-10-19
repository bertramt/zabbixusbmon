#!/usr/bin/python3

from evdev import InputDevice, categorize, ecodes, KeyEvent
from pyzabbix import ZabbixMetric, ZabbixSender
import re, datetime
gamepad = InputDevice('/dev/input/event0')

UPDATE_INTERVAL = 10000
CURRENT_INTERVAL = 10
b1 = 0
b2 = 0
b3 = 0
b4 = 0
b5 = 0
b6 = 0
b7 = 0
b8 = 0
b9 = 0
b10 = 0
b11 = 0
b12 = 0


for event in gamepad.read_loop():
  if event.type == ecodes.EV_KEY:
    keyevent = categorize(event)
    if keyevent.keystate == KeyEvent.key_down or keyevent.keystate == KeyEvent.key_up:
      print (event)
      #print (keyevent.keycode)
      eventdata = (re.sub("[^0-9^.\,]", "", str(event)))
      eventstring = eventdata.split(",")
      print (eventstring[1])
      btn_num = int(eventstring[1])
      if btn_num > 287 and btn_num < 300:
        btn_num = btn_num-287
        packet = [
          ZabbixMetric('pimon', 'usb.joypad.b'+str(btn_num), int(eventstring[3]))
        ]
        result = ZabbixSender(use_config=True).send(packet)

  #Update Every so often just because
  if CURRENT_INTERVAL > 0:
    #print (CURRENT_INTERVAL)
    CURRENT_INTERVAL = CURRENT_INTERVAL-1
  else:
    CURRENT_INTERVAL = UPDATE_INTERVAL
    print("UPDATE: "+str(datetime.datetime.now()))
    pressed = (gamepad.active_keys())
    if 288 in pressed:
      b1 = 1
    else:
      b1 = 0
    if 289 in pressed:
      b2 = 1
    else:
      b2 = 0
    if 290 in pressed:
      b3 = 1
    else:
      b3 = 0
    if 291 in pressed:
      b4 = 1
    else:
      b4 = 0
    if 292 in pressed:
      b5 = 1
    else:
      b5 = 0
    if 293 in pressed:
      b6 = 1
    else:
      b6 = 0
    if 294 in pressed:
      b7 = 1
    else:
      b7 = 0
    if 295 in pressed:
      b8 = 1
    else:
      b8 = 0
    if 296 in pressed:
      b9 = 1
    else:
      b9 = 0
    if 297 in pressed:
      b10 = 1
    else:
      b10 = 0
    if 298 in pressed:
      b11 = 1
    else:
      b11 = 0
    if 299 in pressed:
      b12 = 1
    else:
      b12 = 0
    
    print("B1:"+str(b1))
    print("B2:"+str(b2))
    print("B3:"+str(b3))
    print("B4:"+str(b4))
    print("B5:"+str(b5))
    print("B6:"+str(b6))
    print("B7:"+str(b7))
    print("B8:"+str(b8))
    print("B9:"+str(b9))
    print("B10:"+str(b10))
    print("B11:"+str(b11))
    print("B12:"+str(b12))

    packet = [
      ZabbixMetric('pimon', 'usb.joypad.b1', b1),
      ZabbixMetric('pimon', 'usb.joypad.b2', b2),
      ZabbixMetric('pimon', 'usb.joypad.b3', b3),
      ZabbixMetric('pimon', 'usb.joypad.b4', b4),
      ZabbixMetric('pimon', 'usb.joypad.b5', b5),
      ZabbixMetric('pimon', 'usb.joypad.b6', b6),
      ZabbixMetric('pimon', 'usb.joypad.b7', b7),
      ZabbixMetric('pimon', 'usb.joypad.b8', b8),
      ZabbixMetric('pimon', 'usb.joypad.b9', b9),
      ZabbixMetric('pimon', 'usb.joypad.b10', b10),
      ZabbixMetric('pimon', 'usb.joypad.b11', b11),
      ZabbixMetric('pimon', 'usb.joypad.b12', b12),

    ]
    result = ZabbixSender(use_config=True).send(packet)