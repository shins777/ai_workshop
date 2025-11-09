# Audio examples for gemini-live


## Install Python dependencies
```
uv add google-cloud-texttospeech playsound==1.2.2 pyobjc
```

## Usage

Authenticate your environment. 
```
gcloud config set project {PROJECT_ID}
gcloud auth application-default set-quota-project {PROJECT_ID}
gcloud auth application-default login
```

Run the examples with the following command. 
```
uv run -m audio.tts.chirp3_tts
uv run -m audio.tts.gemini_tts
```