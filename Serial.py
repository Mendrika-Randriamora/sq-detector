import serial
import time

def envoyer_message(port="/dev/ttyACM0", message=0, baudrate=9600):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)  # laisse le temps à l'Arduino de reset

        # Ajout du \n pour correspondre à ton code Arduino
        ser.write((str(message) + "\n").encode())

        ser.close()
        print("Message envoyé")

    except Exception as e:
        print(f"Erreur : {e}")