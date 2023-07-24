from flask import Flask, request
import openai

app = Flask(__name__)

@app.route('/get_teacher_ai_response', methods=['POST'])
def get_teacher_ai_response():
    student_input = request.json.get('student_input')
    grade = request.json.get('grade')
    model = "gpt-3.5-turbo"
    openai.api_key = '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'

    messages = [
        {"role": "system", "content": f"You are a professional school teacher teaching a single student in {grade}."},
        {"role": "user", "content": student_input}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        return {"response": response['choices'][0]['message']['content']}
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(port=5001)
