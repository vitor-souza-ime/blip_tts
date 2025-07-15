import cv2
import time
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import win32com.client


# === Initialize BLIP ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)

# === Initialize Windows offline voice ===
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Rate = -1  # speaking speed (-10 to 10)
speaker.Voice = speaker.GetVoices().Item(0)

# === Start webcam ===
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open webcam.")
    exit()

print("Starting continuous scan every 5 seconds...")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            continue

        # Save captured frame as image
        img_path = "temp.jpg"
        cv2.imwrite(img_path, frame)

        # Display image for 5 seconds
        start_time = time.time()
        cv2.namedWindow("Captured Image", cv2.WINDOW_NORMAL)
        while time.time() - start_time < 5:
            cv2.imshow("Captured Image", frame)
            if cv2.waitKey(1) & 0xFF == 27:
                raise KeyboardInterrupt
        cv2.destroyWindow("Captured Image")

        # Process image using BLIP
        image = Image.open(img_path).convert("RGB")
        inputs = processor(image, return_tensors="pt").to(device)
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

        print(f"Caption: {caption}")
        speaker.Speak(caption)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting...")

cap.release()
cv2.destroyAllWindows()
