from mirascope.core import groq


@groq.call("llama-3.1-8b-instant")
def summarize(text: str) -> str:
    return f"Summarize this text: {text}"


@groq.call("llama-3.1-8b-instant")
def translate(text: str, language: str) -> str:
    return f"Translate this text to {language}: {text}"


summary = summarize("Long English text here...")
translation = translate(summary.content, "french")
print(translation.content)
