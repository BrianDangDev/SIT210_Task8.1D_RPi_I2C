import smbus
import time

BH1750_sensor= 0x23
turnoff = 0x00
turnon = 0x01
Reset = 0x07
recieved_address = 0x20

bus = smbus.SMBus(1)
 
def Light():
     address = bus.read_i2c_block_data(BH1750_sensor,recieved_address)
     value = Light_intensity(address)
     return value
   
def Light_intensity(address):
  return((address[1] + (256 * address[0]))/1.2)
   
 
def main():
   
    while True:
     intensity = Light()
     if intensity > 300:
         print("Too bright")
         
     elif intensity > 200 and intensity < 300:
        print("Bright")
       
     elif intensity > 100 and intensity < 200:
        print("Medium")
       
     elif intensity > 30 and intensity < 100:
        print("Dark")
       
     else:
        print("Too Dark")
     time.sleep(0.5)
   
if __name__ == "__main__":
    main()
    time.sleep(5)
