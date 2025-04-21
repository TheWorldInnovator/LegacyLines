import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

st.set_page_config(page_title="LegacyLines", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #1f1f2e;
        color: #f0f0f0;
    }
    .stApp {
        background: linear-gradient(135deg, #1f1f2e, #2c2c3a);
        color: #f0f0f0;
        font-family: 'Segoe UI', sans-serif;
    }
    h1, h2, h3, h4 {
        color: #ffa726;
    }
    .stButton>button {
        background-color: #ffa726;
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 8px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #fb8c00;
    }
    .stSelectbox, .stTextInput {
        background-color: #33334d !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #53354a);
        background-size: 400% 400%;
        animation: gradientMove 15s ease infinite;
        color: #f8f8f2;
        font-family: 'Segoe UI', sans-serif;
    }

    @keyframes gradientMove {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glowing title */
    h1 {
        color: #ff4da6;
        text-shadow: 0 0 10px #ff4da6, 0 0 20px #ff4da6, 0 0 30px #ff4da6;

        animation: pulseGlow 2s infinite;
    }

    @keyframes pulseGlow {
        0% { text-shadow: 0 0 5px #00ffe1; }
        50% { text-shadow: 0 0 20px #00ffe1; }
        100% { text-shadow: 0 0 5px #00ffe1; }
    }

    /* Button style */
    .stButton>button {
        background-color: #00ffe1;
        color: #0f0f0f;
        font-weight: bold;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        box-shadow: 0 0 15px #00ffe1;
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #0ff;
        box-shadow: 0 0 25px #0ff;
        transform: scale(1.05);
    }

    /* Dropdown customization */
    .stSelectbox, .stTextInput {
        background-color: #222644 !important;
        color: white !important;
        border-radius: 8px;
    }

    /* Smooth scroll for entire app */
    html {
        scroll-behavior: smooth;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    div[data-baseweb="select"] > div {
        transition: all 0.3s ease-in-out;
        border: 2px solid #39ff14;
        box-shadow: 0 0 10px #39ff14;
        border-radius: 10px;
    }
    div[data-baseweb="select"]:hover > div {
        transform: scale(1.02);
        box-shadow: 0 0 20px #39ff14;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 Explore Famous Oral Histories")
st.markdown("Select a country to discover one of its most well-known oral history stories.")

countries = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo (Brazzaville)", "Congo (Kinshasa)", "Costa Rica", "Croatia",
    "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica",
    "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada",
    "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras",
    "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya",
    "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
    "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
    "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
    "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain",
    "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan",
    "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
    "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
    "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen",
    "Zambia", "Zimbabwe"] 

country = st.selectbox("🌐 Choose a country", countries)

if st.button("🔍 Show me an oral history"):
    st.subheader(f"Famous Oral History from {country}")
    with st.spinner("Fetching story..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert in global oral traditions, anthropology, and folklore. "
                            "Provide a detailed and culturally accurate account of the most famous oral history or folklore from "
                            f"{country}. Include the background, characters (if any), and the cultural significance or moral behind the story. "
                            "Make it vivid and engaging, as if you were telling it to someone hearing it for the first time."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"What is the most famous oral history from {country}?"
                    }
                ],
                temperature=1,
                max_tokens=4096,
                top_p=1
            )
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error fetching story: {e}")

st.markdown("---")
st.caption("© 2025 LegacyLines. All rights reserved.")
