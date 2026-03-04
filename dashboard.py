
import streamlit as st

st.set_page_config(page_title="AFH Sales Dashboard", layout="wide")
st.title("AFH Sales Intelligence Dashboard")

with open("scout_report.txt") as f:
    scout = f.read()
with open("strategist_report.txt") as f:
    strategist = f.read()
with open("action_report.txt") as f:
    action = f.read()

tab1, tab2, tab3 = st.tabs(["🔍 Trend Scout", "📊 Campaign Strategist", "⚡ Action Engine"])

with tab1:
    st.markdown(scout)
with tab2:
    st.markdown(strategist)
with tab3:
    st.markdown(action)
