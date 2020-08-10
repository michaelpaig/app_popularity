import streamlit as st
from joblib import load
from PIL import Image


st.title('Popular or Not?')

image = Image.open("itunes_app_store_icon_field_640.png")

st.header('Slide to the features on your app')


price = st.slider('Price', min_value=0, max_value=300,
                      value=0, step=1)
content_rating = st.slider('Content Rating', min_value=0, max_value=20,
                      value=0, step=1)
ipad_screenshot = st.slider('Number of Screenshot', min_value=0, max_value=5,
                      value=0, step=1)
lang_num = st.slider('Number of Languages', min_value=0, max_value=80,
                      value=0, step=1)
support_devices = st.slider('Suport Device Number', min_value=0, max_value=50,
                      value=0, step=1)
st.write("If your app is the following category, slide to 1.")
Education = st.slider('Education', min_value=0, max_value=1,
                      value=0, step=1)
Entertainment = st.slider('Entertainment', min_value=0, max_value=1,
                      value=0, step=1)
Games = st.slider('Games', min_value=0, max_value=1,
                      value=0, step=1)


model = load('final.pkl')
features = [price, content_rating, ipad_screenshot,
                     lang_num, support_devices, Education, Entertainment, Games]
popularity = model.predict([features])[0]


if st.button("Run me!"):
    if int(popularity) == 1:
        st.header("Your app is going to be popular!")
    else:
        st.header("You have a potential dud!")

