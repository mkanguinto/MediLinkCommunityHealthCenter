import json
from medilink_contract import build_summary

patient = {"patient_id": "P-001", "name": "Juan Dela Cruz"}
appointments = [{"appointment_id": "A-100", "date": "2026-10-15", "doctor": "Dr. Santos"}]

summary = build_summary(patient, appointments)
print(json.dumps(summary, indent=2))