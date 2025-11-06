import streamlit as st
from src.helper import voice_input, text_to_speech, lim_model_object


def main():
    st.title("Multilingual AI Assistant")

    if st.button("Ask me Anything"):
        with st.spinner("Listening..."):
            text = voice_input()
            response = lim_model_object(text)
            text_to_speech(response)

            # Display audio player and download link
            audio_file = open("speech.mp3", 'rb')
            audio_bytes = audio_file.read()

            st.text_area("Response:", value=response, height=350)
            st.audio(audio_bytes, format='audio/mpe')
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")
            

        


if __name__ == "__main__":
    main()



