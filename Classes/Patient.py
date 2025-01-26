class Patient:
    def __init__(self, p_id, arrival_time, queue_position, status, time_elapsed, triage_category):
        self.id = p_id
        self.arrival_time = arrival_time
        self.queue_position = queue_position
        self.status = status
        self.time_elapsed = time_elapsed
        self.triage_category = triage_category

    def __repr__(self):
        return (f"Patient(id={self.id}, arrival_time={self.arrival_time}, "
                f"queue_position={self.queue_position}, status={self.status}, "
                f"time_elapsed={self.time_elapsed}, triage_category={self.triage_category})")
