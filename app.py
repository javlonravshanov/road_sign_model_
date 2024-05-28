import streamlit as st
from fastai.vision.all import *
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# title
st.write("""
# Road sign model
A model that identifies the type of road sign from the image you have uploaded \n
*P.S. Please upload only road sign images, others are not supported*         
""")

file = st.file_uploader('Upload an image', type=['png', 'jpg', 'gif', 'svg'])
if file:
    st.image(file)
    img = PILImage.create(file)


    model = load_learner('road_sign_model.pkl')

    pred, pred_id, probs = model.predict(img)
    st.success(f'Prediction: {pred}')
    st.info(f'Probability: {probs[pred_id]*100:.2f}%')