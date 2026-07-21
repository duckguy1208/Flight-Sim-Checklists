import streamlit as st

st.set_page_config(page_title="Flight Sim Checklists", layout="centered")

st.title("Flight Sim Checklists")
st.write("FOR FLIGHT SIMULATION USE ONLY.")

# List of aircraft available in your app
aircraft_list = [
    "Airbus A320",
    "Airbus A330",
    "Airbus A340",
    "Airbus A350",
    "Airbus A380",
    "Boeing 737 NG",
    "Boeing 737 MAX",
    "Boeing 777"
]

# Create the dropdown menu in the sidebar
selected_aircraft = st.sidebar.selectbox(
    "Select Aircraft Type:",
    aircraft_list
)

checklist_phase = st.sidebar.radio(
    "Flight Phase:",
    ["Pre-flight", "Before Taxi", "Taxi", "Before Takeoff", "Takeoff", "Descent", "Landing", "Shutdown", "Securing Aircraft"]
)

if checklist_phase == "Pre-flight":
    st.header("Pre-flight Checklist")
    st.markdown("""
    - [ ] Master battery on
    - [ ] Avionics power on
    - [ ] Flight instruments set
    - [ ] Fuel quantity checked
    - [ ] Flight plan loaded
    """)
elif checklist_phase == "Takeoff":
    st.header("Takeoff Checklist")
    st.markdown("""
    - [ ] Runway and departure briefed
    - [ ] Flaps set for takeoff
    - [ ] Transponder set
    - [ ] Lights on
    - [ ] Throttle smoothly to full power
    """)
elif checklist_phase == "Climb":
    st.header("Climb Checklist")
    st.markdown("""
    - [ ] Positive rate of climb
    - [ ] Gear up
    - [ ] Climb power set
    - [ ] Airspeed alive
    """)
elif checklist_phase == "Cruise":
    st.header("Cruise Checklist")
    st.markdown("""
    - [ ] Cruise power set
    - [ ] Fuel flow monitored
    - [ ] Navigation checked
    - [ ] Systems scanned
    """)
elif checklist_phase == "Approach":
    st.header("Approach Checklist")
    st.markdown("""
    - [ ] Approach briefing complete
    - [ ] Altimeter set
    - [ ] Landing lights on
    - [ ] Gear and flaps configured
    """)
elif checklist_phase == "Landing":
    st.header("Landing Checklist")
    st.markdown("""
    - [ ] On final approach
    - [ ] Airspeed stabilized
    - [ ] Flaps set
    - [ ] Touchdown zone targeted
    - [ ] Brakes ready
    """)