from flask import Flask, request
import openai

app = Flask(__name__)

@app.route('/get_evaluation_result', methods=['POST'])
def get_evaluation_result():
    questions = request.json.get('questions')
    answers = request.json.get('answers')
    model = "gpt-3.5-turbo"
    openai.api_key = 'API - Key'

    correct_answers = 0
    for i, question in enumerate(questions):
        answer = answers[i]
        evaluation_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Is this answer correct for the question '{question}': {answer}"}
        ]

        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=evaluation_messages
            )
            if response and response['choices'][0]['message']['content'].lower().strip() == 'correct':
                correct_answers += 1
        except Exception as e:
            return {"error": str(e)}

    score = correct_answers / len(questions) * 100
    return {"score": score}

if __name__ == '__main__':
    app.run(port=5003)
