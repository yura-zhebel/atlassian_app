# app.py
from flask import Flask, redirect, url_for, Response
import streamlit as st
from streamlit.web.bootstrap import run

from threading import Thread
from datetime import datetime

# ----------------------
# Streamlit-приложение
# ----------------------
def streamlit_app():
    st.set_page_config(page_title="Jira Python App", layout="centered")
    st.title("Приложение для Jira (тестовое)")
    
    if st.button("Показать текущую дату и время"):
        now = datetime.now()
        st.write(f"Сегодня: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Запуск Streamlit в отдельном потоке
def start_streamlit():
    run(streamlit_app, "", [], {})

thread = Thread(target=start_streamlit, daemon=True)
thread.start()

# ----------------------
# Flask-приложение
# ----------------------
app = Flask(__name__)

@app.route("/")
def home():
    # Прямо редиректим на локальный Streamlit порт
    # Если используете облако Streamlit, можно вставить iframe на отдельной странице
    return redirect("http://localhost:8501")

# Маршрут для теста (можно заменить на OAuth endpoint для Jira)
@app.route("/status")
def status():
    return Response("Приложение работает!", mimetype="text/plain")

if __name__ == "__main__":
    app.run(port=5000)
