from speech_utils import text_to_speech, speech_to_text
from image_utils import capture_image, encode_image
from ai_utils import configure_genai, upload_to_gemini, generate_ai_response
import google.generativeai as genai


def main():
    configure_genai(api_key="API Key")  # Replace with your API key
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }
    )

    text_to_speech("Hello, I'm your AI assistant. How can I help you today?")
    while True:
        text = speech_to_text()
        if text:
            if "image" in text or "picture" in text:
                text_to_speech("Sure, I'll capture an image for you. Please wait.")
                image_path = capture_image()

                if image_path:
                    text_to_speech("Image captured. What would you like me to do with it?")
                    file = upload_to_gemini(image_path, mime_type="image/jpeg")
                    text_to_speech("Describe your query related to the image.")
                    query = speech_to_text()

                    if query:
                        chat_session = model.start_chat(
                            history=[
                                {"role": "user", "parts": [file, query]},
                                {"role": "model", "parts": [""]},
                            ]
                        )
                        response = chat_session.send_message(query)
                        text_to_speech(response.text)
                    else:
                        text_to_speech("I couldn't understand your query. Please try again.")
                else:
                    text_to_speech("Failed to capture image. Please try again.")

            else:
                prompt = f"User said: {text}. Provide a brief response."
                response = generate_ai_response(model, prompt)
                text_to_speech(response.text)

            text_to_speech("Do you need any more help? Please say yes or no.")
            continue_response = speech_to_text(retry_count=2)
            if continue_response in ["no", "stop"]:
                break

    text_to_speech("Goodbye! Have a great day.")


if __name__ == "__main__":
    main()
