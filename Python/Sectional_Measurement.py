import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Yu Mincho'  # or any font that supports Japanese characters
import tkinter as tk

# グローバル変数nを定義
n = 10

def generate_data(n):
    x = np.linspace(0, 1, n+1)
    y = x**2
    return x, y

def main():
    global n
    x, y = generate_data(200-1)
    fig, ax = plt.subplots()
    ax.set_title("y=x^2のグラフ")
    plot_graph(x, y, ax)
    fig.canvas.manager.set_window_title('y=x^2のグラフ')
    fig.show()
    #nの値をGUIのバーで変更できるようにする
    update_value()
    print(n)
    n=int(n)
    x, y = generate_data(200-1)
    fig, ax = plt.subplots()
    plot_graph(x, y, ax)
    x, y = generate_data(n)
    print(n)
    plot_sectional(x,ax)
    fig.canvas.manager.set_window_title("x^2のグラフと"+str(n)+"分割したときの区分求積したときのイメージ")
    ax.set_title("x^2のグラフと"+str(n)+"分割したときの区分求積したときのイメージ")
    plt.show(block=True)
    
def plot_graph(x, y, ax):
    ax.plot(x, y, label="y=x^2",color="red")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

def plot_sectional(x, ax):
    global n
    width = -(1/n)
    height = x**2
    ax.bar(x, height, width=width, align="edge", label="1/nΣf(1/k)^2")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.legend()

# 変数Nの値を更新する関数
def update_value():
    def ok_clicked():
        global n
        n = max(1, min(int(float(scale.get())), 500))
        root.destroy()

    def cancel_clicked():
        global n
        n = 10
        root.destroy()

    def update_entry(*args):
        value = N.get()
        value = max(1, min(int(float(value)), 500))
        N.set(value)
        label.config(text=value)
        entry.delete(0, 'end')
        entry.insert(0, value)
        scale.set(value)  # スケールの値も更新

    def update_scale(value):
        value = max(1, min(int(float(value)), 500))
        N.set(value)
        label.config(text=value)
        entry.delete(0, 'end')
        entry.insert(0, value)


    def check_entry(*args):
        value = N.get()
        if (not value.isdigit()) or int(value) < 1 or int(value) > 500:
            N.set(int(1))

    root = tk.Tk()
    root.title("整数入力GUI")

    N = tk.StringVar(value='1')
    N.trace("w", check_entry)  # Nの値が変更されたときにcheck_entryを呼び出す

    entry = tk.Entry(root, textvariable=N)
    entry.grid(row=0, column=0, padx=10, pady=10)  # gridを使用し、パディングを追加

    scale = tk.Scale(root, from_=1, to=500, orient='horizontal', command=update_scale,variable=N)
    scale.grid(row=1, column=0, padx=10, pady=10)  # gridを使用し、パディングを追加

    label = tk.Label(root, textvariable=N)
    label.grid(row=2, column=0, padx=10, pady=10)  # gridを使用し、パディングを追加

    ok_button = tk.Button(root, text="OK", command=ok_clicked)
    ok_button.grid(row=3, column=0, padx=10, pady=10)  # gridを使用し、パディングを追加

    cancel_button = tk.Button(root, text="Cancel", command=cancel_clicked)
    cancel_button.grid(row=4, column=0, padx=10, pady=10)  # gridを使用し、パディングを追加

    update_entry("1.0")

    root.geometry("200x200")  # ウィンドウのサイズを設定
    root.wait_window()

if __name__ == "__main__":
    main()