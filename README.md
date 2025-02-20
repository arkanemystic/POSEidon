# POSEidon

A smart fitness coaching app powered by computer vision and AI to perfect your form and track your progress.


## Overview

POSEidon combines cutting-edge computer vision technology with on-device AI processing to create a personal fitness coach that fits in your pocket. The app analyzes your workout form in real-time, counts repetitions, provides vocal feedback, and tracks your progress over time.

## Tech Stack

### Mobile Application (React Native)
- React Native framework for cross-platform compatibility
- Camera integration via react-native-vision-camera
- Real-time audio feedback system using React Native Sound

### Vision Processing
- MediaPipe Pose Estimation for real-time landmark detection
- Custom form analysis algorithms for joint angle measurement
- Movement tracking with temporal filtering
- Intelligent repetition counting system

### On-Device Processing
- Phi-2 LLM (Quantized) for personalized coaching insights
- ONNX Runtime for efficient model execution
- Piper TTS for natural-sounding voice feedback

### Backend (Firebase)
- Authentication for secure user accounts
- Cloud Storage for model updates and exercise templates
- Firestore database for user data and workout history
- Real-time database for seamless data synchronization

## Features

### Form Analysis
- Real-time feedback on exercise technique
- Joint angle measurement with ideal range visualization
- Form correction suggestions based on detected issues
- Support for 30+ common strength exercises

### Workout Tracking
- Automatic exercise detection and rep counting
- Set and rest time tracking
- Personal records and progress visualization
- Workout history with form improvement over time

### AI Coaching
- Personalized workout recommendations
- Form correction with natural language explanations
- Adaptive difficulty progression
- Voice guidance during exercises

## Installation

### Requirements
- iOS 14+ or Android 9+
- Camera and microphone permissions
- 500MB free storage space

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/valhalift/app.git
   cd app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment:
   ```bash
   cp .env.example .env
   # Configure your Firebase credentials in .env
   ```

4. Start the development server:
   ```bash
   npm start
   ```

### Vision Processing Module Setup

1. Navigate to the vision processing directory:
   ```bash
   cd vision-processing
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   pytest
   ```

## Architecture

```
├── Mobile App (React Native)
│   ├── Camera Module
│   │   └── Frame Processing
│   ├── UI Components
│   │   ├── Exercise Library
│   │   ├── Progress Tracking
│   │   └── Form Visualization
│   └── Audio System
│       └── Voice Feedback
│
├── Vision Processing
│   ├── MediaPipe Pose Estimation
│   ├── Form Analysis
│   │   ├── Joint Angle Calculation
│   │   └── Form Scoring
│   ├── Movement Tracking
│   │   ├── Velocity Analysis
│   │   └── Path Prediction
│   └── Rep Counter
│       ├── State Machine
│       └── Exercise Detection
│
├── On-Device AI
│   ├── Phi-2 LLM (Quantized)
│   ├── ONNX Runtime
│   └── Piper TTS
│
└── Firebase Backend
    ├── Authentication
    ├── Cloud Storage
    ├── Firestore
    │   ├── User Profiles
    │   └── Workout Logs
    └── Real-time Database
        └── Session Syncing
```

## Vision Algorithm Details

### Pose Estimation
ValhaLift uses MediaPipe's pose detection to identify 33 key body landmarks in 3D space. The system processes camera frames at 30fps and applies temporal filtering to ensure smooth tracking.

### Form Analysis
The app calculates joint angles using vector mathematics between connected landmarks:
- θ = cos⁻¹((v1·v2)/(|v1|·|v2|))
- Compares calculated angles against exercise-specific ideal ranges
- Factors in individual body proportions and mobility limitations

### Rep Counting Logic
The rep counting system uses a state machine approach:
1. Detect exercise preparation phase
2. Track ROM (Range of Motion) through key joint movements
3. Register completion when exercise-specific conditions are met
4. Apply debouncing to prevent false counts
5. Adapt to user's exercise pace and style over time

## Privacy & Security

ValhaLift prioritizes your privacy:
- All pose processing happens on-device
- Only anonymized exercise statistics are uploaded to the cloud
- Video is never stored or transmitted
- Firebase authentication with multi-factor options
- Option to use the app entirely offline

## Contributing

We welcome contributions from the community! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Roadmap
- [ ] Additional exercise support
- [ ] Custom workout builder
- [ ] Social sharing features
- [ ] Integration with fitness trackers
- [ ] Expanded analytics dashboard

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
