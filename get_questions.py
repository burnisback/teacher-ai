from flask import Flask, request
import openai

app = Flask(__name__)

@app.route('/get_questions', methods=['POST'])
def get_questions():
    subtopic = request.json.get('subtopic')
    model = "gpt-3.5-turbo"
    openai.api_key = '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'

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a list of questions for the subtopic: {subtopic}"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        return {"questions": response['choices'][0]['message']['content'].split('\n')}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(port=5002)
