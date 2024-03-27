def calculate_tip(bill_amount, service_quality, num_people):

  # Validate service quality input
  if service_quality < 1 or service_quality > 5:
    raise ValueError("Service quality must be between 1 and 5")

  # Calculate tip per person
  tip_per_person = bill_amount * (service_quality / 100) / num_people

  return tip_per_person

# Get user input
bill_amount = float(input("Enter the total bill amount: "))
service_quality = int(input("Enter the level of satisfaction (1-5): "))
num_people = int(input("Enter the number of people splitting the bill: "))

# Calculate and print the tip amount
try:
  tip_per_person = calculate_tip(bill_amount, service_quality, num_people)
  print(f"The tip per person is: ${tip_per_person:.2f}")
except ValueError as e:
  print(e)