from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="openai/gpt-oss-120b",
  messages=[{"role":"user","content":"hello"}],
  temperature=1,
  top_p=1,
  max_tokens=4096,
  stream=True
)

for chunk in completion:
  reasoning = getattr(chunk.choices[0].delta, "reasoning_content", None)
  if reasoning:
    print(reasoning, end="")
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

