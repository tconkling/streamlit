import streamlit as st
import SessionState
from streamlit.proto.WidgetStates_pb2 import FloatArray


def get_slider_value(value) -> int:
    if isinstance(value, FloatArray):
        return int(value.value[0])
    return int(value)


def c_to_f(c):
    return int(round(((9.0 / 5.0) * c) + 32))


def f_to_c(f):
    return int(round((f - 32) * (5.0 / 9.0)))


def get_state():
    return SessionState.get(celsius=0)


def get_celsius():
    return get_state().celsius


def get_fahrenheit():
    return c_to_f(get_celsius())


def set_celsius(new_value):
    get_state().celsius = get_slider_value(new_value)
    print(f"set_celsius: {get_celsius()}")


def set_fahrenheit(new_value):
    get_state().celsius = f_to_c(get_slider_value(new_value))
    print(f"set_fahrenheit: {get_fahrenheit()}")


MIN_C = -100
MAX_C = 300
MIN_F = c_to_f(MIN_C)
MAX_F = c_to_f(MAX_C)


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
