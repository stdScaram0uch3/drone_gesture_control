import sys
import select
import time

def hole_neueste_stdin_zeile():
    try:
        # i: Input ready, o: Output ready, e: Error
        i, _, _ = select.select([sys.stdin], [], [], 0.0) 
    except ValueError:
        # Tritt auf, wenn sys.stdin bereits geschlossen ist (z.B. nach EOF in einer Pipe).
        return None
    
    # 2. Wenn sys.stdin im 'i'-Tupel enthalten ist, sind Daten verfügbar.
    if i:
        # Nächste Zeile lesen.
        zeile = sys.stdin.readline()
        if zeile:
            # Wenn readline() Daten zurückgibt.
            return zeile.strip()
        else:
            return None
    else:
        return None

if __name__ == "__main__":
    start_time = time.time()
    
    while True:
        # Rufen Sie die Funktion in Ihrer Hauptschleife auf
        neue_zeile = hole_neueste_stdin_zeile()
        if neue_zeile is not None:
            # Daten gefunden und verarbeitet
            print(f"NEUER INPUT: '{neue_zeile}'")
        else:
            # Keine neuen Daten
            print(f"Keine Daten gefunden. Zeit: {time.time() - start_time:.2f}s")
        time.sleep(0.5) # Wartezeit, um die CPU zu entlasten