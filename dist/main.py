import cv2
import yaml
import time
import csv
from pathlib import Path
from yolov5_loader import detect_cars
from traffic_light import detect_traffic_light_status
from tracker import VehicleTracker

# Carrega configurações
CONFIG_FILE = Path(__file__).parent / "config.yaml"
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

video_path = config["video_path"]
line       = config["line_position"]
roi        = config["roi_traffic_light"]

# Inicializa
cap       = cv2.VideoCapture(video_path)
tracker   = VehicleTracker()
car_count = 0
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

# Configurações de tempo
fps = cap.get(cv2.CAP_PROP_FPS) or 30
frame_interval = 1 / fps
start_time = time.time()

green_time = 0
red_time = 0
green_car_count = 0
frame_data = []

print(f"[INFO] Linha Y de contagem = {line[1]}")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    traffic_light = detect_traffic_light_status(frame, roi)
    dets = detect_cars(frame)
    centers = [d["center"] for d in dets]

    raw_updates = tracker.match(centers)
    updates = [(car_id, center, det["box"]) for det, (car_id, center) in zip(dets, raw_updates)]

    for car_id, center, box in updates:
        x1, y1, x2, y2 = box
        did_cross = tracker.crossed_line(car_id, center, line)
        if traffic_light == "green" and did_cross:
            car_count += 1
            green_car_count += 1

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"ID {car_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    tracker.swap()
    cv2.line(frame, tuple(line[:2]), tuple(line[2:]), (0, 255, 0), 2)

    cv2.putText(frame, f"Veiculos: {car_count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.putText(frame, f"Semaforo: {traffic_light.upper()}", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 255) if traffic_light == "green" else (0, 0, 255), 2)

    cv2.setWindowTitle("Frame", f"Carros: {car_count} | Semáforo: {traffic_light}")
    cv2.imshow("Frame", frame)

    if traffic_light == "green":
        green_time += frame_interval
    elif traffic_light == "red":
        red_time += frame_interval

    frame_data.append({
        "segundo": int(time.time() - start_time),
        "carros_no_frame": len(dets),
        "estado_semaforo": traffic_light
    })

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Salva relatório
output_dir = Path("relatorios")
output_dir.mkdir(exist_ok=True)

with open(output_dir / "relatorio.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "video", "total_carros", "tempo_verde", "tempo_vermelho",
        "media_carros_por_verde", "carros_por_segundo"
    ])
    writer.writeheader()
    writer.writerow({
        "video": Path(video_path).name,
        "total_carros": car_count,
        "tempo_verde": round(green_time, 2),
        "tempo_vermelho": round(red_time, 2),
        "media_carros_por_verde": round(green_car_count / green_time, 2) if green_time > 0 else 0,
        "carros_por_segundo": round(car_count / (green_time + red_time), 2) if (green_time + red_time) > 0 else 0
    })

with open(output_dir / "distribuicao_temporal.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["segundo", "carros_no_frame", "estado_semaforo"])
    writer.writeheader()
    for linha in frame_data:
        writer.writerow(linha)


