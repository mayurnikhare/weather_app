# 🌦 Weather App (Flask Full Stack)

A responsive weather web application built using Flask that fetches real-time weather data from the OpenWeatherMap API. The app allows users to search for any city, view current weather conditions, and check a short-term forecast with a clean and user-friendly interface.

---

## 🚀 Features

* 🌍 Real-time weather data by city name
* 📊 5-day weather forecast
* 🔍 Search history (last 10 searches)
* 🖱 Clickable history for quick search
* 🎨 Responsive UI using Bootstrap
* ⚠️ Error handling for invalid inputs

---

## 🛠 Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, Bootstrap
* **API:** OpenWeatherMap API
* **Others:** Requests, JSON handling

---

## 📂 Project Structure

```
weather_app/
│
├── app.py
├── history.txt
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/mayurnikhare/weather_app.git
cd weather_app
```

### 2️⃣ Install Dependencies

```bash
pip install flask requests
```

### 3️⃣ Add API Key

Open `app.py` and replace:

```python
API_KEY = "e7cde81c3a0cb242fe3960680cb1b8ea"
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000/

---

## 🔮 Future Improvements

* 📍 Auto-detect user location
* 🌙 Dark mode toggle
* 📊 Graphs for temperature trends
* 🗄 Database integration (SQLite)
* 🌐 Deploy live on cloud

---

## 👨‍💻 Author

**Mayur Nikhare**

---

## ⭐ Contributing

Feel free to fork this project and improve it. Contributions are welcome!

---

## 📜 License

This project is open-source and available under the MIT License.
