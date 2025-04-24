from ultralytics import YOLO

model = YOLO("yolov5l.pt")

def detect_cars(frame, conf_threshold=0.5):
    results = model.predict(source=frame, conf=conf_threshold, verbose=False)[0]
    detections = []
    for box in results.boxes.data:
        x1, y1, x2, y2, conf, cls = box
        if int(cls) in [2, 3, 5, 7]:  # carro, moto, ônibus, caminhão
            # converte para Python int
            x1, y1, x2, y2 = map(lambda t: int(float(t)), (x1, y1, x2, y2))
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            detections.append({
                "box": (x1, y1, x2, y2),
                "center": (cx, cy),
            })
    return detections
