from flask import Flask, request
import openai
import json

app = Flask(__name__)

@app.route('/get_course_outline', methods=['POST'])
def get_course_outline():
    topic = request.json.get('topic')
    grade = request.json.get('grade')
    model = "gpt-3.5-turbo"
    openai.api_key = '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'

    outline_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a 30-minute classroom session outline on the topic: {topic} for {grade} in the format of Key: Value, where key is the outline topic and value is an array of topics under that outline topic and the entire response should be in json format. Also do not add any note or any text outside the json block. Also the first high level key should be named classroom_session_outline"}
    ]

    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=outline_messages
        )
        return json.loads(response.choices[0].message['content'].strip())
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(port=5000)
