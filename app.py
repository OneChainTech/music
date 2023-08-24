from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

@app.route("/music", methods=['POST'])
def music():

    # prompt = requests.form.get("prompt")
    # music = requests.form.get("music")
    data = request.json
    prompt = data.get('prompt')
    music = data.get("music")

    client = Client("https://facebook-musicgen--5pw5h.hf.space/")
    result = client.predict(
            "Howdy!",	# str  in 'Describe your music' Textbox component
            "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",	# str (filepath or URL to file) in 'File' Audio component
            fn_index=0
    )
    print(result)
    return jsonify(result)

app.run()
