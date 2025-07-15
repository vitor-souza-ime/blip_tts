

# 🧠 Visual Description System with BLIP and Offline Speech (Windows)

This project implements an **AI-based visual description system** to assist **visually impaired individuals** by capturing images through a webcam, generating captions using **BLIP (Bootstrapping Language-Image Pretraining)**, and speaking the descriptions using **Windows offline text-to-speech (SAPI)**.

## 📷 What It Does

* Captures images every 5 seconds from your webcam.
* Uses a pretrained BLIP model from Hugging Face to generate a natural language description of the image.
* Uses the built-in Windows SAPI voice to speak the caption aloud.

---

## 🔧 Requirements

Install all required packages in one line:

```bash
pip install torch torchvision torchaudio transformers pillow opencv-python pywin32
```

You also need:

* Python 3.8 or higher (recommended: 3.12)
* Windows OS (uses `win32com.client` for offline voice)

---

## 🚀 How to Run

1. Save the main file as `main.py`.
2. Open the terminal and navigate to the project directory.
3. Run:

```bash
python main.py
```

---

## 🗣️ Voice Output

This project uses **Windows built-in voice engine (SAPI)** to read captions aloud offline. The default voice is selected automatically. You can change speed and voice in this line of the code:

```python
speaker.Voice = speaker.GetVoices().Item(0)  # Change index if multiple voices installed
speaker.Rate = -1  # Speed: from -10 (slow) to 10 (fast)
```

---

## 🧠 Model Used

* [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)

This model generates high-quality natural language descriptions from images.

---

## 💡 Use Cases

* Accessibility for blind and visually impaired users
* Image captioning for automation systems
* Smart surveillance or object detection systems with audio feedback

---

## 📄 License

This project is provided for educational and accessibility research purposes. BLIP is under the license provided by its authors on Hugging Face.




