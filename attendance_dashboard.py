import streamlit as st
import pandas as pd

st.title(" Attendance Percentage Calculator")

st.header("Enter Your Attendance Details")

name = st.text_input("Enter Student Name:")
total_classes = st.number_input("Total Number of Classes", min_value=1)
attended = st.number_input("Number of Classes Attended", min_value=0)

if total_classes > 0:
    percentage = round((attended / total_classes) * 100, 2)
else:
    percentage = 0

if name:
    st.success(f"{name}'s Attendance Percentage: *{percentage}%*")

df = pd.DataFrame({
    "Student": [name] if name else [],
    "Total Classes": [total_classes] if name else [],
    "Attended": [attended] if name else [],
    "Attendance %": [percentage] if name else []
})

if not df.empty:
    st.header(" Attendance Summary Table")
    st.dataframe(df)

    st.header(" Attendance % Bar Chart")
    bar_data = df.set_index("Student")[["Attendance %"]]
    st.bar_chart(bar_data)

    st.header(" Attendance Trend Line Chart")
    st.line_chart(bar_data)

with st.expander("ℹ Notes"):
    st.write("""
    - Enter total classes & classes attended  
    - Dashboard calculates attendance %  
    - Generates table, bar chart and line chart  
    """)