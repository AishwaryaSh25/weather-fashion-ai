import streamlit as st
from graph_builder import graph
st.set_page_config(
    page_title="AI Weather Fashion Stylist",
    page_icon="👟🧥",
    layout="centered"
)
st.title("👟🧥 AI Weather Fashion Stylist")
st.write(
    "Get clothing recommendations "
    "based on weather and occasion."
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
            