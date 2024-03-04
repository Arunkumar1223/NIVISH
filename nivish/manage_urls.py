# import subprocess

# def get_local_hostname():
#     try:
#         # Run the 'hostname' command and capture the output
#         result = subprocess.run(['hostname'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

#         # Extract the hostname from the output
#         hostname = result.stdout.strip()
#         return hostname
#     except subprocess.CalledProcessError as e:
#         print(f"Error: {e}")
#         return None

# # Get and print the local hostname
# local_hostname = get_local_hostname()
# if local_hostname:
#     print(f"Local Hostname: {local_hostname}")
# else:
#     print("Failed to retrieve local hostname.")


import subprocess
result = subprocess.run(['hostname'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)

hostname = result.stdout.strip()
print(hostname,"hostname")

# hosts = ['LT-VFY-HP-045', 'nivishstaging']

if hostname == 'nivishstaging':
    url = 'http://65.1.50.165:8000/'
    print(url,"Staging")
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NTQ4MTYyLCJpYXQiOjE3MDY3NzIxNjIsImp0aSI6IjBjMmFkNWQ4MjQ3NDRjMzZiNzBhY2M3MGU2Mzc5YzMxIiwidXNlcl9pZCI6MTJ9.1KvzpJpUXgHp6AKxCXSLgaHdSdXZOixDT32qWfjk67k'

else:
    url = 'http://127.0.0.1:8000/'
    print(url,"Staging")
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjQ3MDAxLCJpYXQiOjE3MDY4NzEwMDEsImp0aSI6ImQ0OTI5NzcwMmRmMjQ0YTQ4YmE4MjEwMmYxMzk5MTc4IiwidXNlcl9pZCI6Mn0.dsECoVHMqIrRJ8Anru-RX1I2Kg7ZToC_KKu23r2rhBs'



url = url 
token1 = token

hcp_url = url+"Hcp/HcpRegistrationPost/"
provider_url = url+"Hcp/ProviderPost/"
infoseek_url = url+"Infoseek/InfoseekUserVerification/"
expirence_url = url+"Hcp/HcpExperiencePost/"
niv_url = url+"Hcp/NIVUpdate/"
hcpmaster_url = url+"Hcp/HcpMaster/"
infoseekmaster_url = url+"Infoseek/InfoseekMaster/"





# countries list


# import pycountry

# # Iterate through all countries and print their names
# for country in pycountry.countries:
#     print(country.name)




# # Country and state



# import pycountry

# def get_states(country_name):
#     try:
#         country = pycountry.countries.get(name=country_name)
#         subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)
#         states = [subdivision.name for subdivision in subdivisions]
#         return states
#     except AttributeError:
#         return None

# def main():
#     country_name = input("Enter a country name: ")
#     states = get_states(country_name)
#     states_list = []
#     if states:
#         print(f"\nStates in {country_name}:")
#         for state in states:
#             states_list.append(state)
#         print(states_list)
            
#     else:
#         print(f"\nStates not found for {country_name}")

# if __name__ == "__main__":
#     main()







