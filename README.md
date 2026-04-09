# 🏋️‍♂️ Personalized Workout Recommendation System

## 📌 Project Overview
This project is a web-based fitness application that provides personalized workout and diet recommendations based on user input.  

Built using Streamlit, the system collects user details such as age, gender, height, weight, fitness level, and goals to generate customized workout plans and calorie targets.

User data is stored using SQLite, enabling basic tracking and future scalability for progress monitoring.

---

## 🎯 Objective
- Provide personalized workout recommendations  
- Calculate BMI and daily calorie targets  
- Suggest diet plans based on fitness goals  
- Store user data for tracking and analysis  

---

## 🛠 Tools & Technologies
- **Python** – Core programming  
- **Streamlit** – Web application framework  
- **SQLite** – Database for storing user data  
- **NumPy** – Calculations (BMI, calories)  

---

## ✨ Features
- 🧾 User input form (age, height, weight, etc.)  
- 📊 Automatic BMI calculation  
- 🔥 Daily calorie burn target estimation  
- 🏋️ Personalized workout recommendations  
- 🥗 Goal-based diet plans  
- 💾 Data storage using SQLite database  
- 📈 Future-ready progress tracking feature  

---

## 🚀 How It Works
1. User enters personal and fitness details  
2. System calculates BMI  
3. Based on fitness goal:
   - Calorie target is generated  
   - Workout plan is recommended  
   - Diet plan is suggested  
4. User data is saved into the database  
5. Results are displayed in an interactive UI  

---

## 📁 Project Structure
- `app.py` – Main Streamlit application  
- `workout_db.sqlite` – SQLite database  
- `requirements.txt` – Dependencies  

---

## 💻 Installation

```bash
git clone https://github.com/your-username/workout-recommender.git
cd workout-recommender
pip install -r requirements.txt
```

---

## ▶️ Usage

```bash
streamlit run app.py
```

### Steps:
- Enter your personal details  
- Select your fitness goal  
- Click **Get Recommendations**  
- View your workout and diet plan  

---

## 📊 Example

**Input:**
- Age: 25  
- Weight: 70 kg  
- Height: 170 cm  
- Goal: Weight Loss  

**Output:**
- BMI: 24.22  
- Calorie Target: ~1540 kcal/day  
- Workouts: HIIT, Jump Rope, Calisthenics  
- Diet: High protein, low carb  

---

## 📌 Workout Categories

### Weight Loss
- HIIT Cardio  
- Jump Rope  
- Calisthenics  

### Muscle Gain
- Strength Training  
- Compound Exercises  
- Progressive Overload  

### Endurance
- Running  
- Cycling  
- Rowing  

### Flexibility
- Yoga  
- Stretching  
- Pilates  

---

## 🥗 Diet Recommendations
- **Weight Loss:** High protein, low carb  
- **Muscle Gain:** High protein, high carb  
- **Endurance:** Balanced diet  
- **Flexibility:** Anti-inflammatory diet  

---

## 📌 Applications
- Fitness tracking systems  
- Personal health assistants  
- Gym and wellness apps  
- Beginner fitness guidance tools  

---

## ⚠️ Limitations
- No real-time progress tracking yet  
- Diet plans are generalized  
- No integration with wearable devices  

---

## 🔮 Future Enhancements
- 📈 Progress tracking dashboard  
- 📱 Mobile app integration  
- ⌚ Wearable device support  
- 🤖 AI-based adaptive workout plans  
- 📊 Advanced analytics & visualization  

---

## 📌 Disclaimer
This application provides general fitness recommendations.  
Consult a healthcare or fitness professional before starting any workout or diet plan.
