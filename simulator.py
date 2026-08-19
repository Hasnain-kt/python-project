import random
queue = []
doctors = []

for i in range(3):
doctor = {
    "available": True,
    "finish_time": 0
}
doctors.append(doctor)

clock = 0
treatment = 0 

for i in range(1 , 6):

    arrival = random.expovariate(10 / 60)

    clock = clock + arrival

    patient_info = {
    "id" : i,
    "arrival_time" : clock,
    "treatment_time" : random.expovariate(1 / 20)
    } 
    queue.append(patient_info)

while (treatment < i):
    # if clock >= doctor["finish_time"]:
    #     doctor["available"] = True
    #     print("\n******Doctor is now available******")
        for dr in doctors:
            if dr["available"] == True:
                selected_doctor = dr 
                selected_doctor["available"] = False
                selected_doctor["finish_time"] = finish_time
                print("doctor available ")

            else:
                clock = selected_doctor["finish_time"]

    print(f"\nPatient ID:{patient_info["id"]} --> arrives at {clock:.2f}")

    if selected_doctor["available"] == True:
        patient = queue.pop(0)

        selected_doctor["available"] = False
        print("\n")
        print(f"Patient {patient["id"]} starts treatment at {clock:.2f}")
        print(f"patient treatment time --> {patient["treatment_time"]:.2f}")

        if patient_info["arrival_time"] > selected_doctor["finish_time"]:

            departure_time = clock + patient["treatment_time"] 
            print(f"patient{patient["id"]} departure time : {departure_time:.2f}")
        else:    
            waiting_time =  selected_doctor["finish_time"] - patient_info["arrival_time"] 
            print(f"patient {patient["id"]} waiting time :{waiting_time:.2f}")
            departure_time = clock + patient["treatment_time"]
            print(f"patient {patient["id"]} departure time :{departure_time:.2f}")

        treatment = treatment + 1

        finish_time = clock + patient["treatment_time"]
        selected_doctor["finish_time"] = finish_time

        print(f"Doctor will finish at {finish_time:.2f}")

    else:
        print("Doctor is busy")
      
