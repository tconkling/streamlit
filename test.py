import streamlit as st
import streamlit.SessionState as SessionState


def c_to_f(c):
    return int(round(((9.0 / 5.0) * c) + 32))


def f_to_c(f):
    return int(round((f - 32) * (5.0 / 9.0)))


def get_state():
    return SessionState.get(celsius=10)


def get_celsius():
    return get_state().celsius


def get_fahrenheit():
    return c_to_f(get_celsius())


def set_celsius(new_value):
    get_state().celsius = int(new_value)


def set_fahrenheit(new_value):
    get_state().celsius = f_to_c(new_value)


MIN_C = -100
MAX_C = 300
MIN_F = c_to_f(MIN_C)
MAX_F = c_to_f(MAX_C)

st.header("Temperature")

st.slider(
    "Celsius",
    value=get_celsius(),
    min_value=MIN_C,
    max_value=MAX_C,
    on_changed=set_celsius,
)
st.slider(
    "Fahrenheit",
    value=get_fahrenheit(),
    min_value=MIN_F,
    max_value=MAX_F,
    on_changed=set_fahrenheit,
)
st.write(f"Temperature: {get_celsius()}C ({get_fahrenheit()}F)")

st.header("Other widgets")

st.selectbox(
    "Selectbox",
    ["one", "two", "three"],
    on_changed=print,
)

st.button("Button", on_changed=lambda: print(f"Button clicked!"))

st.text_input("Text input", on_changed=lambda value: print(f"Text input: {value}"))
