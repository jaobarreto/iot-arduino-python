import serial
import time
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os

load_dotenv()
PORTA = os.getenv("ARDUINO_PORT")

try:
    arduino = serial.Serial(PORTA, 9600, timeout=1)
    time.sleep(2)
except serial.SerialException:
    arduino = None
    print("Arduino não conectado.")

def piscar_led():
    if arduino:
        arduino.write(b'1')
    else:
        messagebox.showerror("Erro", "Arduino não conectado.")

def desligar_led():
    if arduino:
        arduino.write(b'0')
    else:
        messagebox.showerror("Erro", "Arduino não conectado.")

janela = tk.Tk()
janela.title("Controle de LED com Arduino")
janela.geometry("500x500")  

tk.Label(janela, text="Projeto Python + Arduino", font=("Arial", 18)).pack(pady=30)

btn_piscar = tk.Button(
    janela, text="Piscar LED (5x)", command=piscar_led,
    width=25, height=2, bg="green", fg="white", font=("Arial", 12)
)
btn_piscar.pack(pady=20)

btn_desligar = tk.Button(
    janela, text="Desligar LED", command=desligar_led,
    width=25, height=2, bg="red", fg="white", font=("Arial", 12)
)
btn_desligar.pack(pady=10)

janela.mainloop()
