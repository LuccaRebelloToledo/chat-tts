import ChatTTS
import soundfile

# Initialize ChatTTS
chat = ChatTTS.Chat()
chat.load()

# Define the texts to be converted to speech
texts = {
    "en": "This is my homework on a text to speech model, thank you all for your attention.",
    "zh": "这是我的作业，关于一个文本到语音的模型，谢谢大家的关注。",
    "pt": "Este é o meu trabalho de casa sobre um modelo de texto para fala, obrigado a todos pela atenção."
} 

# Generate and save speech for each language
for lang, text in texts.items():
    wavs = chat.infer([text], use_decoder=True, lang=lang)
    soundfile.write(f"output_{lang}.wav", wavs[0], 24000)