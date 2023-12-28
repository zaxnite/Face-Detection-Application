# Face Detection using OpenCV

This simple Python script uses the OpenCV library to perform real-time face detection through your computer's webcam. It utilizes the Haar Cascade classifier for face detection.

## Prerequisites

Ensure you have the required libraries installed. You can install them using:

```bash
pip install opencv-python
```

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/face-detection.git
   cd face-detection
   ```

2. **Download Haar Cascade File:**
   Download the Haar Cascade file for face detection from [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and save it in the project directory as `haarcascade_frontalface_default.xml`.

3. **Create a Virtual Environment (Optional):**
   If you prefer working within a virtual environment, create and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

4. **Run the Script:**
   ```bash
   python face_detection.py
   ```

## How to Use

- Upon running the script, your webcam will be activated, and the video feed will display with real-time face detection.

- Press the 'q' key to quit the program.

## Notes

- Ensure that your webcam is connected and functioning properly.

- You can customize the script by adjusting parameters like the scale factor and minimum neighbors in the `detectMultiScale` function for more accurate face detection.

Feel free to modify and enhance the code according to your needs. Happy coding!