# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.
from flask import send_file
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
    
    
    config = aai.TranscriptionConfig(
    summarization=True,
    summary_model=aai.SummarizationModel.informative,
    summary_type=aai.SummarizationType.bullets
    )

    transcript = aai.Transcriber().transcribe(FILE_URL, config)

    return summary_parser(transcript.summary)

def download_notes(title, body):
    if not title:
        title = "Sample"
    if not body:
        body = "Sample"
    content = f"{title}\n\n{body}"

    with open('sample_file.txt', 'w') as file:
        file.write(content)

    return send_file('sample_file.txt', as_attachment=True)

def summary_parser(input_string):
    if input_string:
        result_list = input_string.split("-")
        
        # Remove leading and trailing whitespaces, including newline characters
        result_list = [element.strip("\n") for element in result_list]
        
        # Remove empty strings from the list
        result_list = [element for element in result_list if element]
        
        # Add back the hyphen to each element except the last one
        result_list = ["-" + element  for element in result_list[:-1]] + [result_list[-1]]
        
        return result_list
    else:
        return ""