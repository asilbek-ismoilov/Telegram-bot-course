import wikipedia

def wiki(text):
    wikipedia.set_lang("uz")
    result = wikipedia.summary(text)
    return result