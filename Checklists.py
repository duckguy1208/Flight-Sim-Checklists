# checklists.py

AIRCRAFT_CHECKLISTS = {
    "Airbus A320": {
        "Pre-flight": [
            "Parking Brake — ON",
            "Batteries 1 & 2 — AUTO / ON (Check > 25.5V)",
            "External Power — ON (if available)",
            "ADIRS 1, 2, 3 — NAV",
            "APU MASTER — ON",
            "APU BLEED — ON",
            "Exterior Lights — NAV & LOGO ON",
            "Cockpit Lights — AS REQUIRED",
            "Crew Oxygen Supply — ON",
            "Flaps Lever — CHECK RETRACTED",
            "Engine Masters 1 & 2 — OFF",
            "Engine Mode Selector — NORMAL",
            "Thrust Levers — IDLE",
            "MCDU / Flight Plan — SET & CHECK",
        ],
        "Before Taxi": [
            "Engine Mode Selector — IGN/START",
            "Engine 2 Master Switch — ON",
            "Engine 1 Master Switch — ON",
            "Engine Mode Selector — NORM At 19% N1",
            "APU MASTER — OFF (as required)",
            "ANTI-ICE / WING — (as required)",
            "Status / ECAM — CHECKED (NO BLUE)",
            "Flight Controls — CHECK (FULL FREE)",
            "Pitch Trim — SET FOR TAKEOFF",
            "Rudder Trim — RESET ZERO",
            "Flaps — SET FOR TAKEOFF"
        ],
        "Taxi": [
            "Nose Light — TAXI",
            "Auto Brake — MAX",
            "ATC Transponder — AUTO / ON",
            "TCAS — TA/RA",
            "Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brakes — CHECK "
        ],
        "Before Takeoff": [
            "Brake Temp — CHECK",
            "Approach Path & Runway — CLEAR",
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Nose Light — TO",
            "ECAM MEMO — TO NO BLUE",
            "Cabin Crew — REPORTED READY"
        ],
        "Climbout": [
            "THRUST LEVERS — CLB",
            "AP1 — ON",
            "Taxi Lights — OFF",
            "Above 10,000 ft — LANDING LIGHTS OFF",
            "AT TA - Altimiter SET STD",
        ],
        "Descent": [
            "MCDU Perf Page — ENTER ARRIVAL DATA & QNH",
            "MCDU Flight Plan — VERIFY STAR & APPROACH",
            "Altimiter — SET & CROSSCHECK",
            "Landing Elevation — SET",
            "Auto Brake — SET (LOW or MED)",
            "Approach Phase — ACTIVATE (Via MCDU)"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Landing Lights — ON",
            "Nose Light — TAXI",
            "Flaps — SET FULL or CONF 3",
            "Gear — DOWN (3 GREEN)",
            "ECAM MEMO — LANDING NO BLUE",
            "Ground Spoilers — ARMED",
            "Tables — STOWED"
        ],
        "Shutdown": [
            "Parking Brake — ON",
            "Thrust Levers — IDLE",
            "APU MASTER / EXT PWR — ON / CONNECTED",
            "Engine Master 1 & 2 — OFF",
            "Fuel Pumps (ALL) — OFF",
            "Beacon Light — OFF",
            "Seat Belts Sign — OFF",
            "Altimeter — SET STD"
        ],
        "Securing Aircraft": [
            "Oxygen Crew Supply — OFF",
            "ADIRS 1, 2, 3 — OFF",
            "APU BLEED — OFF",
            "APU MASTER — OFF",
            "Exterior Lights — ALL OFF",
            "Emergency Exit Lights — OFF",
            "Batteries 1 & 2 — OFF"
        ]
    },
    "Airbus A330": {
        "Pre-flight": [
            "Parking Brake — ON",
            "Batteries 1 & 2 — AUTO / ON",
            "External Power 1 & 2 — CONNECTED / ON",
            "APU MASTER — ON",
            "APU BLEED — ON",
            "ADIRS 1, 2, 3 — NAV (Full Alignment / Check Drift)",
            "Exterior Lights — NAV & LOGO ON",
            "Oxygen Crew Supply — ON",
            "Engine Masters 1 & 2 — OFF",
            "Engine Mode Selector — NORM",
            "Thrust Levers — IDLE",
            "Fuel Trim Tank / CG System — CHECK / AUTO",
            "ETOPS / Oceanic Equipment — VERIFIED READY",
            "MCDU / Flight Plan — INIT A & B, PERF, F-PLN SET"
        ],
        "Before Taxi": [
            "APU BLEED — ON",
            "Engine Mode Selector — IGN/START",
            "Engine 1 Master Switch — ON",
            "Engine 2 Master Switch — ON",
            "Engine Mode Selector — NORM (At 19% N1)",
            "GEN 1 & 2 — ON",
            "APU MASTER — OFF (as required)",
            "Hydraulic Panel — CHECK (Green, Blue, Yellow)",
            "Status / ECAM — CHECKED (NO BLUE)",
            "Flight Controls — CHECK (FULL FREE)",
            "Pitch Trim & Rudder Trim — SET FOR TAKEOFF / ZERO",
            "Flaps — SET FOR TAKEOFF"
        ],
        "Taxi": [
            "Nose Light — TAXI",
            "Auto Brake — MAX",
            "TCAS — TA/RA",
            "Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brake Test — CHECK",
            "Taxi Clearances & Oversteer Limits — ACKNOWLEDGED"
        ],
        "Before Takeoff": [
            "Brake Temp — CHECK",
            "Approach Path & Runway — CLEAR",
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Nose Light — TO",
            "ECAM MEMO — TO NO BLUE",
            "Cabin Crew — REPORTED READY"
        ],
       "Climbout": [
            "THRUST LEVERS — CLB",
            "AP1 — ON",
            "Taxi Lights — OFF",
            "Above 10,000 ft — LANDING LIGHTS OFF",
            "AT TA - Altimiter SET STD",
        ],
        "Descent": [
            "MCDU Performance Page — ENTER ARRIVAL DATA & QNH",
            "Trim Tank Fuel Transfer — VERIFY FORWARD TRANSFER AUTO",
            "FMGS / Flight Plan — VERIFY STAR & APPROACH",
            "Barometric Pressure — SET & CROSSCHECK",
            "Landing Elevation — AUTO",
            "Auto Brake — SET (LOW, MED, or BTV)",
            "Approach Phase — ACTIVATE (Via MCDU)"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Outer Wing Tank Transfer — CHECK AUTO",
            "Landing Lights — ON",
            "Nose Light — TAXI",
            "Flaps — SET",
            "Gear — DOWN (3 GREEN)",
            "ECAM MEMO — LANDING NO BLUE",
            "Ground Spoilers — ARMED",
            "Tables — STOWED"
        ],
        "Shutdown": [
            "Parking Brake — ON",
            "Thrust Levers — IDLE",
            "Engine Mode Selector — NORM",
            "Engine Master 1 & 2 — OFF",
            "Fuel Pumps (ALL) — OFF",
            "Beacon Light — OFF",
            "Seat Belts Sign — OFF",
            "APU MASTER - ON / EXT PWR 1 & 2 — ON / CONNECTED",
            "BARO Pressure — SET STD"
        ],
        "Securing Aircraft": [
            "Oxygen Crew Supply — OFF",
            "ADIRS 1, 2, 3 — OFF",
            "APU BLEED — OFF",
            "APU MASTER — OFF",
            "Exterior Lights — ALL OFF",
            "Emergency Exit Lights — OFF",
            "Batteries 1 & 2 — OFF"
        ]
    },
    "Airbus A340": {
        "Pre-flight": [
            "Parking Brake — ON",
            "Batteries 1 & 2 — AUTO / ON",
            "External Power 1 & 2 — CONNECTED / ON",
            "APU MASTER — ON",
            "APU BLEED — ON",
            "ADIRS 1, 2, 3 — NAV (Full Alignment / Check Drift)",
            "Exterior Lights — NAV & LOGO ON",
            "Oxygen Crew Supply — ON",
            "Engine Masters 1, 2, 3 & 4 — OFF",
            "Engine Mode Selector — NORM",
            "Thrust Levers — IDLE",
            "Fuel Trim Tank / CG System — CHECK / AUTO",
            "ETOPS / Oceanic Equipment — VERIFIED READY",
            "MCDU / Flight Plan — INIT A & B, PERF, F-PLN SET"
        ],
        "Before Taxi": [
            "APU BLEED — ON",
            "Engine Mode Selector — IGN/START",
            "Engine 1 & 2 Master Switch — ON",
            "Engine 3 & 4 Master Switch — ON",
            "Engine Mode Selector — NORM (At 19% N1)",
            "GEN 1, 2, 3 & 4 — ON",
            "APU MASTER — OFF (as required)",
            "Hydraulic Panel — CHECK (Green, Blue, Yellow)",
            "Status / ECAM — CHECKED (NO BLUE)",
            "Flight Controls — CHECK (FULL FREE)",
            "Pitch Trim & Rudder Trim — SET FOR TAKEOFF / ZERO",
            "Flaps — SET FOR TAKEOFF"
        ],
        "Taxi": [
            "Nose Light — TAXI",
            "Auto Brake — MAX",
            "TCAS — TA/RA",
            "Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brake Test — CHECK",
            "Taxi Clearances & Oversteer Limits — ACKNOWLEDGED"
        ],
        "Before Takeoff": [
            "Brake Temp — CHECK",
            "Approach Path & Runway — CLEAR",
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Nose Light — TO",
            "ECAM MEMO — TO NO BLUE",
            "Cabin Crew — REPORTED READY"
        ],
       "Climbout": [
            "THRUST LEVERS — CLB",
            "AP1 — ON",
            "Taxi Lights — OFF",
            "Above 10,000 ft — LANDING LIGHTS OFF",
            "AT TA - Altimiter SET STD",
        ],
        "Descent": [
            "MCDU Performance Page — ENTER ARRIVAL DATA & QNH",
            "Trim Tank Fuel Transfer — VERIFY FORWARD TRANSFER AUTO",
            "FMGS / Flight Plan — VERIFY STAR & APPROACH",
            "Barometric Pressure — SET & CROSSCHECK",
            "Landing Elevation — AUTO",
            "Auto Brake — SET (LOW, MED, or BTV)",
            "Approach Phase — ACTIVATE (Via MCDU)"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Outer Wing Tank Transfer — CHECK AUTO",
            "Landing Lights — ON",
            "Nose Light — TAXI",
            "Flaps — SET",
            "Gear — DOWN (4 GREEN)",
            "ECAM MEMO — LANDING NO BLUE",
            "Ground Spoilers — ARMED",
            "Tables — STOWED"
        ],
        "Shutdown": [
            "Parking Brake — ON",
            "Thrust Levers — IDLE",
            "Engine Mode Selector — NORM",
            "Engine Master 1, 2, 3 & 4 — OFF",
            "Fuel Pumps (ALL) — OFF",
            "Beacon Light — OFF",
            "Seat Belts Sign — OFF",
            "APU MASTER - ON / EXT PWR 1 & 2 — ON / CONNECTED",
            "BARO Pressure — SET STD"
        ],
        "Securing Aircraft": [
            "Oxygen Crew Supply — OFF",
            "ADIRS 1, 2, 3 — OFF",
            "APU BLEED — OFF",
            "APU MASTER — OFF",
            "Exterior Lights — ALL OFF",
            "Emergency Exit Lights — OFF",
            "Batteries 1 & 2 — OFF"
        ]
    },
    "Airbus A350": {
        "Pre-flight": [
            "Parking Brake — ON",
            "Batteries 1 & 2 — AUTO / ON",
            "External Power 1, 2 & 3 — CONNECTED / ON",
            "APU MASTER & BLEED — ON",
            "ADIRS 1, 2, 3 — NAV (Auto-align via MFD)",
            "Exterior Lights — NAV & LOGO ON",
            "Oxygen Crew Supply — ON",
            "Engine Masters 1 & 2 — OFF",
            "FMS / OIS — FLIGHT PLAN & PERF SET (via KCCU/Touch)",
            "ROPS / BTV Performance — PREPARED"
        ],
        "Before Taxi": [
            "APU BLEED — OFF",
            "Engine Start Selector — IGN/START",
            "Engine 1 Master Switch — ON (Verify Automatic Start Sequence)",
            "Engine 2 Master Switch — ON",
            "Engine Start Selector — NORMAL",
            "APU MASTER — OFF (as required)",
            "Status / ECAM — CHECKED (NO BLUE / ECL CLEARED)",
            "Flight Controls — CHECK (FULL FREE)",
            "Flaps — SET FOR TAKEOFF (CONF 1, 2, or 3)"
        ],
        "Taxi": [
            "Nose Light — TAXI",
            "Auto Brake — MAX / BTV SET",
            "TCAS — TA/RA",
            "Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brake Test — CHECK"
        ],
        "Before Takeoff": [
            "Brake Temp — CHECK",
            "Approach Path & Runway — CLEAR",
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Nose Light — TO",
            "ECL / ECAM MEMO — TO NO BLUE",
            "Cabin Crew — REPORTED READY"
        ],
        "Climbout": [
            "THRUST LEVERS — CLB",
            "AP1 — ON",
            "Taxi Lights — OFF",
            "Above 10,000 ft — LANDING LIGHTS OFF",
            "AT TA - Altimiter SET STD",
        ],
        "Descent": [
            "FMS / Arrival Data — ENTERED & CONFIRMED",
            "BTV (Brake to Vacate) — SELECTED / SET",
            "Barometric Pressure — SET & CROSSCHECK",
            "Approach Phase — ACTIVATE",
            "Landing Elevation — AUTO"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Landing Lights — ON",
            "Nose Light — TAXI",
            "Flaps — FULL (or CONF 3)",
            "Gear — DOWN (3 GREEN)",
            "ECAM / ECL MEMO — LANDING NO BLUE",
            "Ground Spoilers — ARMED"
        ],
        "Shutdown": [
            "Parking Brake — ON",
            "Thrust Levers — IDLE",
            "Engine Start Selector — NORMAL",
            "Engine Master 1 & 2 — OFF",
            "Seat Belts Sign — OFF",
            "APU MASTER / EXT PWR — ON / CONNECTED",
            "Fuel Systems — CHECK AUTO SHUTOFF",
            "Beacon Light — OFF"
        ],
        "Securing Aircraft": [
            "Oxygen Crew Supply — OFF",
            "ADIRS 1, 2, 3 — OFF",
            "APU BLEED & MASTER — OFF",
            "Exterior Lights — ALL OFF",
            "Emergency Exit Lights — OFF",
            "Batteries 1 & 2 — OFF"
        ]
    },
    "Boeing 737 NG": {
        "Pre-flight": [
            "Parking Brake — SET",
            "Battery Switch — GUARD CLOSED / ON",
            "Standby Power Switch — GUARD CLOSED / AUTO",
            "AC / DC Bus Transfer — AUTO",
            "Electrical Power (EXT PWR / APU) — ON BUS",
            "Emergency Exit Lights — GUARD CLOSED / ARMED",
            "APU BLEED — ON",
            "IRS Selectors (L & R) — NAV (Aligning)",
            "Window Heat — ON",
            "Electric Hydraulic Pumps (A & B) — ON",
            "Fuel Pumps — ON (as required)",
            "FMC / CDU — IDENT, POS INIT, ROUTE & PERF SET",
            "MCP — ALT, HDG, IAS SET",
            "Takeoff Speeds (V1, VR, V2) — SET & SELECTED"
        ],
        "Before Taxi": [
            "Engine Start Levers — CUTOFF",
            "Engine Start Switches — GRD (Start #2, then #1)",
            "Engine Start Levers — IDLE DETENT (at 25% N2)",
            "Generators 1 & 2 — ON BUS",
            "APU BLEED — OFF",
            "APU Switch — OFF",
            "Flaps — SET FOR TAKEOFF",
            "Flight Controls — CHECK (FULL FREE)",
            "Trim — SET FOR TAKEOFF",
            "Recall & Autoflight — CHECKED / CLEAR"
        ],
        "Taxi": [
            "Taxi Light — ON",
            "Auto Brake — RTO",
            "TCAS — TA/RA",
            "Weather Radar — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brakes — CHECK"
        ],
        "Before Takeoff": [
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Taxi Light — OFF",
            "MCP / LNAV & VNAV — ARMED / SELECTED",
            "Engine Start Switches — CONT",
            "Takeoff Config — CHECKED",
            "Cabin Crew — REPORTED READY"
        ],
        "Climbout": [
            "Autopilot — ENGAGE (Above 1,000 ft AGL)",
            "Flaps — RETRACT (On Speed Schedule)",
            "Engine Start Switches — OFF / AUTO",
            "Auto Brake — OFF",
            "Altimeters — SET STANDARD (at Transition Alt)"
        ],
        "Descent": [
            "FMC Arrival & Approach — ENTERED & EXECUTED",
            "Descent & Approach Briefing — COMPLETE",
            "Altimeters — SET QNH / LOCAL",
            "Auto Brake — SET (1, 2, or 3)",
            "Minimums — SET & CROSSCHECKED"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Landing Lights — ON",
            "Engine Start Switches — CONT",
            "Flaps — FULL (Flaps 30 or 40)",
            "Gear — DOWN (3 GREEN)",
            "Speedbrake Lever — ARMED",
            "Landing Checklist — COMPLETE"
        ],
        "Shutdown": [
            "Parking Brake — SET",
            "Engine Start Levers — CUTOFF",
            "Engine Start Switches — OFF",
            "Fasten Seat Belts Switch — OFF",
            "Electric Hydraulic Pumps — OFF",
            "Fuel Pumps — OFF",
            "APU / EXT PWR — ON BUS",
            "Position Light — STEADY",
            "Window Heat — OFF"
        ],
        "Securing Aircraft": [
            "IRS Selectors — OFF",
            "Emergency Exit Lights — OFF",
            "APU BLEED & APU Switch — OFF",
            "Battery Switch — OFF"
        ]
    },
    "Boeing 737 MAX": {
        "Pre-flight": [
            "Parking Brake — SET",
            "Battery Switch — GUARD CLOSED / ON",
            "Standby Power Switch — GUARD CLOSED / AUTO",
            "AC / DC Bus Transfer — AUTO",
            "Electrical Power (EXT PWR / APU) — ON BUS",
            "Emergency Exit Lights — GUARD CLOSED / ARMED",
            "APU BLEED — ON",
            "IRS Selectors (L & R) — NAV (Aligning via MAX Display)",
            "Window Heat — ON",
            "Electric Hydraulic Pumps (A & B) — ON",
            "Fuel Pumps — ON (as required)",
            "FMC / CDU — IDENT, POS INIT, ROUTE & PERF SET",
            "MCP — ALT, HDG, IAS SET",
            "Takeoff Speeds (V1, VR, V2) — SET & SELECTED"
        ],
        "Before Taxi": [
            "Engine Start Levers — CUTOFF",
            "Engine Start Switch — GRD (Start #2, then #1)",
            "Engine Start Levers — IDLE DETENT (Monitor Bowed Rotor Motoring)",
            "Generators 1 & 2 — ON BUS",
            "APU BLEED — OFF",
            "APU Switch — OFF",
            "Flaps — SET FOR TAKEOFF (e.g., Flaps 5)",
            "Flight Controls — CHECK (FULL FREE)",
            "Trim — SET FOR TAKEOFF",
            "Recall & Autoflight — CHECKED / CLEAR"
        ],
        "Taxi": [
            "Taxi Light — ON",
            "Auto Brake (Center Console) — RTO",
            "TCAS — TA/RA",
            "Weather Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brakes — CHECK"
        ],
        "Before Takeoff": [
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Taxi Light — OFF",
            "MCP / LNAV & VNAV — ARMED / SELECTED",
            "Engine Start Switches — CONT",
            "Takeoff Config — CHECKED",
            "Cabin Crew — REPORTED READY"
        ],
        "Climbout": [
            "Thrust Levers — TAKEOFF / TOGA",
            "Airspeed — ALIVE & CROSSCHECKED",
            "80 Knots — CHECKED",
            "Rotate (VR) — PITCH UP ~15°",
            "Positive Rate — GEAR UP (Auto-Depressurizes)",
            "Autopilot — ENGAGE (Above 1,000 ft AGL)",
            "Flaps — RETRACT (On Speed Schedule)",
            "Engine Start Switches — OFF / AUTO",
            "Auto Brake — OFF",
            "Altimeters — SET STANDARD (at Transition Alt)"
        ],
        "Descent": [
            "FMC Arrival & Approach — ENTERED & EXECUTED",
            "Descent & Approach Briefing — COMPLETE",
            "Altimeters — SET QNH / LOCAL",
            "Auto Brake — SET (1, 2, or 3)",
            "Minimums — SET & CROSSCHECKED"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Landing Lights — ON",
            "Engine Start Switches — CONT",
            "Flaps — FULL (Flaps 30 or 40)",
            "Gear — DOWN (3 GREEN)",
            "Speedbrake Lever — ARMED",
            "Landing Checklist — COMPLETE"
        ],
        "Shutdown": [
            "Parking Brake — SET",
            "Engine Start Levers — CUTOFF",
            "Engine Start Switches — OFF",
            "Fasten Seat Belts Switch — OFF",
            "Electric Hydraulic Pumps — OFF",
            "Fuel Pumps — OFF",
            "APU / EXT PWR — ON BUS",
            "Position Light — STEADY",
            "Window Heat — OFF"
        ],
        "Securing Aircraft": [
            "IRS Selectors — OFF",
            "Emergency Exit Lights — OFF",
            "APU BLEED & APU Switch — OFF",
            "Battery Switch — OFF"
        ]
    },
    "Boeing 777": {
        "Pre-flight": [
            "Parking Brake — SET",
            "Battery Switch — GUARD CLOSED / ON",
            "APU / External Power — ON BUS",
            "ADIRU — ON (Verify Align Status on EICAS)",
            "Hydraulic Primary & Demand Pumps — AUTO / ON",
            "Window Heat — ON",
            "Passenger Signs — ON",
            "Emergency Exit Lights — ARMED",
            "Fuel Pumps — ON (Check Main & Center Tanks)",
            "FMC / CDU — IDENT, POS INIT, ROUTE & PERF SET",
            "MCP — ALT, HDG, IAS SET",
            "Takeoff Speeds (V1, VR, V2) — SET & SELECTED"
        ],
        "Before Taxi": [
            "Engine Fuel Control Switches — CUTOFF",
            "Engine Start Switches — START (Start #1 & #2)",
            "Engine Fuel Control Switches — RUN (at 20% N2)",
            "Generators 1 & 2 — ON BUS",
            "APU BLEED — AUTO / OFF",
            "APU Selector — OFF",
            "Flaps — SET FOR TAKEOFF (Flaps 5 or 15)",
            "Flight Controls — CHECK (FULL FREE)",
            "Stabilizer Trim — SET FOR TAKEOFF",
            "EICAS — CHECKED (NO WARNINGS / ECL CLEARED)"
        ],
        "Taxi": [
            "Taxi Light — ON",
            "Auto Brake — RTO",
            "TCAS — TA/RA",
            "Weather Radar / PWS — ON / AUTO",
            "Cabin Crew — ADVISED",
            "Brake Test — CHECK (Monitor Temps & Main Gear Bogies)"
        ],
        "Before Takeoff": [
            "Landing Lights — ON",
            "Strobe Lights — ON",
            "Taxi Light — OFF",
            "MCP / LNAV & VNAV — ARMED / SELECTED",
            "Takeoff Config — CHECKED (NO EICAS WARNINGS)",
            "Cabin Crew — REPORTED READY"
        ],
        "Climbout": [
            "Thrust Levers — TAKEOFF / TOGA",
            "Airspeed — ALIVE & CROSSCHECKED",
            "80 Knots — CHECKED",
            "Rotate (VR) — PITCH UP ~12.5°",
            "Positive Rate — GEAR UP",
            "Autopilot 1 or 2 — ENGAGE (Above 200 ft AGL)",
            "Flaps — RETRACT (On Speed Schedule)",
            "Auto Brake — OFF",
            "Altimeters — SET STANDARD (at Transition Alt)"
        ],
        "Descent": [
            "FMC Arrival & Approach — ENTERED & EXECUTED",
            "Center Tank Fuel — CHECK BALANCED / EMPTY",
            "Descent & Approach Briefing — COMPLETE",
            "Altimeters — SET QNH / LOCAL",
            "Auto Brake — SET (1, 2, 3, 4, or MAX)",
            "Minimums — SET & CROSSCHECKED"
        ],
        "Landing": [
            "Cabin Crew — REPORTED READY",
            "Landing Lights — ON",
            "Flaps — FULL (Flaps 25 or 30)",
            "Gear — DOWN (3 GREEN / Main Gear Bogie Tilt Verified)",
            "Speedbrake Lever — ARMED",
            "EICAS / Landing Checklist — COMPLETE"
        ],
        "Shutdown": [
            "Parking Brake — SET",
            "Engine Fuel Control Switches — CUTOFF",
            "Passenger Signs — OFF",
            "Hydraulic Primary Pumps — OFF",
            "Fuel Pumps — OFF",
            "APU / Primary External Power — ON BUS",
            "Position Light — STEADY",
            "Window Heat — OFF"
        ],
        "Securing Aircraft": [
            "ADIRU — OFF",
            "Emergency Exit Lights — OFF",
            "APU Selector — OFF",
            "Battery Switch — OFF"
        ]
    }
}