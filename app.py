from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

API_KEY = "e7cde81c3a0cb242fe3960680cb1b8ea"


# 📦 DB Model
class SearchHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


# 📍 Location API
@app.route("/location")
def location():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    return jsonify(requests.get(url).json())


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        try:
            # 🌦 Current weather
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            res = requests.get(url)
            data = res.json()

            if res.status_code != 200:
                error = "City not found!"
            else:
                weather_data = {
                    "city": city.title(),
                    "temperature": data["main"]["temp"],
                    "feels_like": data["main"]["feels_like"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "condition": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                # 📊 Forecast
                forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
                forecast_data = requests.get(forecast_url).json()

                forecast_list = []

                for item in forecast_data["list"][::8]:  # 5 days
                    forecast_list.append({
                        "temp": item["main"]["temp"],
                        "time": item["dt_txt"].split(" ")[0]
                    })

                weather_data["forecast"] = forecast_list

                # ⭐ Save history
                db.session.add(SearchHistory(city=city.title()))
                db.session.commit()

        except:
            error = "Something went wrong!"

    history = SearchHistory.query.order_by(SearchHistory.timestamp.desc()).limit(10).all()

    return render_template("index.html", weather=weather_data, error=error, history=history)


if __name__ == "__main__":
    app.run(debug=True)