# Real-time Voice Translator 🎤

A Streamlit application for real-time Japanese ⇔ English voice translation using offline models.

## Features

- ✅ **Completely Offline**: No internet required after initial setup
- ✅ **Real-time Processing**: Live voice translation
- ✅ **Bidirectional**: Japanese ⇔ English translation
- ✅ **Dual Display**: Shows both original transcription and translation
- ✅ **Timestamp Tracking**: Records when each translation was made

## Installation

1. **Install Dependencies**:
   \`\`\`bash
   python scripts/install_dependencies.py
   \`\`\`

2. **For PyAudio Issues**:
   - **Windows**: `pip install pipwin && pipwin install pyaudio`
   - **Mac**: `brew install portaudio && pip install pyaudio`
   - **Linux**: `sudo apt-get install portaudio19-dev && pip install pyaudio`

## Usage

1. **Run the Application**:
   \`\`\`bash
   streamlit run scripts/voice_translator.py
   \`\`\`

2. **First Run**: Models will be downloaded automatically (requires internet)

3. **Select Language**: Choose your input language (Japanese or English)

4. **Start Recording**: Click the "Start Recording" button

5. **Speak**: Talk clearly into your microphone

6. **View Results**: See real-time transcription and translation

## Technical Details

### Models Used
- **Speech Recognition**: OpenAI Whisper (base model)
- **Translation**: Helsinki-NLP Marian models
  - Japanese → English: `Helsinki-NLP/opus-mt-ja-en`
  - English → Japanese: `Helsinki-NLP/opus-mt-en-jap`

### Performance
- **Processing Time**: ~2-5 seconds per 3-second audio chunk
- **Audio Quality**: 16kHz, mono
- **Supported Languages**: Japanese ⇔ English

### System Requirements
- **Python**: 3.7+
- **RAM**: 4GB+ recommended
- **Storage**: ~2GB for models
- **Microphone**: Required for voice input

## Troubleshooting

### Common Issues

1. **PyAudio Installation Error**:
   - Follow platform-specific installation instructions above

2. **Model Download Fails**:
   - Ensure stable internet connection for first run
   - Models are cached after first download

3. **Microphone Not Working**:
   - Check microphone permissions
   - Ensure microphone is not used by other applications

4. **Poor Translation Quality**:
   - Speak clearly and at moderate pace
   - Ensure good microphone quality
   - Avoid background noise

### Performance Tips

- **Better Accuracy**: Speak clearly with pauses between sentences
- **Faster Processing**: Use shorter speech segments (2-3 seconds)
- **Memory Usage**: Close other applications if running low on RAM

## File Structure

\`\`\`
├── scripts/
│   ├── voice_translator.py    # Main Streamlit application
│   └── install_dependencies.py # Dependency installer
├── requirements.txt           # Python dependencies
└── README.md                 # This file
\`\`\`

## License

This project uses open-source models and libraries. Please check individual model licenses for commercial use.
