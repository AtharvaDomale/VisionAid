# VisionAid: AI Assistant with Voice and Image Interaction

**VisionAid** is an AI assistant that combines advanced speech recognition, image processing, and generative AI to assist users through natural language and visual tasks.

## Features
- Voice-to-text and text-to-voice interaction.
- Captures and processes images for user queries.
- Uses Gemini Generative AI for content generation.


## Project Structure

```
VisionAid/
├── Requirements.txt          # List of dependencies required for the project
├── main.py                   # Main entry point of the program
├── speech_utils.py           # Module for handling speech-to-text and text-to-speech
├── image_utils.py            # Module for image capturing and encoding
├── ai_utils.py               # Module for interacting with Gemini Generative AI
├── README.md                 # Project description and setup instructions
```

- `Requirements.txt`: Contains all the Python packages that need to be installed.
- `main.py`: The main file that orchestrates the interaction between speech, image, and AI functionalities.
- `speech_utils.py`: A module for converting text to speech and speech to text.
- `image_utils.py`: A module for capturing and encoding images.
- `ai_utils.py`: A module for handling interactions with the Gemini Generative AI.


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/atharvadomale/VisionAid.git
   cd VisionAid
   ```

2. Install dependencies:
   ```bash
   pip install -r Requirements.txt
   ```

3. Replace `"API Key"` in `ai_utils.py` with your Gemini API key.

## Usage
Run the program:
```bash
python main.py
```

## Modules
- `speech_utils.py`: Handles speech-to-text and text-to-speech.
- `image_utils.py`: Manages image capturing and encoding.
- `ai_utils.py`: Manages generative AI interactions.

---

### Contributions
Contributions are welcome! Open an issue or submit a pull request.
