import cv2
import yaml

# Carrega o caminho do vídeo do config.yaml
with open("config.yaml", "r") as f:
    base_cfg = yaml.safe_load(f)

video_path = base_cfg["video_path"]
cap = cv2.VideoCapture(video_path)
success, original_frame = cap.read()
cap.release()

if not success:
    print("Erro ao carregar o vídeo.")
    exit()

cv2.namedWindow("Clique para definir a linha", cv2.WINDOW_NORMAL)

def save_config(points):
    data = {
        "video_path": video_path.replace("\\", "/"),
        "line_position": [points[0][0], points[0][1], points[1][0], points[1][1]],
        "roi_traffic_light": [20, 20, 60, 100]  # Placeholder
    }
    with open("config.yaml", "w") as f:
        yaml.dump(data, f)
    print("Linha salva em config.yaml!")

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
                cv2.line(frame_local, points_local[0], points_local[1], (255, 0, 0), 2)
            cv2.imshow("Clique para definir a linha", frame_local)

    cv2.setMouseCallback("Clique para definir a linha", click_event, param=(frame, points))
    cv2.imshow("Clique para definir a linha", frame)

    while True:
        key = cv2.waitKey(1)
        if len(points) == 2:
            temp_frame = frame.copy()
            cv2.putText(temp_frame, "Pressione 'o' para OK ou 'r' para refazer", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
            cv2.imshow("Clique para definir a linha", temp_frame)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('o'):
                save_config(points)
                cv2.destroyAllWindows()
                exit()
            elif key == ord('r'):
                break  # Recomeça a definição da linha

