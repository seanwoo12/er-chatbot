import requests
import pandas as pd
from Classes.Patient import Patient

url = "https://ifem-award-mchacks-2025.onrender.com/api/v1/queue"

def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def extract_data(data):
    if data is None:
        return None

    patients = data["patients"]
    longest_wait_time = data["longestWaitTime"]
    waiting_time = data["waitingCount"]
    patient_data = []
    for patient in patients:
        p = Patient(patient["id"],
                    patient["arrival_time"],
                    patient["queue_position"],
                    patient["status"],
                    patient["time_elapsed"],
                    patient["triage_category"])
        patient_data.append(p)

    return patient_data, longest_wait_time, waiting_time

data = fetch_data()
d = extract_data(data)

