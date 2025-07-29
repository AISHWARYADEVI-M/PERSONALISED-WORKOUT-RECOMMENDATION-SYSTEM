import streamlit as st
import sqlite3
import os

DB_PATH = "workout_db.sqlite"

# --------------------- DB Init Function ---------------------
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        # Check if users table exists
        cursor.execute("""
            SELECT name FROM sqlite_master WHERE type='table' AND name='users';
        """)
        result = cursor.fetchone()
        if not result:
            cursor.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER,
                    gender TEXT,
                    height REAL,
                    weight REAL,
                    fitness_level TEXT,
                    activity_level TEXT,
                    goal TEXT,
                    workout_duration INTEGER,
                    bmi REAL,
                    calorie_target INTEGER
                )
            """)
            conn.commit()
            print("✅ 'users' table created.")
        else:
            print("ℹ️ 'users' table already exists.")

def save_user_to_db(name, age, gender, height, weight, fitness_level, activity_level, goal, duration, bmi, calories):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (
                name, age, gender, height, weight, fitness_level,
                activity_level, goal, workout_duration, bmi, calorie_target
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            name, age, gender, height, weight, fitness_level,
            activity_level, goal, duration, bmi, calories
        ))
        conn.commit()

# ------------------------------------------------------------

def main():
    init_db()  # Ensure DB and table are ready
    st.set_page_config(page_title="Personalized Workout Recommender", layout="wide")
    
    # Title and Description
    st.title("🏋️‍♂️ Personalized Workout Recommendation System")
    st.write("Enter your details below to get a personalized workout plan tailored to your needs!")
    
    # User Input Form
    with st.form("user_input_form"):
        username = st.text_input("Name", max_chars=20)
        age = st.number_input("Age", min_value=10, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
        weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
        fitness_level = st.selectbox("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
        goal = st.selectbox("Workout Goal", ["Weight Loss", "Muscle Gain", "Endurance", "Flexibility"])
        workout_duration = st.slider("Preferred Workout Duration (minutes)", 10, 120, 30)
        submit_button = st.form_submit_button("Get Recommendations")
    
    if username:
        st.subheader(f"Welcome, {username}!")
    
    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"Your BMI: {bmi:.2f}")
    
    # Calculate daily calorie burn target dynamically
    if goal == "Weight Loss":
        calorie_deficit = int(weight * 22)
    elif goal == "Muscle Gain":
        calorie_deficit = int(weight * 18)
    elif goal == "Endurance":
        calorie_deficit = int(weight * 20)
    else:
        calorie_deficit = int(weight * 19)
    
    st.subheader(f"🔥 {username}, you should aim to burn {calorie_deficit} kcal per day to reach your goal.")
    
    # Save to database
    if submit_button:
        try:
            save_user_to_db(username, age, gender, height, weight, fitness_level, activity_level, goal, workout_duration, bmi, calorie_deficit)
            st.success("✅ Your data has been saved to the database!")
        except Exception as e:
            st.error(f"❌ Error saving to database: {e}")

        # Workout Recommendations
        st.subheader("🔥 Recommended Workouts for You:")
        
        if goal == "Weight Loss":
            st.write("✅ HIIT Cardio - 30 mins (~300-400 kcal burned)")
            st.write("✅ Jump Rope - 20 mins (~250 kcal burned)")
            st.write("✅ Calisthenics Routine - 45 mins (~350 kcal burned)")
        elif goal == "Muscle Gain":
            st.write("✅ Strength Training - 45 mins (~200-400 kcal burned)")
            st.write("✅ Progressive Overload Routine")
            st.write("✅ Compound Lifts (Squats, Deadlifts, Bench Press)")
        elif goal == "Endurance":
            st.write("✅ Long Distance Running - 60 mins (~600 kcal burned)")
            st.write("✅ Rowing Machine - 40 mins (~450 kcal burned)")
            st.write("✅ Cycling - 45 mins (~500 kcal burned)")
        elif goal == "Flexibility":
            st.write("✅ Yoga - 30 mins (~150 kcal burned)")
            st.write("✅ Dynamic Stretching - 20 mins (~100 kcal burned)")
            st.write("✅ Pilates - 40 mins (~200 kcal burned)")

        # Progress Tracker
        st.subheader("📊 Track Your Progress")
        st.write("Log your workouts and track your improvements over time! (Feature in Development)")

        # Diet Recommendations
        st.subheader("🥗 Suggested Diet Plan")
        if goal == "Weight Loss":
            st.write("✅ **High Protein, Low Carb Diet**")
            st.write("• Protein: **150g** | Carbs: **100g** | Fats: **50g**")
            st.write("• Foods: Lean meat, fish, eggs, leafy greens, nuts")
            st.write("• Avoid processed foods and sugary drinks")
        elif goal == "Muscle Gain":
            st.write("✅ **High Protein, High Carb Diet**")
            st.write("• Protein: **200g** | Carbs: **250g** | Fats: **60g**")
            st.write("• Foods: Chicken, brown rice, sweet potatoes, dairy")
            st.write("• Eat frequent meals, consider protein shakes")
        elif goal == "Endurance":
            st.write("✅ **Balanced Diet with Complex Carbs**")
            st.write("• Protein: **140g** | Carbs: **180g** | Fats: **50g**")
            st.write("• Foods: Bananas, nuts, whole grains, lean meats")
            st.write("• Hydration and electrolytes are key")
        elif goal == "Flexibility":
            st.write("✅ **Anti-Inflammatory Diet with Omega-3s**")
            st.write("• Protein: **130g** | Carbs: **120g** | Fats: **50g**")
            st.write("• Foods: Green leafy vegetables, berries, nuts, fatty fish")


if __name__ == "__main__":
    main()
