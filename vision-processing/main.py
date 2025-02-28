import sys
import os
import cv2
import mediapipe as mp
from src.pose_estimation.detector import PoseDetector
from src.form_analysis.analyzer import FormAnalyzer
from src.movement_tracking.tracker import MovementTracker
from src.rep_counter.counter import RepCounter

def main():
    cap = cv2.VideoCapture(0)  # Use 0 for webcam
    pose_detector = PoseDetector()
    form_analyzer = FormAnalyzer()
    movement_tracker = MovementTracker()
    rep_counter = RepCounter()
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break
            
        # Process frame through pipeline
        landmarks = pose_detector.detect(image)
        if landmarks:
            joint_angles = form_analyzer.calculate_angles(landmarks)
            movement = movement_tracker.track(landmarks)
            rep_count = rep_counter.count(movement)
            
            # Draw results on image
            annotated_image = pose_detector.draw_landmarks(image, landmarks)
            # Add UI elements showing angles, count, etc.
            
        cv2.imshow('Fitness Vision Analysis', annotated_image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC key
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()