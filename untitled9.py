

import requests


def fetch_weather_data():

    API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

    response = requests.get(API_URL)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch weather data. Error:", response.status_code)
        return None


def group_weather_data_by_date(data):
    grouped_data = {}
    for entry in data["list"]:
        date = entry["dt_txt"].split()[0]
        if date not in grouped_data:
            grouped_data[date] = []
        grouped_data[date].append(entry)
    return grouped_data


def display_weather_data(grouped_data):
    while True:
        print("Enter your choice:")
        print("1: Temperature")
        print("2: Weather Description")
        print("3: Wind Speed")
        print("4: Pressure")
        print("0: Exit")

        choice = input("Choice: ")

        if choice == "0":
            print("Exiting the program.")
            break
        elif choice in {"1", "2", "3", "4"}:
            if choice == "3":
                print("Wind Speed:")
                for date, weather_data_for_date in grouped_data.items():
                    for entry in weather_data_for_date:
                        time = entry["dt_txt"].split()[1]
                        wind_speed = entry["wind"]["speed"]
                        print(
                            f"Date: {date}, Time: {time}, Wind Speed: {wind_speed} m/s")
                print()
            else:
                for date, weather_data_for_date in grouped_data.items():
                    a = 1
                    b = 1
                    c = 1
                    print(f"Weather Data for {date}:")
                    for entry in weather_data_for_date:
                        time = entry["dt_txt"].split()[1]
                        temperature = entry["main"]["temp"]
                        weather_description = entry["weather"][0]["description"]
                        wind_speed = entry["wind"]["speed"]
                        pressure = entry["main"]["pressure"]

                        if choice == "1":
                            if a == 1:
                                print("Showing Tempreature:")
                                a = a+1
                            print(
                                f"Time: {time}, Temperature: {temperature}°C")
                        elif choice == "2":
                            if b == 1:
                                print("Showing Weather Description:")
                                b = b+1
                            print(
                                f"Time: {time}, Weather: {weather_description}")
                        elif choice == "4":
                            if c == 1:
                                print("Showing Pressure:")
                                c = c+1
                            print(f"Time: {time}, Pressure: {pressure} hPa")
                    print()
        else:
            print("Invalid choice. Please try again.")


def main():
    data = fetch_weather_data()
    if not data:
        return

    grouped_data = group_weather_data_by_date(data)
    display_weather_data(grouped_data)


if __name__ == "__main__":
    main()
