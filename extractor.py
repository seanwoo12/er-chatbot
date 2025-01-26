import pandas as pd
import json

with open('test_data', 'r') as file:
    data = json.load(file)

longest_wait_time = data['longestWaitTime']
waiting_count = data['waitingCount']

patients = data['patients']
df = pd.DataFrame(patients)
df.to_csv('patients_data.csv', index=False)
