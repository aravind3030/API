#Doctors Listing
  {
    "id": 1,
    "name": "Dr. Smith",
    "specialization": "Cardiologist",
    "schedule": "Evenings, Mon-Sat",
    "max_patients_per_day": 10
  },
  {
    "id": 2,
    "name": "Dr. Johnson",
    "specialization": "Dermatologist",
    "schedule": "Evenings, Mon-Fri",
    "max_patients_per_day": 8
  }
#Doctor Detail
{
  "id": 1,
  "name": "Dr. Smith",
  "specialization": "Cardiologist",
  "schedule": "Evenings, Mon-Sat",
  "max_patients_per_day": 10,
  "available_dates": ["2023-10-02", "2023-10-03", ...]
}

#Appointment Booking
{
  "doctor_id": 1,
  "patient_name": "John Doe",
  "appointment_date": "2023-10-05"
}
#Example Response
{
  "id": 123,
  "doctor_id": 1,
  "patient_name": "John Doe",
  "appointment_date": "2023-10-05",
  "status": "Booked"
}

