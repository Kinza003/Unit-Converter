import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Custom css for styling
st.markdown("""
    <style>
        /* Centering Content */
        .main {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
            
        /* Sttling for select boxes and input fields */ 
        .stSelectbox, .stTextInput {
            border-radius: 10px;
            padding: 10px;
            font-size: 16px;
            border: 2px solid #3498db;
            background-color: #f9f9f9;
            color: #333;
        }
            
        /* Styling for button */
        /* Styling for button */
        div.stButton > button {
            background-color: #3498db !important; /* Blue */
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            transition: 0.3s ease-in-out !important;
            border: none !important;
            cursor: pointer !important;
        }

        /* Button hover effect */
        div.stButton > button:hover {
            background-color: red !important;
            color: white !important;
            transform: scale(1.05) !important;
        }
            
        /* Styling for success message */
            .stAlert {
            font-size: 18px;
            font-weight: bold;
            color: #2ecc71;
        
        }
            
        /* Styling for error message */
        .stError {
            font-size: 18px;
            font-weight: bold;
            color: #e74c3c;
        }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='text-align: center; color: #3498db;'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

st.markdown("""
    <h3 style='text-align: center; color: #2c3e50; font-size: 22px; font-weight: bold;'>
        🔥 Convert units instantly & effortlessly! 🚀
    </h3>
""", unsafe_allow_html=True)

# Dictionary of unit types
unit_category = {
    "Length" : ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Yard", "Mile"],
    "Weight" : ["Kilogram", "Gram", "Pound", "Ounce", "Ton"],
    "Temperature" : ["Celsius", "Fahrenheit", "Kelvin"], 
    "Volume" : ["Liter", "Milliliter", "Cubic Meter", "Gallon"],
    "Force" : ["Newton", "Dyne", "Pound-Force"],
    "Energy" : ["Joule", "Kilojoule", "Calorie", "Kilocalorie", "Watt-hour"]
}

#  Main drop down for type selection
category = st.selectbox("Select Unit category", list(unit_category.keys()))

# Sub drop down for unit selection (dependent on type selection)
from_unit = st.selectbox("From", unit_category[category])
to_unit = st.selectbox("To", unit_category[category])

#  Conversion Function
def convert_units (value, category, from_unit, to_unit):
    try:
        value = float(value)  # Convert input to a number (type casting)

        # Conversion factor for differnt categories
        conversion_factors = {
            # Length
            "Length" : {
                "Meter" : 1,
                "Centimeter" : 100,
                "Millimeter" : 1000,
                "Kilometer" : 0.001,
                "Inch" : 39.3701,
                "Foot" : 3.28084,
                "Yard" : 1.09361,
                "Mile": 0.000621371
            },

            # Weight
            "Weight" : {
                "Kilogram" : 1,
                "Gram" : 1000,
                "Pound" : 2.20462,
                "Ounce" : 35.274,
                "Ton" : 0.001
            },

            # Temperature
            "Temperature" : {
                "Celsius" : lambda x: x,
                "Fahrenheit" : lambda x: (x - 32) * 5/9,
                "Kelvin" : lambda x: x - 273.15
            },

            # Volume
            "Volume" : {
                "Liter" : 1,
                "Milliliter" : 1000,
                "Cubic Meter" : 0.001,
                "Gallon" : 0.264172
            },

            # Force
            "Force" : {
                "Newton" : 1,
                "Dyne" : 100000,
                "Pound-Force" : 0.224809
            },

            # Energy
            "Energy" : {
                "Joule" : 1,
                "Kilojoule" : 0.001, 
                "Calorie" : 0.239006,
                "Kilocalorie" : 0.000239006,
                "Watt-hour" : 0.000277778
            }
        }


        # Handle Temperature Separately (Since it's not a direct factor conversion)
        if (category == "Temperature"):
            if (from_unit == "Celsius" and to_unit == "Fahrenheit"):
                return (value * 9/5) + 32
            elif (from_unit == "Celsius" and to_unit == "Kelvin"):
                return value + 273.15
            elif (from_unit == "Fahrenheit" and to_unit == "Celsius"):
                return (value - 32) * 5/9
            elif (from_unit == "Fahrenheit" and to_unit == "Kelvin"):
                return (value - 32) * 5/9 + 273.15
            elif (from_unit == "Kelvin" and to_unit == "Celsius"):
                return value - 273.15
            elif (from_unit == "Kelvin" and to_unit == "Fahrenheit"):
                return (value - 273.15) * 9/5 + 32
            else:
                return value  # Same unit conversion
            
            # General Unit Conversion
        if from_unit in conversion_factors[category] and to_unit in conversion_factors[category]:
            from_factor = conversion_factors[category][from_unit]  
            to_factor = conversion_factors[category][to_unit]  
            return value * (to_factor / from_factor)  # Fixed formula

        return None  # Invalid conversion

    except ValueError:
        return None  # Invalid input
    

# Input field for value
value = st.text_input("🔢 Enter value to convert...", "1")


#  Button to convert
if st.button ("🔄 Convert"):
    result = convert_units(value, category, from_unit, to_unit)
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result: .2f} {to_unit}")
    else:
        st.error("⚠️ Invalid conversion or input")
