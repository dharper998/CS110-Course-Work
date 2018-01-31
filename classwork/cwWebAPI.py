import requests
import os
def main():
    r = requests.get("https://api.spacexdata.com/v2/launches")
    spacex = r.json()
    while True:
        moredetails = input("Enter a flight number between 1 and 50 to see more details (Q to Quit): ")
        if moredetails.lower() == "q":
            break
        else:
            if int(moredetails) > 0 and int(moredetails) <= 50:
                flight = spacex[int(moredetails)-1]
                rocket = flight["rocket"]
                os.system('clear')
                print("--------------------------------------------------------------------------------")
                print("Flight Number:", flight["flight_number"])
                print("Launch Year:", flight["launch_year"])
                print("Rocket Name:", rocket["rocket_name"])
                print("Rocket Type:", rocket["rocket_type"])
                print("Payload:", rocket["second_stage"]["payloads"][0]["payload_id"])
                print("Payload Type:", rocket["second_stage"]["payloads"][0]["payload_type"])
                print("Payload Customers: ", end="")

                for i in range(len(rocket["second_stage"]["payloads"][0]["customers"])):
                    print(rocket["second_stage"]["payloads"][0]["customers"][i], end='')
                    if i+1 == len(rocket["second_stage"]["payloads"][0]["customers"]):
                        print("")
                    else:
                        print(", ", end='')

                print("Launch Site:", flight["launch_site"]["site_name_long"])
                print("Landing Success:", rocket["first_stage"]["cores"][0]["land_success"])

                print("Reused Parts:", end='')
                for i in flight["reuse"]:
                    if i == True:
                        if i+1 == len(flight["reuse"]):
                            print("")
                        else:
                            print(", ", end='')

                print("Flight Details:", flight["details"])
                print("--------------------------------------------------------------------------------")
            else:
                os.system('clear')
                print("Invalid Flight Number")
main()
