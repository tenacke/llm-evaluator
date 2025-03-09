import ollama

example_data = {
    "id": "dm-test-8764fb95bfad8ee849274873a92fb8d6b400eee2",
    "decoded": "paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley . townsend hit back at merson on twitter after scoring for england against italy .",
    "expert_annotations": [
        {"coherence": 2, "consistency": 5, "fluency": 5, "relevance": 2},
        {"coherence": 2, "consistency": 5, "fluency": 5, "relevance": 4},
        {"coherence": 3, "consistency": 5, "fluency": 5, "relevance": 2},
    ],
    "turker_annotations": [
        {"coherence": 4, "consistency": 5, "fluency": 4, "relevance": 5},
        {"coherence": 5, "consistency": 4, "fluency": 4, "relevance": 4},
        {"coherence": 4, "consistency": 5, "fluency": 4, "relevance": 5},
        {"coherence": 4, "consistency": 5, "fluency": 4, "relevance": 5},
        {"coherence": 2, "consistency": 2, "fluency": 3, "relevance": 4},
    ],
    "references": [
        "Andros Townsend an 83rd minute sub in Tottenham's draw with Burnley. He was unable to find a winner as the game ended without a goal. Townsend had clashed with Paul Merson last week over England call-up.",
        "Sports columnist Paul Merson and Andros Townsend are in the midst of a twitter feud. Merson started it when Townsend was called up and wrote something disparaging about him in his column. Since then things have gone back and forth between the two.",
        "Merson is angered by the statement made by Townsend in his Sky Sports column. Merson threw a dig at Townsend after scoring his last game.",
        "Paul Merson has officially restarted his row line up with Andros Townsend. This is a result of seeing Townsend's performance in the last seven minutes of the game the previous Sunday.",
        "An athlete was brought in to save the game during an event against a rival team.  Although many disagreed with this decision as players have been known to get in trouble from time to time.",
        "Paul Merson and Andros Townsend have been in a bout for a while now, Merson felt that Townsend did not deserve a place in the English team. Townsend scored for England with a crucial goal to which Merson apologized and acknowledge the performance of Townsend in that game and wished him well on his performance. The back and forth between the two men has continued regardless but it appears that now their bad feelings have subsided despite some light jest between the two.",
        'Paul Merson restarted his fued with the former Arenal player Andros Townsend. Townsend the former Arsenal player scored a goal for England against italy. Townsend replied to Mersons remarks on Twitter by saying "not bad for a player that should be` nowhere near the squad \'ay"',
        "Paul Merson used to play for Arsenal. Andros Townsend has been criticized by Paul Merson. The goal scored against Italy was made by Townsend.",
        "Paul Merson, former Arsenal player and Andros Townsend have restarted their bout of banter. Merson tweeted about Townsend and his poor performance making it clear he did not believe that Townsend was good enough to play for England. Townsend however scored the crucial goal for England vs Italy. Merson swallowed his criticism of Townsend and acknowledge his performance. The two are in a good place now however and any subsequent banter between the two appears to have been in good taste.",
        "Andros Townsend used to play for arsenal. Sky sports pundit Merson criticized Andros Townsend. Andros Townsend scored a goal against Italy to a draw.",
        "Paul Merson, the Sky Sports pundit, criticized Andros Townsend last week after his call-up to the england squad.  Merson admitted it was a mistake after Townsend scored, bringing the match against Italy to a tie on Tuesday.  Merson is a former Arsenal player himself.",
    ],
    "model_id": "M1",
    "filepath": "cnndm/dailymail/stories/8764fb95bfad8ee849274873a92fb8d6b400eee2.story",
}

example_text = "".join(example_data["references"])
example_summary = example_data["decoded"]

query = (
    "What is the evaluation of the summary of this given text?\nText:\n"
    + example_text
    + "\n\nSummary:\n"
    + example_summary
)

model_name = "my-model-llama3.1-8b:latest"

response = ollama.chat(
    model=model_name,
    messages=[
        {"role": "user", "content": query},
    ],
)

print(response.message.content)
