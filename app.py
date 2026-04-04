from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "e7cde81c3a0cb242fe3960680cb1b8ea"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    history = []

    # ✅ Load history
    try:
        with open("history.txt", "r") as file:
            history = file.readlines()
            history = [h.strip() for h in history[::-1]]
            history = history[:10]
    except:
        history = []

    if request.method == "POST":
        city = request.form.get("city")

        try:
            # 🌦 Current Weather API
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if str(data["cod"]) != "200":
                error = "City not found!"
            else:
                weather_data = {
                    "city": city.title(),
                    "temperature": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "condition": data["weather"][0]["description"],
                    "wind": data["wind"]["speed"],
                    "icon": data["weather"][0]["icon"],
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                # 📊 Forecast API
                forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
                forecast_data = requests.get(forecast_url).json()

                forecast_list = []
                for item in forecast_data["list"][:5]:
                    forecast_list.append({
                        "temp": item["main"]["temp"],
                        "time": item["dt_txt"]
                    })

                weather_data["forecast"] = forecast_list

                # 🔍 Save history
                with open("history.txt", "a") as file:
                    file.write(city + "\n")

        except:
            error = "Network error!"

    return render_template("index.html", weather=weather_data, error=error, history=history)


if __name__ == "__main__":
    app.run(debug=True)