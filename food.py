import streamlit as st
import ollama

# 🎨 Background + sidebar styling
st.markdown(
    """
    <style>
    /* Main app background */
    .stApp {
        background-color: #E6E6FA; /* Lavender */
        color: #2c2c2c;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #AEC6CF; /* Pastel Blue */
        color: #1b1b1b; /* Dark text for contrast */
    }

    /* Headings */
    h1 {
        color: #4B0082; /* Indigo accent for headings */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🏠 Hero banner
st.markdown("""
# 🍳 AI Recipe & Food Assistant  
✨ Your smart cooking buddy — get recipes, nutrition info, and step-by-step cooking guidance! ✨
""")

# ⚙️ Sidebar settings
st.sidebar.header("⚙️ Settings")
diet = st.sidebar.selectbox("🥗 Choose diet type:", ["Any", "Vegetarian", "Vegan", "Keto"])
cuisine = st.sidebar.selectbox("🌍 Cuisine:", ["Any", "Indian", "Italian", "Chinese", "Mexican", "Korean"])
ingredients = st.text_input("📝 Enter ingredients you have:")

# 🚀 Generate recipe
if st.button("Get Recipe"):
    with st.spinner("Cooking up ideas..."):
        response = ollama.chat(
            model="llama3.2",
            messages=[{"role":"user","content":f"Suggest a {diet} {cuisine} recipe using {ingredients} with step-by-step instructions"}]
        )
    recipe_text = response["message"]["content"]

    st.success("👩‍🍳 Recipe Suggestion:")
    st.markdown(f"### {recipe_text}")

    # 🍎 Nutrition Info
    with st.spinner("Calculating nutrition info..."):
        nutrition = ollama.chat(
            model="llama3.2",
            messages=[{"role":"user","content":f"Give approximate nutrition info (calories, protein, carbs, fat) for this recipe: {recipe_text}"}]
        )
    st.info("🍎 Nutrition Information (approximate):")
    st.markdown(nutrition["message"]["content"])

    # 📖 Cooking Steps (text only)
    st.markdown("## 📖 Cooking Steps")
    steps = recipe_text.split("\n")
    for step in steps:
        if step.strip():
            st.markdown(f"- {step}")