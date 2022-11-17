import streamlit as st
import whisper
import os


st.title("Audio Transcription and Translation with Whisper")

audio_file = st.file_uploader("Choose a file", type= ["wav","mp3","m4a"])
if audio_file is not None:
    with open(os.path.join("tempDir",audio_file.name),"wb") as f: 
        f.write(audio_file.getbuffer())
    st.success("Saved File")

model = whisper.load_model("base")


if st.sidebar.button("Transcribe"):
    if audio_file is not None:
        st.sidebar.text("Transcribing...")
        transcript = model.transcribe(os.path.join("tempDir",audio_file.name))

        st.sidebar.success("Transcription complete")
        st.text(transcript["text"][:100])
    else:
        st.error("Please Upload an Audio File")

if st.sidebar.button("Download"):
    if transcript is not None:
        st.sidebar.text("Downloading...")
        st.sidebar.success("Download complete")
        st.download_button("Download", transcript["text"])
    else:
        st.error("Please Transcribe an Audio File")