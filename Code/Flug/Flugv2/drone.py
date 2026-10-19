import sys

def main():
    for line in sys.stdin:
        print(f"Empfangen: {line.strip()}", flush=True)

if __name__ == "__main__":
    main()