class PatientQueue:
    def __init__(self):
        self._queues = [[] for _ in range(5)]

    def add_patient(self, patient):
        if 1 <= patient.triage_category <= 5:
            self._queues[patient.triage_category - 1].append(patient)
        else:
            raise ValueError("Triage category must be between 1 and 5.")

    def next_patient(self):
        for severity in range(4, -1, -1):
            if self._queues[severity]:
                return self._queues[severity].pop(0)
        return None

    def size(self):
        return sum(len(queue) for queue in self._queues)

    def is_empty(self):
        return all(not queue for queue in self._queues)
