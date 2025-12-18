# transport Mode Selection

distance = 8

if distance < 3:
    transport = "Walk"
elif distance <= 15:
    transport = "Bike"
else:
    transport = "Car"

print("AI recommends the transport of: ", transport)