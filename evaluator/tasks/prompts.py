SUMMARIZATION_TEMPLATE = """
You will be given one summary written for a news article. Your task is to
rate the summary on one metric. Please make sure you read and understand
these instructions carefully.

Evaluation Criteria:
{criteria}

Please rate the summary based on the above metrics and provide your scores and explanations in the response box. 
Please use the following format for your response: 
Score: point 
Explanation: explanation

Here is the input:
Summary: {summary}
Text: {text}
"""


COHERENCE_CRITERIA = """
Coherence: It measures the quality of all sentences collectively, 
do they make sense as a whole, with the context organized and connected logically.
Score 5: Entirely coherent, with good context-relatedness among all the sentences.
Score 4: Only containing some minor illogical parts that basically do not affect overall coherency.
Score 3: Coherent in general, with some obvious conflicting logical or inconsistent problems. 
Score 2: There are major unreasonable logic and semantic inconsistencies, but at least the related topic.
Score 1: Not coherent at all, full of self-contradictory or unrelated content.

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. 
Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for the metric on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.
4. Provide the scores for coherence in the response box.
5. Provide a brief explanation for each score in the response box.
"""

RELEVANCE_CRITERIA = """
Relevance: It measures the quality of the summary in terms of how well it covers the main topic and key points of the news article.
Score 5: Entirely relevant, covering all the main topics and key points of the news article.
Score 4: Only containing some minor irrelevant parts that basically do not affect overall relevance.
Score 3: Relevant in general, with some obvious conflicting logical or inconsistent problems.
Score 2: There are major irrelevant parts, but at least the related topic.
Score 1: Not relevant at all, full of self-contradictory or unrelated content.

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. 
Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for the metric on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.
4. Provide the scores for coherence in the response box.
5. Provide a brief explanation for each score in the response box.
"""

FLUENCY_CRITERIA = """
Fluency: It measures the quality of individual sentences, are they grammatically correct, 
non-repetitive, and in accord with common English usage, with clear meanings.
Score 5: Entirely fluent, grammatically correct, and well-written.
Score 4: Only containing some minor non-fluent parts or grammatical errors that basically have no effect on fluency.
Score 3: Fluent in general, with some obvious grammatical errors and unfamiliar phrases. 
Score 2: There are major grammatical errors, duplication, unfamiliar phrases and syntactic structures, and missing components, but some fluent segments.
Score 1: Not fluent at all, full of meaningless fragments and unclear contents.

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. 
Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for the metric on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.
4. Provide the scores for coherence in the response box.
5. Provide a brief explanation for each score in the response box.
"""

CONSISTENCY_CRITERIA = """
Consistency: It measures the quality of the summary in terms of how well it maintains the same tone and style throughout the text.
Score 5: Entirely consistent, with the same tone and style maintained throughout the text.
Score 4: Only containing some minor inconsistent parts that basically do not affect overall consistency.
Score 3: Consistent in general, with some obvious conflicting tone and style problems.
Score 2: There are major inconsistent tone and style, but at least the related topic.
Score 1: Not consistent at all, full of self-contradictory or unrelated tone and style.

Evaluation Steps:
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. 
Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for the metric on a scale of 1 to 5, where 1 is the lowest and 5 is the highest based on the Evaluation Criteria.
4. Provide the scores for coherence in the response box.
5. Provide a brief explanation for each score in the response box.
"""

NLI_TEMPLATE = """
You are given a Natural Language Inference (NLI) task output to evaluate. You will receive:

- A premise: the original statement
- A hypothesis: a statement that may or may not logically follow from the premise
- A label: the model's predicted relationship between the premise and the hypothesis ("entailment", "contradiction", or "neutral")

{criteria}

Your task is to evaluate the model's label and return "True" if the label is correct and "False" if the label is incorrect. You should also provide an explanation of why the label is correct or incorrect, based strictly on the logical relationship between the premise and hypothesis.

Example 1:

Premise: "A woman is running a marathon."
Hypothesis: "A woman is engaging in a physical activity."
Label: Entailment
Explanation: The hypothesis is a logical consequence of the premise. Running a marathon is a form of physical activity. The broader category of "physical activity" includes activities such as running, so the hypothesis follows logically. Therefore, you should return "True" if the label is "entailment" and "False" if any other label is given.

Example 2:

Premise: "A cat is sleeping on the sofa."
Hypothesis: "A cat is chasing a mouse."
Label: Contradiction
Explanation: The hypothesis describes an activity that directly contradicts the premise. Sleeping and chasing are mutually exclusive actions; a cat cannot be doing both simultaneously. Therefore, you should return "True" if the label is "contradiction" and "False" if any other label is given.

Example 3:

Premise: "A man is playing the piano at a concert."
Hypothesis: "The man is famous."
Label: Neutral
Explanation: The premise provides no information about the man's fame. Playing the piano at a concert does not necessarily imply fame; it could be a local or amateur performance. Therefore, the hypothesis is neither entailed nor contradicted by the premise. So, you should return "True" if the label is "neutral" and "False" if any other label is given.

Return your output in the following format:

Answer: [True/False]  
Explanation: [Your explanation why the answer is correct or incorrect, based strictly on the logical relationship between the premise and hypothesis]

Here is the input:
Premise: {premise}
Hypothesis: {hypothesis}
Label: {label}
"""

NLI_CRITERIA = """
Below you can see the definitions and examples for each one of the possible answers

Entailment: The Hypothesis is a logical consequence of the Premise. The information in the Hypothesis must be true if the Premise is true. (E.g., specific to general, part to whole, synonyms, paraphrasing)
Contradiction: The Hypothesis directly conflicts with the Premise. If the Premise is true, the Hypothesis cannot be true. (E.g., opposite meanings, factual disagreements, mutually exclusive statements)
Neutral: The Hypothesis is plausible but not guaranteed by the Premise. The Premise provides insufficient information to determine the truth of the Hypothesis. (E.g., additional details, unrelated content, implications that are not certain)
"""

PAIRWISE_TEMPLATE = """
You are given a question and two different answers provided by two separate AI models. Your task is to carefully compare both answers and decide which one is better.
You should consider the following criteria in your evaluation:

{criteria}
Please return your judgment in the following format:

Better Answer: [Answer 1 / Answer 2]
Explanation: [A detailed explanation of why you chose that answer, referring to the criteria above]

Here is the input:
Question: {question}
Answer 1: {answer_1}
Answer 2: {answer_2}
"""

PAIRWISE_CRITERIA = """
Relevance: How well does the answer address the question?
Correctness: Is the answer factually and logically accurate?
Clarity: Is the answer clear, well-structured, and easy to understand?
Depth: Does the answer show reasoning or deeper insight when appropriate?
"""

TRANSLATION_TEMPLATE = """
You are a professional English-to-Turkish translation evaluator. You will be given two sentences:

Source sentence (English): The original English sentence.
Translated sentence (Turkish): A sentence that is claimed to be its correct translation.
Your task is to evaluate how accurate, fluent, and grammatically correct the Turkish sentence is, using the following three equally important criteria:

Evaluation Criteria:
{criteria}

Output Format (strictly follow this structure):
Score: [1-5]
Explanation: [Clear and concise explanation citing strengths and weaknesses in terms of the three evaluation criteria]

Here is the input:
Source sentence (English): {source}
Translated sentence (Turkish): {translation}
"""

TRANSLATION_CRITERIA = """
Meaning Preservation: Does the Turkish sentence convey the full and correct meaning of the English sentence?
Fluency and Naturalness: Does the Turkish sentence sound natural and idiomatic to a native speaker?
Grammar and Spelling: Is the sentence free from grammatical errors, awkward constructions, or spelling mistakes?
Scoring (Only integers: 1 to 5):
5 (Excellent): Meaning is perfectly preserved; sentence is fluent and grammatically flawless. Professional-quality translation.
4 (Good): Small issues in word choice or fluency, but meaning is clear and no serious errors.
3 (Adequate): Understandable but has some meaning loss or unnatural phrasing. Noticeable grammatical or stylistic issues.
2 (Poor): Major meaning inaccuracies or awkward, incorrect language. Hard to read naturally.
1 (Very Poor): Completely incorrect, misleading, or incomprehensible translation.
"""

GENERIC_TEMPLATE = """
You are a professional evaluator. You will be given a task to evaluate the model's output based on the following description:
{criteria}

Your task is to evaluate the model's output and provide a score and explanation in the following format:
Score: [score]
Explanation: [Your explanation here]

Here is the input:
Input: {input}
Output: {output}
"""
