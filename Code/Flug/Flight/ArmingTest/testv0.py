# credits to dronekit python ;)
# following the example on: https://dronekit-python.readthedocs.io/en/latest/guide/connecting_vehicle.html
# also on: https://dronekit-python.readthedocs.io/en/latest/guide/taking_off.html

from dronekit import connect, VehicleMode
import time

def spin_motors(vehicle):
    """
    Arms vehicle and fly to aTargetAltitude.
    """

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    # Giving time for emergencies and last checks
    print("Arming motors in: ")
    for i in range (0,10):
        print(i)
        time.sleep(1)
    
    # Copter should arm in GUIDED mode
    vehicle.mode    = VehicleMode("GUIDED")
    vehicle.armed   = True

    # Confirm vehicle armed before attempting to take off
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)
    
    print("Armed")

    time.sleep(10)

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