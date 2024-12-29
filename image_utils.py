import cv2
import base64


def capture_image(camera_index=0):
    """Capture an image using the specified camera index."""
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite("captured_image.jpg", frame)
        return "captured_image.jpg"
    else:
        return None


def encode_image(image_path):
    """Encode the image as a Base64 string."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
