import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import simpledialog

def koch_curve(n, p1=np.array([0, 0]), p2=np.array([1, 0])):
    if n == 0:
        return np.array([p1, p2])
    s = p1 + (p2 - p1) / 3
    t = p1 + (p2 - p1) * 2 / 3
    u = s + (t - s) * np.exp(1j * np.pi / 3)
    return np.concatenate([koch_curve(n-1, p1, s), koch_curve(n-1, s, u), koch_curve(n-1, u, t), koch_curve(n-1, t, p2)])

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    n = simpledialog.askinteger("Input", "Nの値を入力してください")
    curve = koch_curve(n)
    plt.figure(figsize=(8, 8))
    plt.plot(curve.real, curve.imag)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

if __name__ == "__main__":
    main()