# credits to dronekit python ;)
# following the example on: https://dronekit-python.readthedocs.io/en/latest/guide/connecting_vehicle.html
# also on: https://dronekit-python.readthedocs.io/en/latest/guide/taking_off.html

from dronekit import connect, VehicleMode
import time
import sys

def check_mode(vehicle, exit_if_not_guided=False):
    #check if the mode is set to guided. if nothing specified, wait until it changed to guided, else end the program
    while(vehicle.mode.name.upper() != "GUIDED"):
        if(exit_if_not_guided == True):
            print(f"[SAFETY] Vehicle mode changed to {vehicle.mode.name}! Exiting program for safety.")
            try:
                vehicle.close()
                print("Connection closed.")
            except Exception as e:
                print(f"Error closing vehicle: {e}")
            sys.exit("[ABORT] Script stopped because vehicle left GUIDED mode.")
        else:
            print("Set vehicle mode to guided!")
            time.sleep(1)

def spin_motors(vehicle):
    print("Basic pre-arm checks")

    check_mode(vehicle)

    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    # Giving time for emergencies and last checks
    print("Arming motors in: ")
    for i in range (0,10):
        print(10-i)
        time.sleep(1)
    
    # Copter should arm in GUIDED mode
    while vehicle.mode.name != "GUIDED":
        print("Switch vehicle mode to guided!")
        time.sleep(1)
    
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    
    print("Armed")

    for i in range (20):
        check_mode(vehicle, exit_if_not_guided=True)
        time.sleep(1)

    # Disarming it again
    print("Disarming Vehicle")

    vehicle.armed = False

    while vehicle.armed:
        print(" Waiting for disarming...")
        time.sleep(1)

def main():
    # Connect to the Vehicle (in this case a serial endpoint)
    vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
    spin_motors(vehicle)

if __name__ == "__main__":
    main() 