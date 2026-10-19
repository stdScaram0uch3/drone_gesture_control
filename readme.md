# Gesture-Controlled Drone (Matura Thesis)

This repository contains the test code and experimental implementations developed for my Matura thesis on autonomous drones and AI-based visual processing.

The project explores real-time gesture recognition using an embedded system to control a custom-built drone. The hardware development was split into two main prototypes: a basic platform to master flight dynamics and a second prototype equipped with onboard camera processing.

## Project Structure

The codebase is organized into modular sub-projects, each focusing on specific functional components:

* **Flight Controller Testbed (Teensy):** PID control loops and basic flight dynamics for a lightweight drone setup.
* **Companion Computer Logic (Raspberry Pi):** High-level drone control scripts, safety routines, error handling, and manual override/takeover logic.
* **Computer Vision:** Simple gesture recognition modules using image classification models.
* **System Integration:** Scripts connecting the gesture recognition pipeline directly with the Raspberry Pi control interface for real-time response.

## Repository Contents

All files included here represent the original code tests submitted alongside the written thesis.