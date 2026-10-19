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

def arm_and_takeoff(vehicle, aTargetAltitude, timeout=60):
    # Arms vehicle and fly to aTargetAltitude.

    print("Basic pre-arm checks")
    # Don't try to arm until autopilot is ready

    check_mode(vehicle)

    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    # Copter should arm in GUIDED mode
    print("Arming motors")
    vehicle.armed   = True

    start = time.time()
    while not vehicle.armed:
        if time.time() - start > timeout:
            raise TimeoutError("Arming timed out")
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

    start = time.time()
    while True:
        check_mode(vehicle, True)
        alt = vehicle.location.global_relative_frame.alt
        print(" Altitude:", alt)
        if alt is not None and alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        if time.time() - start > timeout:
            raise TimeoutError("Takeoff timed out")
        time.sleep(1)

def land(vehicle, timeout=60):
    check_mode(vehicle, True)

    print("Landing...")
    vehicle.mode = VehicleMode("LAND")
    start = time.time()
    while getattr(vehicle.mode, 'name', None) != "LAND":
        if time.time() - start > 5:
            raise TimeoutError("Failed to set LAND mode")
        time.sleep(0.5)
        if time.time() - start > timeout:
            raise TimeoutError("Landing timed out")
        
def disarm(vehicle, timeout=30):
    check_mode(vehicle, True)
    """Disarm vehicle once landed."""
    print("Disarming Vehicle")
    # safety: don't disarm if clearly airborne
    try:
        alt = vehicle.location.global_relative_frame.alt
    except Exception:
        alt = None
    if alt is not None and alt > 1.0:
        raise RuntimeError("Refuse to disarm while >1.0m altitude")

    vehicle.armed = False
    start = time.time()
    while vehicle.armed:
        if time.time() - start > timeout:
            raise TimeoutError("Disarming timed out")
        print(" Waiting for disarming...")
        time.sleep(1)

def main(vehicle):
    try:
        arm_and_takeoff(vehicle, 3)
        time.sleep(20)
        land(vehicle)
        disarm(vehicle)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            vehicle.close()
        except:
            pass

if __name__ == "__main__":
    vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=57600)
    main(vehicle)