import Queue
class PatientQueue(Queue):
    def __init__(self):
        self._queues = [[] for _ in range(5)]


    def add_patient(self, patient):
        if 1 <= patient.severity <= 5:
            self._queues[patient.severity - 1].append(patient)
        else:
            raise ValueError("Severity level must be between 1 and 5.")

    def next_patient(self):
        for severity in range(4, -1, -1):
            if self._queues[severity]:
                return self._queues[severity].pop(0)
        return None

    def get_position(self, Patient):
        for severity, queue in enumerate(self._queues, start=1):
            for position, patient in enumerate(queue):
                if patient.name == name:
                    return severity, position + 1
        return None

    def size(self):
        return sum(len(queue) for queue in self._queues)

    def is_empty(self):
        return all(not queue for queue in self._queues)
