#!/bin/bash
# detect.py in hand_venv starten und stdout in eine Pipe geben
source ./hand_venv/bin/activate
python detect.py | (
    source ./drone_venv/bin/activate
    python drone.py
)