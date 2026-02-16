# name : peter mbugua
# date : 12/02/2026
# string formatting

#  get string length
sentence = "i watch rugby"

string_length = len(sentence)

print(f"the length is: {string_length}")

# splitting a string
sentence_2 = "daw joke with me"
split=sentence_2.split(" ")

print(f"the first subject is:", split[0]) 
print(f"the second subject is:", split[1])


# make everything caps
mpesa_code = "ub312ee"

capitalized = mpesa_code.upper()

print("new mpesa code:", capitalized)

small_letters = mpesa_code.lower()

print("new mpesa code:", small_letters)


balance = "100kes"
amount_added = "50kes"
cleaned_balance = balance.replace("kes", "")
print("clened balance: ", cleaned_balance)
cleaned_amount_added = amount_added .replace("kes", "")
print("cleaned amount added: ", cleaned_amount_added)

new_balance = int(cleaned_balance) + int(cleaned_amount_added)
print(f"the new balance is: ", new_balance)
end = ("kes")
print(new_balance)
print(f"{new_balance}{end}")

print(f"confirmed you have received 40kes from philip. your new mpesa balance is{new_balance}{end}  ")