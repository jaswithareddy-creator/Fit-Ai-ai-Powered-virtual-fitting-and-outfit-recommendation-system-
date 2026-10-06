from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import cv2
import mediapipe as mp
import numpy as np

app = FastAPI(title="FitAI Backend")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mp_pose = mp.solutions.pose


@app.get("/")
def home():
    return {
        "message": "FitAI AI Backend is running!"
    }


@app.post("/analyze")
async def analyze_body(file: UploadFile = File(...)):

    # Read uploaded image
    image_bytes = await file.read()

    # Convert image bytes to numpy array
    image_array = np.frombuffer(image_bytes, np.uint8)

    # Convert to OpenCV image
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    if image is None:
        return {
            "success": False,
            "message": "Invalid image"
        }

    # Convert BGR to RGB
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # MediaPipe Pose
    with mp_pose.Pose(
        static_image_mode=True,
        model_complexity=1,
        min_detection_confidence=0.5
    ) as pose:

        result = pose.process(rgb_image)

    # Check whether body was detected
    if not result.pose_landmarks:
        return {
            "success": False,
            "message": "No body detected. Please upload a clear full-body photo."
        }

    landmarks = result.pose_landmarks.landmark

    # Important body landmarks
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
    right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP]
    right_hip = landmarks[mp_pose.PoseLandmark.RIGHT_HIP]

    left_ankle = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE]
    right_ankle = landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE]

    # Calculate approximate body proportions
    shoulder_width = abs(
        left_shoulder.x - right_shoulder.x
    )

    hip_width = abs(
        left_hip.x - right_hip.x
    )

    body_height = (
        abs(left_ankle.y - left_shoulder.y)
        + abs(right_ankle.y - right_shoulder.y)
    ) / 2

    # Simple prototype classification
    if shoulder_width < 0.20:
        body_profile = "Small"
        recommended_size = "S"
    elif shoulder_width < 0.30:
        body_profile = "Medium"
        recommended_size = "M"
    else:
        body_profile = "Large"
        recommended_size = "L"

    return {
        "success": True,

        "body_analysis": {
            "height_estimation": "Approximate",
            "body_profile": body_profile,
            "recommended_size": recommended_size
        },

        "landmarks_detected": len(landmarks),

        "body_proportions": {
            "shoulder_width": round(shoulder_width, 3),
            "hip_width": round(hip_width, 3),
            "body_height_ratio": round(body_height, 3)
        },

        "message": "Body landmarks detected successfully."
    }


