import streamlit as st

st.set_page_config(page_title="Flight Sim Checklists", layout="centered")

st.title("Flight Sim Checklists")
st.write("FOR FLIGHT SIMULATION USE ONLY.")

# List of aircraft available in your app
aircraft_list = [
    "Cessna 172 Skyhawk",
    "Airbus A320neo",
    "Boeing 737-800",
    "Boeing 777-300ER"
]

# Create the dropdown menu in the sidebar
selected_aircraft = st.sidebar.selectbox(
    "Select Aircraft Type:",
    aircraft_list
)

checklist = st.selectbox(
    "Choose a checklist",
    ["Pre-flight", "Takeoff", "Climb", "Cruise", "Approach", "Landing"]
)

if checklist == "Pre-flight":
    st.header("Pre-flight Checklist")
    st.markdown("""
    - [ ] Master battery on
    - [ ] Avionics power on
    - [ ] Flight instruments set
    - [ ] Fuel quantity checked
    - [ ] Flight plan loaded
    """)
elif checklist == "Takeoff":
    st.header("Takeoff Checklist")
    st.markdown("""
    - [ ] Runway and departure briefed
    - [ ] Flaps set for takeoff
    - [ ] Transponder set
    - [ ] Lights on
    - [ ] Throttle smoothly to full power
    """)
elif checklist == "Climb":
    st.header("Climb Checklist")
    st.markdown("""
    - [ ] Positive rate of climb
    - [ ] Gear up
    - [ ] Climb power set
    - [ ] Airspeed alive
    """)
elif checklist == "Cruise":
    st.header("Cruise Checklist")
    st.markdown("""
    - [ ] Cruise power set
    - [ ] Fuel flow monitored
    - [ ] Navigation checked
    - [ ] Systems scanned
    """)
elif checklist == "Approach":
    st.header("Approach Checklist")
    st.markdown("""
    - [ ] Approach briefing complete
    - [ ] Altimeter set
    - [ ] Landing lights on
    - [ ] Gear and flaps configured
    """)
elif checklist == "Landing":
    st.header("Landing Checklist")
    st.markdown("""
    - [ ] On final approach
    - [ ] Airspeed stabilized
    - [ ] Flaps set
    - [ ] Touchdown zone targeted
    - [ ] Brakes ready
    """)