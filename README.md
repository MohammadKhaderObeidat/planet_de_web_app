<div align="center">

# 🌿 Plant Disease Detection System

**AI-powered leaf disease classification for potato and tomato crops**

This repository contains a local Streamlit web app and notebook for training a plant disease detection model on the `PlantVillage` dataset.

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-orange?style=flat-square)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square)](https://streamlit.io/)

</div>

---

## Project Summary

This project includes:

- `app.py` — Streamlit application for image upload, prediction, and result display
- `plant.ipynb` — notebook containing dataset loading, model definition, training, evaluation, and saving
- `technical_report.md` — full documentation of the work completed in this workspace
- `download_dataset.py` — helper script to download the dataset if needed
- `PlantVillage/` — local dataset directory with training images
- `plant_model.keras` — trained Keras model artifact saved during this session

## Local Model and Dataset Status

This workspace now includes the dataset and the trained model artifact required to run the app locally.

- Dataset directory: `./PlantVillage`
- Dataset images: 11,227 images across 6 classes
- Saved trained model: `plant_model.keras`

### Classes

- `Potato___Early_blight`
- `Potato___Late_blight`
- `Potato___healthy`
- `Tomato_Bacterial_spot`
- `Tomato__Tomato_YellowLeaf__Curl_Virus`
- `Tomato_healthy`

## Model Architecture

The model is a custom TensorFlow Keras `Sequential` CNN built from scratch. It includes:

1. `Input` shape `(256, 256, 3)`
2. `Resizing(256, 256)`
3. `Rescaling(1./255)`
4. `RandomFlip("horizontal_and_vertical")`
5. `RandomRotation(0.2)`
6. `Conv2D(16, 3, padding='same', activation='relu')`
7. `MaxPooling2D()`
8. `Conv2D(32, 3, padding='same', activation='relu')`
9. `MaxPooling2D()`
10. `Conv2D(64, 3, padding='same', activation='relu')`
11. `MaxPooling2D()`
12. `Dropout(0.2)`
13. `Flatten()`
14. `Dense(128, activation='relu')`
15. `Dense(6, activation='softmax')`

## Training Details

The model was trained locally using the notebook and the following settings:

- `IMAGE_SIZE = 256`
- `BATCH_SIZE = 32`
- training on a subset of the dataset using `train_ds.take(50)`
- validation using `val_ds.take(20)`
- `epochs = 4`
- optimizer: `adam`
- loss: `SparseCategoricalCrossentropy(from_logits=False)`
- metric: `accuracy`

### Training result

- Test accuracy: `0.8576`
- Saved model file: `plant_model.keras`

## How to Run Locally

### 1. Activate the virtual environment

```bash
source ./venv/bin/activate
```

### 2. Run the Streamlit app

```bash
streamlit run app.py
```

### 3. Open the browser

Go to: http://localhost:8501

## If the Model File Is Missing

`app.py` now checks for a saved model file and shows a warning if none is available.

Supported model file names:

- `plant_model.keras`
- `potato_model.keras`
- `tomato_model.keras`
- `plant_model.h5`
- `potato_model.h5`
- `tomato_model.h5`

If the app cannot find a model file, add `plant_model.keras` to the folder and reload.

## Project Files

| File | Description |
|------|-------------|
| `app.py` | Streamlit app for model prediction and UI |
| `plant.ipynb` | Notebook with dataset loading, model architecture, training, evaluation, and saving |
| `technical_report.md` | Complete local documentation of the project and changes made |
| `plant_model.keras` | Saved trained model artifact |
| `download_dataset.py` | Dataset downloader helper script |
| `README.md` | Project overview and local run instructions |

## Notes

- This repo is now self-contained for local use with the existing dataset and saved model.
- The original upstream README referenced a separate `D:\plant_diseases_det` project path, but this workspace contains the necessary local files.
- Use `streamlit run app.py` rather than running `app.py` directly with Python to avoid Streamlit bare-mode warnings.

---

## Additional Information

If you want to retrain the model or improve accuracy:

1. Open `plant.ipynb`
2. Adjust data augmentation, architecture, or epochs
3. Run the training cells
4. Save the model again with `model.save('plant_model.keras')`

---

### Contact / Reference

Based on the original [plant_diseases_detiction](https://github.com/Dhairyagoel10/plant_diseases_detiction) repository.
