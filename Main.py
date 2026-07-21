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

# --- MAIN PAGE: Display Checklists ---
st.title(f"{selected_aircraft} Checklist")
st.subheader(f"Phase: {checklist_phase}")

# Example conditional logic to load specific checklists
if selected_aircraft == "Cessna 172 Skyhawk":
    if checklist_phase == "Pre-flight":
        st.checkbox("Control Wheel Lock - REMOVE")
        st.checkbox("Ignition Switch - OFF")
        st.checkbox("Master Switch - ON")
        st.checkbox("Fuel Quantity Indicators - CHECK")
    elif checklist_phase == "Before Takeoff":
        st.checkbox("Flight Controls - FREE & CORRECT")
        st.checkbox("Flight Instruments - CHECK & SET")
        st.checkbox("Fuel Selector Valve - BOTH")

elif selected_aircraft == "Airbus A320neo":
    if checklist_phase == "Pre-flight":
        st.checkbox("Batteries 1 & 2 - AUTO / ON")
        st.checkbox("External Power - ON (if available)")
        st.checkbox("APU Bleed - ON")
    elif checklist_phase == "Before Takeoff":
        st.checkbox("Flaps - SET FOR TAKEOFF")
        st.checkbox("Pitch Trim - SET")
        st.checkbox("ECAM Memo - TO NO BLUE")

    st.info(f"Currently displaying **{checklist_phase}** items for the **{selected_aircraft}**.")