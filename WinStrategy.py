import streamlit as st
import pandas as pd
import numpy as np

# Initialize data storage (in-memory for prototype)
if 'corporate_strategies' not in st.session_state:
    st.session_state.corporate_strategies = []

if 'business_unit_strategies' not in st.session_state:
    st.session_state.business_unit_strategies = []

if 'plant_strategies' not in st.session_state:
    st.session_state.plant_strategies = []

# Helper functions
def add_strategy(level, aspiration, field_focus, tactics, capabilities, management_systems, success_measures):
    strategy = {
        "Winning Aspiration": aspiration,
        "Playing Field": field_focus,
        "Tactics": tactics,
        "Capabilities Needed": capabilities,
        "Management Systems": management_systems,
        "Success Measures": success_measures,
        "Progress": "Not Started"
    }
    if level == "Corporate":
        st.session_state.corporate_strategies.append(strategy)
    elif level == "Business Unit":
        st.session_state.business_unit_strategies.append(strategy)
    else:
        st.session_state.plant_strategies.append(strategy)

def update_strategy_progress(level, index, progress):
    if level == "Corporate":
        st.session_state.corporate_strategies[index]["Progress"] = progress
    elif level == "Business Unit":
        st.session_state.business_unit_strategies[index]["Progress"] = progress
    else:
        st.session_state.plant_strategies[index]["Progress"] = progress

def display_dashboard(level):
    if level == "Corporate":
        st.write("### Corporate Strategy Dashboard")
        if len(st.session_state.corporate_strategies) > 0:
            df = pd.DataFrame(st.session_state.corporate_strategies)
            st.table(df)
        else:
            st.write("No strategies created yet.")
    
    elif level == "Business Unit":
        st.write("### Business Unit Strategy Dashboard")
        if len(st.session_state.business_unit_strategies) > 0:
            df = pd.DataFrame(st.session_state.business_unit_strategies)
            st.table(df)
        else:
            st.write("No strategies created yet.")
    
    else:
        st.write("### Plant Strategy Dashboard")
        if len(st.session_state.plant_strategies) > 0:
            df = pd.DataFrame(st.session_state.plant_strategies)
            st.table(df)
        else:
            st.write("No strategies created yet.")

# Streamlit app UI
st.title("Win Strategy Prototype - AreteDom")
st.write("This prototype aligns with AreteDom's strategy alignment principles from Corporate to Plant levels.")

# Sidebar menu tabs for Corporate, Business Unit, and Plant Level
tab = st.sidebar.radio("Choose Level", ["Corporate", "Business Unit", "Plant"])

# Strategy Form Input
if tab == "Corporate":
    st.sidebar.title("Corporate Level Strategy")
    with st.sidebar.form("corporate_strategy_form"):
        aspiration = st.text_input("Step 1: Winning Aspiration and Purpose")
        field_focus = st.text_input("Step 2: Playing Field (Areas of Focus)")
        tactics = st.text_input("Step 3: Tactics to Win")
        capabilities = st.text_input("Step 4: Capabilities Needed")
        management_systems = st.text_input("Step 5: Management Systems and Resources")
        success_measures = st.text_input("Step 6: What Success Looks Like (Measures)")
        submit = st.form_submit_button("Add Corporate Strategy")
        
        if submit and aspiration and field_focus and tactics and capabilities and management_systems and success_measures:
            add_strategy("Corporate", aspiration, field_focus, tactics, capabilities, management_systems, success_measures)
            st.success("Corporate Strategy added!")

elif tab == "Business Unit":
    st.sidebar.title("Business Unit Level Strategy")
    with st.sidebar.form("business_unit_strategy_form"):
        aspiration = st.text_input("Step 1: Winning Aspiration and Purpose")
        field_focus = st.text_input("Step 2: Playing Field (Areas of Focus)")
        tactics = st.text_input("Step 3: Tactics to Win")
        capabilities = st.text_input("Step 4: Capabilities Needed")
        management_systems = st.text_input("Step 5: Management Systems and Resources")
        success_measures = st.text_input("Step 6: What Success Looks Like (Measures)")
        submit = st.form_submit_button("Add Business Unit Strategy")
        
        if submit and aspiration and field_focus and tactics and capabilities and management_systems and success_measures:
            add_strategy("Business Unit", aspiration, field_focus, tactics, capabilities, management_systems, success_measures)
            st.success("Business Unit Strategy added!")

elif tab == "Plant":
    st.sidebar.title("Plant Level Strategy")
    with st.sidebar.form("plant_strategy_form"):
        aspiration = st.text_input("Step 1: Winning Aspiration and Purpose")
        field_focus = st.text_input("Step 2: Playing Field (Areas of Focus)")
        tactics = st.text_input("Step 3: Tactics to Win")
        capabilities = st.text_input("Step 4: Capabilities Needed")
        management_systems = st.text_input("Step 5: Management Systems and Resources")
        success_measures = st.text_input("Step 6: What Success Looks Like (Measures)")
        submit = st.form_submit_button("Add Plant Strategy")
        
        if submit and aspiration and field_focus and tactics and capabilities and management_systems and success_measures:
            add_strategy("Plant", aspiration, field_focus, tactics, capabilities, management_systems, success_measures)
            st.success("Plant Strategy added!")

# Strategy Progress Tracking
if tab == "Corporate" and len(st.session_state.corporate_strategies) > 0:
    st.sidebar.title("Track Corporate Strategy Progress")
    strategy_select = st.sidebar.selectbox("Select a strategy", range(len(st.session_state.corporate_strategies)))
    progress = st.sidebar.selectbox("Progress Status", ["Not Started", "In Progress", "Completed"])
    update_progress = st.sidebar.button("Update Progress")
    
    if update_progress:
        update_strategy_progress("Corporate", strategy_select, progress)
        st.success("Corporate strategy progress updated!")

elif tab == "Business Unit" and len(st.session_state.business_unit_strategies) > 0:
    st.sidebar.title("Track Business Unit Strategy Progress")
    strategy_select = st.sidebar.selectbox("Select a strategy", range(len(st.session_state.business_unit_strategies)))
    progress = st.sidebar.selectbox("Progress Status", ["Not Started", "In Progress", "Completed"])
    update_progress = st.sidebar.button("Update Progress")
    
    if update_progress:
        update_strategy_progress("Business Unit", strategy_select, progress)
        st.success("Business Unit strategy progress updated!")

elif tab == "Plant" and len(st.session_state.plant_strategies) > 0:
    st.sidebar.title("Track Plant Strategy Progress")
    strategy_select = st.sidebar.selectbox("Select a strategy", range(len(st.session_state.plant_strategies)))
    progress = st.sidebar.selectbox("Progress Status", ["Not Started", "In Progress", "Completed"])
    update_progress = st.sidebar.button("Update Progress")
    
    if update_progress:
        update_strategy_progress("Plant", strategy_select, progress)
        st.success("Plant strategy progress updated!")

# Main page - Dashboard for Corporate, Business Unit, or Plant strategies
if tab == "Corporate":
    display_dashboard("Corporate")
elif tab == "Business Unit":
    display_dashboard("Business Unit")
else:
    display_dashboard("Plant")

# Add footer with AreteDom brand
st.markdown("""
    ---
    **Adept Transformation Partners, LLC - AreteDom**  
    Strategy alignment tool prototype.
    """)
