# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = "Maria", age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# Estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 
"Rohan", age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# Estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = "Valentina", age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# Add your code here
names = ["Maria", "Rohan", "Valentina"]
insurance_costs = [4150.0, 5320.0, 35210.0]
insurance_data = list(zip(names, insurance_costs))
print("Actual cost: " + str(insurance_data))

estimated_insurance_data = []
estimated_insurance_data.append(("Maria", maria_insurance_cost))
estimated_insurance_data.append(("Rohan", rohan_insurance_cost))
estimated_insurance_data.append(("Valentina", valentina_insurance_cost))
print("Estimated cost: " + str(estimated_insurance_data))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)
medical_records = list(zip(names, insurance_costs))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]
print(first_medical_record)

medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))

cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

occurrences_paul = names.count("Paul")
print("There are " + str(occurrences_paul) + " individuals with the name Paul in our medical records.")
