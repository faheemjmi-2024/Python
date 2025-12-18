# password strength checker

password = "Secure3p@s"
password_strength = len(password)

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Your password strenght is: ", strength)