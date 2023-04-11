import gradio as gr
import requests

SERVER = '130.211.213.132'
# SERVER = '10.0.0.34'
PORT = '80'
# PORT = '8888'

def generate(text, temperature):
    data = {'instances': [text], 'temperature': temperature}

    response = requests.post(url=f'http://{SERVER}:{PORT}/predict', json=data)

    return response.json()['predictions'][0]

examples = [
    ["What is capitol of Slovakia?", 0.2],
    ["Jon Doe started in company ABC in 2020. He resigned in 2022 and started in company XYZ. Which company Jon Doe worked in 2021?", 0.2],
    ["Current temperature in Weston, FL is 26 C. What is the temperature in Weston, FL in Fahrenheit?", 0.2]
]

generator = gr.Interface(
    title='Google LLM',
    fn=generate,
    inputs=[
        gr.components.Textbox(lines=5, label="Input Text"),
        gr.Slider(0.1, 1.0, value=0.2, label="Temperature"),
    ],
    outputs=gr.components.Textbox(label="Generated Text"),
    examples=examples
)

generator.launch(server_name='0.0.0.0', server_port=8080)
