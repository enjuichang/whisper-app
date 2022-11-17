import streamlit as st
import whisper
import tempfile


st.title("Audio Transcription and Translation with Whisper")

audio_file = st.file_uploader("Choose a file", type= ["wav","mp3","m4a"])
if audio_file is not None:
    fp = tempfile.TemporaryFile()
    fp.write(audio_file.getbuffer())
    st.success("Saved File")

model = whisper.load_model("base")

if st.sidebar.button("Transcribe"):
    if audio_file is not None:
        st.sidebar.text("Transcribing...")
        fp.seek(0)
        transcript = model.transcribe(fp.read())
        fp.close()
        st.sidebar.success("Transcription complete")
        st.text(transcript["text"])
    else:
        st.error("Please Upload an Audio File")