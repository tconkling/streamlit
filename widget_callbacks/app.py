import streamlit as st
import SessionState


def get_state():
    return SessionState.get(text="", num_clicks=0)


def on_text_changed(new_value, old_value):
    get_state().text = new_value


def on_button_clicked():
    get_state().num_clicks += 1


st.write("Widget callback prototype")

st.write(f"Current text: {get_state().text}; num_clicks={get_state().num_clicks}")


st.text_input("Text input", on_changed=on_text_changed)
st.button("Click me", on_clicked=on_button_clicked)
st.button("No callback")
