import cv2
import yaml

# Carrega vídeo
with open("config.yaml", "r") as f:
    base_cfg = yaml.safe_load(f)

video_path = base_cfg.get("video_path", "input_video.mp4")
cap = cv2.VideoCapture(video_path)

# Pega o primeiro frame
ret, original_frame = cap.read()
cap.release()
if not ret:
    print("Erro ao ler o vídeo")
    exit()

cv2.namedWindow("Defina ROI do Semáforo", cv2.WINDOW_NORMAL)

def save_config(pts):
    x1, y1 = pts[0]
    x2, y2 = pts[1]
    roi = [min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)]
    base_cfg["roi_traffic_light"] = roi
    with open("config.yaml", "w") as f:
        yaml.dump(base_cfg, f)
    print(f"ROI salva: {roi} em config.yaml")

# Loop principal
while True:
    frame = original_frame.copy()
    points = []

    def click_event(event, x, y, flags, param):
        frame_local, points_local = param
        if event == cv2.EVENT_LBUTTONDOWN and len(points_local) < 2:
            points_local.append((x, y))
            cv2.circle(frame_local, (x, y), 5, (0, 0, 255), -1)
            if len(points_local) == 2:
                cv2.rectangle(frame_local, points_local[0], points_local[1], (255, 0, 0), 2)
            cv2.imshow("Defina ROI do Semáforo", frame_local)

    cv2.setMouseCallback("Defina ROI do Semáforo", click_event, param=(frame, points))
    cv2.imshow("Defina ROI do Semáforo", frame)

    while True:
        key = cv2.waitKey(1)
        if len(points) == 2:
            temp_frame = frame.copy()
            cv2.putText(temp_frame, "Pressione 'o' para OK ou 'r' para refazer", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            cv2.imshow("Defina ROI do Semáforo", temp_frame)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('o'):
                save_config(points)
                cv2.destroyAllWindows()
                exit()
            elif key == ord('r'):
                break  # Recomeça
