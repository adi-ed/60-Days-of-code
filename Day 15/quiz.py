import json
with open("questions.json",'r') as f:
    content = f.read()
    
# print(content)

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1,"-",alternative)
    choice = int(input("Enter your answer: "))
    question["user_answer"] = choice
    
score = 0   
for index, question in enumerate(data):
    if question["user_answer"] == question["correct_answer"]:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    msg = f"{result} {index + 1} . Your answer: {question['user_answer']}, " \
    f"Correct answer: {question['correct_answer']}"
    print(msg)
print(f"Final Score is: {score} / {len(data)}")