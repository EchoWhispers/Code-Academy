# # Assume a PIN code consists of 4 random digits stored in a variable. We can call it stored_pin.
# # Then create a loop going through all possible combinations until you find the one stored.
# #
# # Found PIN: 1234



stored_pin = '1234'
for i in range(10000):
    pin = str(i).zfill(4) # uzpildo skaicias
    if pin == stored_pin:
        print(f"Found PIN: {pin}")
        break