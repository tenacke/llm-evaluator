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

query = "summary\n" + example_summary + "\ntext\n" + example_text + "\n"

model_name = "evallm:v3"

for part in ollama.generate(model_name, query, stream=True):
    print(part["response"], end="", flush=True)
