from deepgram import Deepgram
import asyncio, json
from pathlib import Path, PureWindowsPath

# I've explicitly declared my path as being in Windows format, so I can use forward slashes in it.
filename = PureWindowsPath("D:\\GithubRepo\\deepgram\\AWSTest.mp4.crdownload")

# Convert path to the right format for the current operating system
PATH_TO_FILE = Path(filename)

# The API key you created in step 1
DEEPGRAM_API_KEY = '04241277829a49a4eed4a4e687bdd022bc39ae0b'

# Replace with your file path and audio mimetype
#PATH_TO_FILE = R'D:/GithubRepo/deepgram/AWSTest.mp4'
MIMETYPE = 'audio/MP4s'

async def main():
    # Initializes the Deepgram SDK
    dg_client = Deepgram(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as audio:
        source = {'buffer': audio, 'mimetype': MIMETYPE}
        options = {'punctuate': True, 'language': 'en-GB'}

        print('Requesting transcript...')
        print('Your file may take up to a couple minutes to process.')
        print('While you wait, did you know that Deepgram accepts over 40 audio file formats? Even MP4s.')
        print('To learn more about customizing your transcripts check out developers.deepgram.com')

        response = await dg_client.transcription.prerecorded(source,  options)
        print(json.dumps(response, indent=4))

asyncio.run(main())
