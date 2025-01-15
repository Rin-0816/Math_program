import cv2
import numpy as np
import time
from collections import deque
import matplotlib.pyplot as plt
import csv

def measure_yellow_object_distance(camera_matrix, dist_coeffs, object_diameter, csv_filename, max_time=30):
    # カメラ映像をキャプチャ
    cap = cv2.VideoCapture(0)

    # 距離データを保存するためのキュー (最大100件)
    distance_data = deque(maxlen=100)

    # グラフの初期設定
    plt.ion()
    fig, ax = plt.subplots()
    x_data = []
    y_data = []

    start_time = time.time()
    
    elapsed_time = 0 
    # CSV ファイルの準備 (データを毎回上書き)
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time (s)", "Distance (m)"])  # ヘッダー行

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # HSVに変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        
        
        # 黄色の範囲を定義（調整が必要）
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        # マスクを作成
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # 輪郭を検出
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # 最も大きな輪郭を取得
            largest_contour = max(contours, key=cv2.contourArea)
            (x, y), radius = cv2.minEnclosingCircle(largest_contour)

            if radius > 10:  # 半径が十分大きい場合のみ処理
                # 物体を描画
                center = (int(x), int(y))
                cv2.circle(frame, center, int(radius), (0, 255, 0), 2)

                # 距離計算 (ピンホールカメラモデル)
                focal_length = camera_matrix[0, 0]  # カメラ行列の焦点距離
                distance = (object_diameter * focal_length) / (2 * radius)  # 推定距離
                distance_data.append(distance)

                # 距離を表示
                cv2.putText(frame, f"Distance: {distance:.2f} m", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # グラフ用データ更新
                elapsed_time = time.time() - start_time
                x_data.append(elapsed_time)
                y_data.append(distance)

                # データをCSVに保存
                with open(csv_filename, mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([elapsed_time, distance])

        # 結果を表示
        
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)
        
        cv2.moveWindow("Frame", 1000, 0)  # カメラウィンドウを (100, 100) に配置
        cv2.moveWindow("Mask", 1000, 500)
        # グラフをリアルタイム更新
        ax.clear()
        ax.plot(x_data, y_data, label="距離 (m)")
        ax.set_xlim(left=0, right=max(30, elapsed_time))
        ax.set_ylim(0, max(1, max(y_data, default=1)))
        ax.set_xlabel("時間 (s)")
        ax.set_ylabel("距離 (m)")
        ax.set_title("リアルタイム距離測定")
        ax.legend()
        ax.grid(True)
        plt.pause(0.01)

        # 経過時間が指定時間を超えたら終了
        if elapsed_time > max_time:
            time.sleep(1)
            plt.close(fig)
            break

        # キーイベント処理
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    plt.ioff()
    plt.show()

# 使用例
camera_matrix = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]], dtype=np.float32)
dist_coeffs = np.zeros(5)  # 歪み係数
object_diameter = 0.1  # 黄色物体の直径 (m)
csv_filename = "yellow_object_distance.csv"

measure_yellow_object_distance(camera_matrix, dist_coeffs, object_diameter, csv_filename)
