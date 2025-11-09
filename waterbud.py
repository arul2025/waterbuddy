import streamlit as st

st.set_page_config(page_title="WaterBuddy 💧", page_icon="💧", layout="centered")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f7fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("💧 WaterBuddy — Stay Hydrated!")

# --- 1️⃣ Age-based standard goals ---
AGE_GOALS = {
    "Children (4–8)": 1200,
    "Teens (9–13)": 1700,
    "Adults (14–64)": 2200,
    "Seniors (65+)": 1800
}

# --- 2️⃣ User input ---
age_group = st.selectbox("Select your age group:", list(AGE_GOALS.keys()))
default_goal = AGE_GOALS[age_group]
goal = st.number_input("Set your daily goal (ml):", min_value=500, max_value=4000, value=default_goal, step=100)

# --- 3️⃣ Log water intake ---
if "total" not in st.session_state:
    st.session_state.total = 0

st.write(f"### Today's total: {st.session_state.total} ml / {goal} ml")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("+250 ml"):
        st.session_state.total += 250
with col2:
    if st.button("+500 ml"):
        st.session_state.total += 500
with col3:
    if st.button("Reset (New Day)"):
        st.session_state.total = 0

# --- 4️⃣ Progress & feedback ---
progress = min(st.session_state.total / goal, 1.0)
st.progress(progress)

percent = progress * 100
st.write(f"**Progress: {percent:.1f}%**")

# Motivational messages
if percent < 50:
    st.info("💧 Keep sipping! Hydration boosts your energy.")
elif percent < 75:
    st.success("👏 Great job! You’re staying hydrated.")
elif percent < 100:
    st.success("🌊 Almost there! Just a few more sips.")
else:
    st.balloons()
    st.success("🎉 Goal achieved! You’re fully hydrated today!")

# --- 5️⃣ Optional hydration tip ---
tips = [
    "Drink a glass before each meal.",
    "Keep a bottle on your desk.",
    "Add lemon or mint to make water more fun.",
    "Start your day with a glass of water."
]
import random
st.caption(f"💡 Tip: {random.choice(tips)}")
