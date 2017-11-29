import pexpect
import sys,time


def do_led_colour(a,r,g,b):
 con = pexpect.spawn('gatttool -b '+a+' -I')
 con.expect('\[LE\]>')
 print "connecting"
 con.sendline('connect')
 con.expect(['\[CON\]','Connection successful.*\[LE\]>'])

 print "connected"    
 value="#B%d,%d,%d,*"%(r,g,b)
 cmd_string=""
 for i in value:
  cmd_string += '%02x' % (ord(i))
 command = 'char-write-req 0x0025 %s' % (cmd_string)
 con.sendline(command)
 con.expect('\[LE\]>')
 con.sendline('quit')

# find out what the bluetooth address for your ironbot is:
# TODO run 'sudo hcitool lescan' and check for RS-BLE entries
a="9C:1D:58:88:1E:29" #RS-BLE

# connect
# gatttool -b <mac of ironbot> -I
# reponse should be something like connection successful
# and the led on the ironbot (not the front one)that is red should now be blue
# send the command to the handle which has a uuid of 0000fff1
# got the handle by using char-desc and checking the line "handle: 0x0025, uuid: 0000fff1-0000-1000-8000-00805f9b34fb"


do_led_colour(a,255,255,255)
time.sleep(1)
do_led_colour(a,255,0,0)
time.sleep(1)
do_led_colour(a,0,255,0)
time.sleep(1)
do_led_colour(a,0,0,255)
time.sleep(1)
do_led_colour(a,0,0,0)
