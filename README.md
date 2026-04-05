# 🌦 Weather App (Flask)

A modern, feature-rich weather application built using **Python Flask**, **OpenWeather API**, and **Chart.js**.  
This project includes real-time weather, animations, history tracking, and a beautiful UI with dark/light mode.

---

## 🚀 Live Demo
👉 Add your deployed Render link here  
Example:  
https://your-app.onrender.com

---

## 📸 Features

✅ Real-time weather search (by city)  
✅ Auto location weather detection  
✅ 5-day weather forecast  
✅ Temperature chart (Chart.js)  
✅ Weather animations (rain, clouds, clear sky)  
✅ Dark / Light mode toggle 🌙  
✅ Recent search history (last 10 cities)  
✅ Hover effects on buttons & cards  
✅ Stylish UI with responsive design  
✅ Weather icons from OpenWeather  

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, Bootstrap, JavaScript  
- **Backend:** Python (Flask)  
- **API:** OpenWeather API  
- **Charts:** Chart.js  
- **Deployment:** Render  

---

## 📂 Project Structure

```
weather-app/
│── app.py
│── requirements.txt
│── history.txt
│── templates/
│   └── index.html
│── static/
│   └── style.css
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/weather-app.git
cd weather-app
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add your API key

In `app.py`:

```python
API_KEY = "YOUR_OPENWEATHER_API_KEY"
```

👉 Get API key from:  
https://openweathermap.org/api

---

### 5. Run the app

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment (Render)

1. Push code to GitHub  
2. Go to 👉 Render  
3. Click **New Web Service**  
4. Connect your GitHub repo  
5. Set:

```
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
```

6. Click **Deploy**

---

## 📊 Features Explained

### 🌡 Weather Data
- Temperature  
- Feels like  
- Humidity  
- Wind speed  
- Weather condition  

---

### 📈 Chart
- Displays temperature trend using Chart.js  

---

### 🌦 Animations
- Rain animation for rainy weather  
- Cloud & clear sky effects  
- Smooth UI transitions  

---

### 🌙 Dark Mode
- Toggle button at top-right  
- Changes UI theme dynamically  

---

### 🔍 History Feature
- Stores last 10 searched cities  
- Click to quickly reload weather  

---

## 🧠 Future Improvements

- 🌍 Auto-location weather (fully integrated UI)  
- ⭐ Favorite cities system  
- 🗄 Database instead of file storage  
- 📱 Mobile app version  
- 📊 Advanced analytics charts  

---

## ⚠️ Important Notes

Make sure `requirements.txt` includes:

```
Flask
requests
gunicorn
Flask-SQLAlchemy
```

---

## 👨‍💻 Author

**Mayur Nikhare**

---

## ⭐ If you like this project

Give a ⭐ on GitHub and feel free to contribute!
