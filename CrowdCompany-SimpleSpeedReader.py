import streamlit as st
import time

# URL des Bildes
image_url = "https://d8wyob5mxqc1u.cloudfront.net/Allgemein/RaimundBauer180pxMagenta.png"

# Anzeigen des Bildes
st.image(image_url, caption='Raimund Bauer Crowdcompany UG')

#  Funktion zum aufteilen des Textes in Wörter
def split_string(text):
    return text.split()

# Initialisiere einen Platzhalter
placeholder = st.empty()

content = st.text_input("Enter your text for speed reading here: ")

pause_text_input = st.text_input ("Delay", value="")
pause_slider = st.slider("Delay in seconds", min_value=0.1, max_value=5.0, value=0.5, step=0.1)

if not pause_text_input:
    Pause = float(pause_slider)
else:
    Pause = float(pause_slider)

number_of_words_slider = st.slider("Number of words to show", min_value=1, max_value=10, value=3, step=1)
number_of_words=number_of_words_slider

# Check if there is content to display
if content:
    words = split_string(content)
    for i in range(0, len(words), number_of_words):  # Hier ist der Schritt auf X gesetzt
        # Grasp up to 3 words
        words_to_show = ' '.join(words[i:i+number_of_words])  # Dieser Bereich wählt ebenfalls X Wörter aus
        # Using Markdown with HTML to style the text
        placeholder.markdown(f"<h1 style='text-align: center; color: black; font-size: 48px;'>{words_to_show}</h1>", unsafe_allow_html=True)
        time.sleep(Pause)
