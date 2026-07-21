##  Aircraft Checklists

### Airbus Series
- [ ] **A220** - Draft full checklist
- [ ] **A320** - Complete all 9 phases (Pre-flight through Securing Aircraft)
- [ ] **A330** - Expand beyond basic Pre-flight and Before Takeoff phases
- [ ] **A340** - Draft full checklist
- [ ] **A350** - Draft full checklist

### Boeing Series
- [ ] **737 NG** - Draft full checklist
- [ ] **737 MAX** - Draft full checklist
- [ ] **777** - Draft full checklist

### Embraer Series
- [ ] **E175 Family** - Draft full checklist
- [ ] **E175 E2 Family** - Draft full checklist

### Bombardier Series
- [ ] **CRJ Family** - Draft full checklist
- [ ] **Dash 8 Family** - Draft full checklist

---

##  Core Application Features

- [ ] **Refactor Data Structure:** Move inline checklists from hardcoded `if/elif` blocks into a clean JSON/YAML data format or centralized dictionary file (`checklists.py`).
- [ ] **Reset Progress Button:** Add a button in the sidebar to reset all checked boxes for the current aircraft/phase.
- [ ] **Emergency Checklists:** Create a secondary navigation section for non-normal / emergency checklists (e.g., Engine Failure, Rapid Depressurization).
- [ ] **Custom Checklist Creator:** Allow users to upload or create custom `.json` checklists directly through the UI.

---

##  UI & UX Enhancements

- [ ] **Checklist Progress Bar:** Display a percentage progress bar showing how many items in the current phase are completed.
- [ ] **Audio Feedback:** Add option for audio chimes/callouts when completing a phase.
- [ ] **Dark / Cockpit Theme:** Customize Streamlit theme settings to fit night flight cockpit aesthetics (e.g., dim red/dark mode).
- [ ] **Compact Mode:** Provide a toggleable compact view designed for small screens or tablet/secondary monitor pop-outs.

---

##  Deployment & Docs

- [x] Create initial `main.py` prototype
- [x] Create initial `README.md`
- [x] Create initial `TODO.md`
- [x] Deploy app to Streamlit Community Cloud
- [ ] Finish Each Checklist
