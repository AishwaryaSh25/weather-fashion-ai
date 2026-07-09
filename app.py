import streamlit as st
from graph_builder import graph
st.set_page_config(
    page_title="AI Women's Weather & Occasion Stylist",
    page_icon="👠👜",
    layout="centered"
)
st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #FFF5F8;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #FFEFF5;
}

/* Headings */
h1, h2, h3 {
    color: #C2185B;
}

/* Normal text */
p, label, div {
    color: #5C3A4A;
}

/* Text input */
.stTextInput input {
    background-color: #FFFFFF;
    border: 2px solid #F8BBD0;
    border-radius: 12px;
    color: #5C3A4A;
}

/* Selectbox */
.stSelectbox div[data-baseweb="select"] {
    background-color: white;
    border-radius: 12px;
}

/* Button */
.stButton > button {
    background-color: #EC407A;
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    padding: 10px 25px;
}

.stButton > button:hover {
    background-color: #D81B60;
    color: white;
}

/* Success message */
.stSuccess {
    background-color: #FCE4EC;
    color: #880E4F;
}

/* Warning */
.stWarning {
    background-color: #FFF3E0;
}

/* Error */
.stError {
    background-color: #FFEBEE;
}

/* Spinner text */
.stSpinner {
    color: #C2185B;
}

</style>
""", unsafe_allow_html=True)

st.title("👠🌸 AI Women's Weather & Occasion Stylist")
st.write(
    "💖 Choose the perfect outfit"
    " that matches today's weather and your plans."
)
location = st.text_input(
   "Enter city and country",
    placeholder="Example: Noida, India"
)

occasion = st.selectbox(

    "Select Occasion",
    [
        "Office",
        "Party",
        "Wedding",
        "Gym",
        "College",
        "Casual"
    ]
)
if st.button("Get Recommendation"):
    if not location:
        st.warning(
            "Please enter a location."
        )
    else:
        with st.spinner(
            "Analyzing weather..."
        ):
         result = graph.invoke(
               {
                    "location": location,
                    "occasion": occasion
                }
            )

        
        if "error" in result:

            st.error(result["error"])

        else:

           
            st.success(
                "Recommendation generated!"
            )

       
            st.subheader("📍 Location")

            st.write(

                f"{result['weather_data']['city']}, "

                f"{result['weather_data']['country']}"
            )

          
            st.subheader("🌡 Weather")

            st.write(

                f"Temperature: "

                f"{result['weather_data']['temperature']} °C"
            )

            st.write(

                f"Condition: "

                f"{result['weather_data']['description']}"
            )

        
            st.subheader("🎯 Occasion")

            st.write(occasion)

           
            st.subheader(
                "👕 Recommended Outfit"
            )

            st.write(
                result["recommendation"]
            )
            