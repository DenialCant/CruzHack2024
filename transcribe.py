# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "db2eac9430074de2b97c0d7d83a017ee"



def audio_to_text(url):
    # URL of the file to transcribe
    FILE_URL = url
    #"https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

    # You can also transcribe a local file by passing in a file path
    # FILE_URL = './path/to/file.mp3'
    transcriber = aai.Transcriber()
    transcript = transcriber.transcribe(FILE_URL)
    return transcript.text

# print(transcript.text)
