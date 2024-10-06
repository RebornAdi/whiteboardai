import base64
from flask import Flask, render_template, request, jsonify
from io import BytesIO
from PIL import Image
import pyttsx3
import google.generativeai as genai

app = Flask(__name__)

# Initialize pyttsx3 for text-to-speech
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Configure Generative AI
genai.configure(api_key='AIzaSyDkXCF9pwFnauJcN4_FwX8YIDQtkw7HoPk')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the base64 image data from the request
        data = request.json['image']
        image_data = base64.b64decode(data.split(",")[1])
        
        # Open the image
        image = Image.open(BytesIO(image_data))
        
        # Save the image to disk (optional, for debugging)
        image.save("media/screenshot.png")
        print("Image saved as 'screenshot.png'")

        # Use the AI model to process the image
        question = Image.open("media/screenshot.png")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(["Analyse the following and answer accordingly 1)if user wants to converse do converse if it is conversation give only response 2)if other things then see and tell and analyse", question])
        
        # Get the AI-generated response text
        result_text = response.text
        print("AI Response: ", result_text)

        # Use text-to-speech to read out the AI response
        say(result_text)
        
        return jsonify({"text": result_text})
    
    except Exception as e:
        print("Error processing image: ", str(e))
        return jsonify({"error": "Failed to process image"}), 500

if __name__ == "__main__":
    app.run(debug=True)
