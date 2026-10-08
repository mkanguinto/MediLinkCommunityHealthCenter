import unittest
from medilink_contract import build_summary


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.patient = {"patient_id": "P-001", "name": "Kaye Ann Nicole J. Guinto"}
        self.appointments = [{"appointment_id": "A-100"}]

    def test_summary_preserves_required_public_contract(self):
        summary = build_summary(self.patient, self.appointments)
        self.assertEqual(set(summary.keys()), {"patient", "appointments", "clinic_status"})
        self.assertEqual(summary["patient"], self.patient)
        self.assertEqual(summary["appointments"], self.appointments)

    def test_default_status_is_active(self):
        self.assertEqual(build_summary(self.patient, [])["clinic_status"], "ACTIVE")

    def test_status_is_normalized(self):
        summary = build_summary(self.patient, [], " maintenance ")
        self.assertEqual(summary["clinic_status"], "MAINTENANCE")

    def test_patient_must_be_dict(self):
        with self.assertRaises(ValueError):
            build_summary("not a dict", [])

    def test_patient_must_have_patient_id(self):
        with self.assertRaises(ValueError):
            build_summary({"name": "No ID"}, [])

    def test_appointments_must_be_list(self):
        with self.assertRaises(ValueError):
            build_summary(self.patient, "not a list")

    def test_status_must_be_non_empty(self):
        with self.assertRaises(ValueError):
            build_summary(self.patient, [], "   ")


if __name__ == "__main__":
    unittest.main()