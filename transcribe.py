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

    print("SUMMARY" + transcript.summary)
    return summary_parser(transcript.summary)

def download_notes(title, body):

    content = f"{title}\n\n{body}"

    with open('sample_file.txt', 'w') as file:
        file.write(content)

    return send_file('sample_file.txt', as_attachment=True)


def summary_parser(input_string):
    result_list = input_string.split("-")
    
    # Remove leading and trailing whitespaces, including newline characters
    result_list = [element.strip("\n") for element in result_list]
    
    # Remove empty strings from the list
    result_list = [element for element in result_list if element]
    
    # Add back the hyphen to each element except the last one
    result_list = ["-" + element  for element in result_list[:-1]] + [result_list[-1]]
    
    print(result_list)
    print(len(result_list))
    return result_list

x = """- This is cs two two four four advanced algorithms. We have a mailing list. There's a yellow sheet of paper that's going around. If you want to contact us, you should email the staff at seas harvard. edu.
- In wordram, assume that given xy fitting in a word can do basically all the things that you can do in, say, c. There could be integer overflow, in which case we'll get the overflow of the correct answer. But you can simulate multiplying bigger numbers using in the word ram.
- The basic idea is some kind of divide and conquer. The idea behind van mdeboaz trees is that we will know if x lives in the data structure. How would you search for the predecessor of X in this recursive data structure?
- In any of the if cases, you'll have at most one recursive call. Elements in the array is constant. In constant time, you can follow a pointer and read the value in that memory address. If you treat the min as the same as any other object, then there will be times when you have to recursively insert into the summary. And that will make things w.
- The space of the venom device data structure is not great. So what could you imagine doing instead? What would you do with this hashing in order to improve the space? It turns out that it's possible to.
- There's actually a paper that shows a matching lower bound which shows that you can never do better than the min of de boaz and fusion trees. These are known to be optimal for linear or for nearly linear space data structures. Any final questions before next time we'll see fusion trees?
"""
summary_parser(x)