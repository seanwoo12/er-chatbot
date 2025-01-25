class Patient:
    self.name = name
    self.triage = triage

    def __init__(self, name, triage):
        self.name = name
        self.triage = triage

    def __repr__(self):
        """Return a string representation of the patient."""
        return f"Patient(name={self.name}, severity={self.severity})"