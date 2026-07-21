import streamlit as st
from Checklists import AIRCRAFT_CHECKLISTS

st.set_page_config(page_title="Flight Sim Checklists", layout="centered")

st.title("Flight Sim Checklists")
st.write("FOR FLIGHT SIMULATION USE ONLY.")

# List of aircraft available in your app
available_aircraft = list(AIRCRAFT_CHECKLISTS.keys())
# Create the dropdown menu in the sidebar
selected_aircraft = st.sidebar.selectbox(
    "Select Aircraft Type:",
    list(AIRCRAFT_CHECKLISTS.keys())
)

checklist_phase = st.sidebar.radio(
    "Flight Phase:",
    ["Pre-flight", "Before Taxi", "Taxi", "Before Takeoff", "Climbout", "Descent", "Landing", "After Landing", "Parking", "Securing Aircraft"]
)


# --- MAIN PAGE: Display Checklists ---
st.title(f"{selected_aircraft} Checklist")
st.subheader(f"Phase: {checklist_phase}")

# Fetch items safely using .get()
aircraft_data = AIRCRAFT_CHECKLISTS.get(selected_aircraft, {})
items = aircraft_data.get(checklist_phase, [])

if items:
    # Dynamically render checkboxes for each item found
    for index, item in enumerate(items):
        # Create a unique key for Streamlit state tracking
        item_key = f"{selected_aircraft}_{checklist_phase}_{index}"
        st.checkbox(item, key=item_key)
else:
    st.info(f"No checklist items currently available for **{selected_aircraft}** during **{checklist_phase}**.")

st.info(f"Currently displaying **{checklist_phase}** items for the **{selected_aircraft}**.")

