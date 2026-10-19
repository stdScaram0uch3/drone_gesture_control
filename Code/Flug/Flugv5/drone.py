import sys
import select
import time

import sys
import select

def hole_letzte_zeile():
    """
    Liest den gesamten Puffer und gibt die letzte darin enthaltene Zeile zurück.
    Alle älteren, zwischenzeitlich eingetroffenen Zeilen werden übersprungen.
    """
    letzte_zeile = None
    
    try:
        # Endlosschleife, die abbricht, sobald select meldet, dass der Puffer leer ist.
        while True:
            i, _, _ = select.select([sys.stdin], [], [], 0.0) # (Timeout 0.0)
            if i:
                zeile = sys.stdin.readline()
                if zeile:
                    letzte_zeile = zeile.strip()
                else:
                    break # EOF erreicht, beende die Schleife
            else:
                break # select meldet: Puffer ist leer. Breche das Lesen ab.
                
    except ValueError:
        # sys.stdin ist geschlossen
        pass
    except Exception as e:
        # Andere Fehler beim Lesen
        print(f"Fehler beim Lesen: {e}", file=sys.stderr)
        
    return letzte_zeile

if __name__ == "__main__":
    start_time = time.time()
    
    while True:
        # Rufen Sie die Funktion in Ihrer Hauptschleife auf
        neue_zeile = hole_letzte_zeile()
        if neue_zeile is not None:
            # Daten gefunden und verarbeitet
            print(f"NEUER INPUT: '{neue_zeile}'")
        else:
            # Keine neuen Daten
            print(f"Keine Daten gefunden. Zeit: {time.time() - start_time:.2f}s")
        time.sleep(0.5) # Wartezeit, um die CPU zu entlasten