# Glasses Tracker - AI-Powered Real-time Glasses Detection

A real-time web application for detecting whether people are wearing glasses using AI/ML models with TensorFlow.js on the frontend and Flask on the backend.

## Features

- 👓 Real-time glasses detection using BlazeFace and pixel analysis
- 📊 Live statistics dashboard with detection counts
- 📈 Face tracking and history logging
- 📥 CSV export functionality for detection data
- 🎨 Modern dark-themed UI with gradient accents
- 📱 Responsive design

## Tech Stack

**Frontend:**
- TensorFlow.js
- BlazeFace (face detection model)
- Vanilla JavaScript
- HTML5 Canvas

**Backend:**
- Flask
- Flask-SocketIO
- OpenCV
- MediaPipe
- NumPy

## Setup

### Prerequisites
- Python 3.8+
- Webcam
- Modern web browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/glasses-tracker.git
cd glasses-tracker
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Click "Start Tracking" to begin detection

## Project Structure

```
glasses-tracker/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── templates/
    └── index.html        # Frontend application
```

## How It Works

1. **Face Detection**: Uses BlazeFace model to detect faces in real-time from webcam
2. **Glasses Detection**: Analyzes the eye region for:
   - Edge density (frame characteristics)
   - Dark pixels (typical of glass frames)
3. **Face Tracking**: Maintains face IDs across frames to avoid duplicate counting
4. **Statistics**: Updates live counters and maintains detection history

## Usage

- **Start Tracking**: Begin real-time glasses detection
- **Reset**: Clear all statistics and history
- **Export CSV**: Download detection data as CSV file

## Features in Detail

### Detection Dashboard
- Current detection status
- Live count of people with/without glasses
- Total tracked individuals
- Confidence score visualization

### Detection Log
- Timestamped entries of detection changes
- Quick view of detection history
- Auto-scrolls to latest entries

## License

MIT License

## Contributing

Contributions welcome! Feel free to fork and submit pull requests.
