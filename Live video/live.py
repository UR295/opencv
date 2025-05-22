import cv2
import os
import zipfile
import time

def capture_video(output_path, duration=10):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return False

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

    start_time = time.time()
    print(f"Recording video for {duration} seconds...")
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Recording (press q to stop)', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Recording stopped by user.")
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Video saved to {output_path}")
    return True

def zip_videos(source_folder, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(source_folder):
            for file in files:
                if file.endswith(('.mp4', '.avi', '.mkv')):
                    filepath = os.path.join(root, file)
                    zipf.write(filepath, arcname=file)
    print(f"Created zip file: {zip_name}")

if __name__ == "__main__":
    videos_folder = 'videos'
    if not os.path.exists(videos_folder):
        os.makedirs(videos_folder)

    timestamp = int(time.time())
    video_filename = f"live_capture_{timestamp}.avi"
    video_path = os.path.join(videos_folder, video_filename)

    success = capture_video(video_path, duration=10)
    if success:
        zip_path = os.path.join(videos_folder, 'compressed_videos.zip')
        zip_videos(videos_folder, zip_path)





#                   CAMERA IPWEBCAM FROM MOBILE

# import cv2
# import os
# import zipfile
# import time

# def capture_video_from_ipcam(output_path, stream_url, duration=10):
#     cap = cv2.VideoCapture(stream_url)
#     if not cap.isOpened():
#         print("Error: Could not open IP camera stream.")
#         return False

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

#     start_time = time.time()
#     print(f"Recording video from IP camera for {duration} seconds...")
#     while time.time() - start_time < duration:
#         ret, frame = cap.read()
#         if not ret:
#             print("Failed to grab frame from IP stream.")
#             break
#         out.write(frame)
#         cv2.imshow('IP Camera Recording (press space to stop)', frame)
#         if cv2.waitKey(1) & 0xFF == ord(' '):  # Press space to stop early
#             print("Recording stopped by user.")
#             break

#     cap.release()
#     out.release()
#     cv2.destroyAllWindows()
#     print(f"Video saved to {output_path}")
#     return True

# def zip_videos(source_folder, zip_name):
#     with zipfile.ZipFile(zip_name, 'w') as zipf:
#         for root, _, files in os.walk(source_folder):
#             for file in files:
#                 if file.endswith(('.mp4', '.avi', '.mkv')):
#                     filepath = os.path.join(root, file)
#                     zipf.write(filepath, arcname=file)
#     print(f"Created zip file: {zip_name}")

# if __name__ == "__main__":
#     videos_folder = 'https/videos'
#     if not os.path.exists(videos_folder):
#         os.makedirs(videos_folder)

#     stream_url = "http://192.168.224.106:8080//video"  # Your IP camera URL
#     timestamp = int(time.time())
#     video_filename = f"live_capture_{timestamp}.avi"
#     video_path = os.path.join(videos_folder, video_filename)

#     success = capture_video_from_ipcam(video_path, stream_url, duration=10)
#     if success:
#         zip_path = os.path.join(videos_folder, 'compressed_videos.zip')
#         zip_videos(videos_folder, zip_path)
