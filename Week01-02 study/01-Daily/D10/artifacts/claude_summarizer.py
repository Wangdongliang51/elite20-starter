import anthropic

client = anthropic.Anthropic()

def summarize(text: str, max_tokens: int = 1024) -> str:
    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=max_tokens,
        messages=[
            {
                "role": "user",
                "content": f"请用中文总结以下内容，保持要点完整：\n\n{text}",
            }
        ],
    )
    return next(b.text for b in response.content if b.type == "text")

if __name__ == "__main__":
    sample = (
        "Artificial intelligence (AI) is intelligence demonstrated by machines, "
        "as opposed to the natural intelligence displayed by animals and humans. "
        "AI research has been defined as the field of study of intelligent agents, "
        "which refers to any system that perceives its environment and takes actions "
        "that maximize its chance of achieving its goals."
    )
    print(summarize(sample))
