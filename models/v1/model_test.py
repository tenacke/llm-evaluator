import ollama
import os


example_text = ""
with open(
    os.path.join(
        "datasets",
        "cnndm/dailymail/stories/8764fb95bfad8ee849274873a92fb8d6b400eee2.story",
    ),
    "r",
) as f:
    example_text = f.read()

example_summary = "paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley . townsend hit back at merson on twitter after scoring for england against italy ."

query = (
    "What is the evaluation of the summary of this given text?\nText:\n"
    + example_text
    + "\n\nSummary:\n"
    + example_summary
    + "Score: \n"
)

model_name = "evallm:v1"

response = ollama.chat(
    model=model_name,
    messages=[
        {"role": "user", "content": query},
    ],
)

print("Response:")
print(response.message.content)
print("Expert Annotations (avg):\n Coherence: 2.67")
print("Turker Annotations (avg):\n Coherence: 3.8")
