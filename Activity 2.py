print("Welcome to the country code checker!")

country_code = {'India' : '0091',
                'Nepal' : '0007',
                'Malaysia' : '0247'}

print("\nThe code for the country of India is:")
print(country_code.get('India', 'Not found, sorry!'))

print("\nThe country code for Japan is:")
print(country_code.get("Japan", "Not found, sorry!"))


print("\nThank you gor using this website!")