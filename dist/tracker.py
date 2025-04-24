class VehicleTracker:
    def __init__(self):
        self.prev_centers = {}
        self.curr_centers = {}
        self.counted = set()
        self.next_id = 0

    def match(self, detections):
        """
        Só popula self.curr_centers e retorna lista de (id, center).
        Não altera prev_centers ainda.
        """
        self.curr_centers = {}
        ids = []
        for center in detections:
            matched_id = None
            for car_id, prev in self.prev_centers.items():
                if abs(center[0] - prev[0]) < 50 and abs(center[1] - prev[1]) < 50:
                    matched_id = car_id
                    break
            if matched_id is None:
                matched_id = self.next_id
                self.next_id += 1
            self.curr_centers[matched_id] = center
            ids.append((matched_id, center))
        return ids

    def crossed_line(self, car_id, center, line):
        # só usa prev_centers, que não mudou desde último frame
        if car_id in self.counted or car_id not in self.prev_centers:
            return False

        y_prev = self.prev_centers[car_id][1]
        y_now  = center[1]
        y_line = line[1]
        print(f"[CROSS] ID={car_id}, y_prev={y_prev}, y_now={y_now}, y_line={y_line}")

        if y_now < y_line <= y_prev:
            self.counted.add(car_id)
            print(f"[CROSS] → contou ID={car_id}")
            return True

        return False

    def swap(self):
        # só aqui sobrescrevemos prev com curr
        self.prev_centers = self.curr_centers.copy()
