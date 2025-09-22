import streamlit as st
from datetime import datetime

st.title("Приложение для Jira (тестовое)")

if st.button("Показать текущую дату и время"):
    now = datetime.now()
    st.write(f"Сегодня: {now.strftime('%Y-%m-%d %H:%M:%S')}")