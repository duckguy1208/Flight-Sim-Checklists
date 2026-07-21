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

if selected_aircraft == "Airbus A320":
    if checklist_phase == "Pre-flight":
        st.checkbox("Parking Brake - ON", key="a320_pf_1")
        st.checkbox("Batteries 1 & 2 - AUTO / ON", key="a320_pf_2")
        st.checkbox("External Power - ON (if available)", key="a320_pf_3")
        st.checkbox("APU MASTER - ON", key="a320_pf_4")
        st.checkbox("APU BLEED - ON", key="a320_pf_5")
        st.checkbox("ADIRS (1, 2, 3) - NAV", key="a320_pf_6")
        st.checkbox("Exterior Lights - NAV / LOGO ON", key="a320_pf_7")
        st.checkbox("MCDU / Flight Plan - SET & INITIALIZED", key="a320_pf_8")

    elif checklist_phase == "Before Taxi":
        st.checkbox("APU BLEED - OFF", key="a320_bt_1")
        st.checkbox("Engine Mode Selector - IGN/START", key="a320_bt_2")
        st.checkbox("Engine 2 Master Switch - ON", key="a320_bt_3")
        st.checkbox("Engine 1 Master Switch - ON", key="a320_bt_4")
        st.checkbox("Engine Mode Selector - NORMAL", key="a320_bt_5")
        st.checkbox("Status / ECAM - CHECKED (NO BLUE)", key="a320_bt_6")
        st.checkbox("Flight Controls - CHECK (FULL FREE)", key="a320_bt_7")

    elif checklist_phase == "Taxi":
        st.checkbox("Nose Light - TAXI", key="a320_tx_1")
        st.checkbox("Auto Brake - MAX", key="a320_tx_2")
        st.checkbox("Flaps - SET FOR TAKEOFF", key="a320_tx_3")
        st.checkbox("Pitch Trim - SET FOR TAKEOFF", key="a320_tx_4")
        st.checkbox("Cabin Crew - ADVISED", key="a320_tx_5")
        st.checkbox("Radar / PWS - ON / AUTO", key="a320_tx_6")

    elif checklist_phase == "Before Takeoff":
        st.checkbox("Brake Temp - CHECK", key="a320_bto_1")
        st.checkbox("Approach Path - CLEAR", key="a320_bto_2")
        st.checkbox("Landing Lights - ON", key="a320_bto_3")
        st.checkbox("Strobe Lights - ON", key="a320_bto_4")
        st.checkbox("Nose Light - TO", key="a320_bto_5")
        st.checkbox("TCAS - TA/RA", key="a320_bto_6")
        st.checkbox("ECAM MEMO - TO NO BLUE", key="a320_bto_7")

    elif checklist_phase == "Takeoff":
        st.checkbox("Thrust Levers - FLEX or TOGA", key="a320_to_1")
        st.checkbox("Airspeed - ALIVE / CHECKED", key="a320_to_2")
        st.checkbox("Rotate (Vr) - PITCH UP 15°", key="a320_to_3")
        st.checkbox("Positive Climb - GEAR UP", key="a320_to_4")
        st.checkbox("Autopilot 1 - ENGAGE (Above 100 ft)", key="a320_to_5")
        st.checkbox("Flaps - RETRACT (At S Speed)", key="a320_to_6")

    elif checklist_phase == "Descent":
        st.checkbox("MCDU Performance Page - ENTER ARRIVAL DATA", key="a320_des_1")
        st.checkbox("Barometric Pressure - SET & CROSSCHECK", key="a320_des_2")
        st.checkbox("Landing Elevation - AUTO", key="a320_des_3")
        st.checkbox("Auto Brake - SET (LOW / MED)", key="a320_des_4")
        st.checkbox("Approach Phase - ACTIVATE", key="a320_des_5")

    elif checklist_phase == "Landing":
        st.checkbox("Cabin Crew - REPORTED READY", key="a320_ldg_1")
        st.checkbox("Landing Lights - ON", key="a320_ldg_2")
        st.checkbox("Flaps - FULL (or CONF 3)", key="a320_ldg_3")
        st.checkbox("Gear - DOWN (3 GREEN)", key="a320_ldg_4")
        st.checkbox("ECAM MEMO - LANDING NO BLUE", key="a320_ldg_5")
        st.checkbox("Sliding Tables - STOWED", key="a320_ldg_6")

    elif checklist_phase == "Shutdown":
        st.checkbox("Parking Brake - ON", key="a320_sd_1")
        st.checkbox("Engine Master 1 & 2 - OFF", key="a320_sd_2")
        st.checkbox("Seat Belts Sign - OFF", key="a320_sd_3")
        st.checkbox("External Power / APU - ON / CONNECTED", key="a320_sd_4")
        st.checkbox("Fuel Pumps - OFF", key="a320_sd_5")
        st.checkbox("Beacon Light - OFF", key="a320_sd_6")

    elif checklist_phase == "Securing Aircraft":
        st.checkbox("Oxygen Crew Supply - OFF", key="a320_sec_1")
        st.checkbox("ADIRS (1, 2, 3) - OFF", key="a320_sec_2")
        st.checkbox("APU BLEED - OFF", key="a320_sec_3")
        st.checkbox("APU MASTER - OFF", key="a320_sec_4")
        st.checkbox("Exterior Lights - OFF", key="a320_sec_5")
        st.checkbox("Batteries 1 & 2 - OFF", key="a320_sec_6")

elif selected_aircraft == "Airbus A330":
    if checklist_phase == "Pre-flight":
        st.checkbox("Batteries 1 & 2 - AUTO / ON", key="a330_pf_1")
        st.checkbox("External Power - ON (if available)", key="a330_pf_2")
        st.checkbox("APU Bleed - ON", key="a330_pf_3")
    elif checklist_phase == "Before Takeoff":
        st.checkbox("Flaps - SET FOR TAKEOFF", key="a330_bto_1")
        st.checkbox("Pitch Trim - SET", key="a330_bto_2")
        st.checkbox("ECAM Memo - TO NO BLUE", key="a330_bto_3")

st.info(f"Currently displaying **{checklist_phase}** items for the **{selected_aircraft}**.")


'''
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
 
 if selected_aircraft == "Airbus A320":
    if checklist_phase == "Pre-flight":
        st.checkbox("Batteries 1 & 2 - AUTO / ON")
        st.checkbox("External Power - ON (if available)")
        st.checkbox("APU Bleed - ON")
    elif checklist_phase == "Before Takeoff":
        st.checkbox("Flaps - SET FOR TAKEOFF")
        st.checkbox("Pitch Trim - SET")
        st.checkbox("ECAM Memo - TO NO BLUE")

elif selected_aircraft == "Airbus A330":
    if checklist_phase == "Pre-flight":
        st.checkbox("Batteries 1 & 2 - AUTO / ON")
        st.checkbox("External Power - ON (if available)")
        st.checkbox("APU Bleed - ON")
    elif checklist_phase == "Before Takeoff":
        st.checkbox("Flaps - SET FOR TAKEOFF")
        st.checkbox("Pitch Trim - SET")
        st.checkbox("ECAM Memo - TO NO BLUE")

    st.info(f"Currently displaying **{checklist_phase}** items for the **{selected_aircraft}**.")
'''