# Technical Report

## Project Overview

This project is a Plant Disease Detection web app built with Streamlit and TensorFlow. It classifies potato and tomato leaf images into 6 classes:

- Potato Early blight
- Potato Late blight
- Potato healthy
- Tomato Bacterial spot
- Tomato Tomato YellowLeaf Curl Virus
- Tomato healthy

The repository includes:

- `app.py` — Streamlit application
- `plant.ipynb` — notebook with dataset loading, model definition, training, and evaluation
- `README.md` — project description and original usage instructions
- `download_dataset.py` — dataset download helper
- `PlantVillage/` — local dataset directory
- `plant_model.keras` — trained model saved during this session

## Environment

- OS: macOS
- Python: 3.11 (virtual environment in `venv/`)
- Key packages:
  - `tensorflow==2.21.0`
  - `streamlit==1.57.0`
  - `numpy`
  - `pillow`

The current active Python environment is the workspace virtual environment:

`/Users/apple/f/f/MASTER/Image_Processing/project/project 2/planet_de_web_app/venv`

## Dataset

The notebook expects the dataset folder at `PlantVillage/` inside the project root.

- Verified dataset exists at `./PlantVillage`
- Dataset content: 11,227 images across 6 classes
- Image pipeline uses `tf.keras.preprocessing.image_dataset_from_directory(...)`

## Notebook Findings

The notebook contains the full model definition and training flow.

- `images_dataset` is loaded from `PlantVillage/` using `tf.keras.preprocessing.image_dataset_from_directory(...)`
- The dataset is shuffled and partitioned into:
  - 80% training batches
  - 10% validation batches
  - 10% test batches
- Preprocessing and augmentation are applied using `tf.keras.Sequential` pipelines
- The notebook builds a custom CNN model from scratch, not a pre-trained transfer learning model
- The model is trained with `model.fit(...)` and evaluated on the test set

## Model Overview

The model is a custom TensorFlow Keras `Sequential` CNN with the following structure:

1. `Input` layer for shape `(256, 256, 3)`
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

### Training configuration

- `IMAGE_SIZE = 256`
- `BATCH_SIZE = 32`
- training on a subset of the dataset using `train_ds.take(50)`
- validation on a subset using `val_ds.take(20)`
- `epochs = 4`
- optimizer: `adam`
- loss: `SparseCategoricalCrossentropy(from_logits=False)`
- metric: `accuracy`

### Model artifact

- After training, the model is saved to `plant_model.keras`
- This artifact is loaded by `app.py` for prediction

## Changes Made

### 1. Model loading guard in `app.py`

The app was updated to:

- search for model files with names:
  - `plant_model.keras`
  - `potato_model.keras`
  - `tomato_model.keras`
  - `plant_model.h5`
  - `potato_model.h5`
  - `tomato_model.h5`
- show a warning when no model weights are found
- show an error if weights fail to load
- disable predictions until a valid saved model is available

### 2. Trained model creation

A training script was executed against the existing `PlantVillage` dataset.

- Training configuration used from notebook:
  - `IMAGE_SIZE = 256`
  - `BATCH_SIZE = 32`
  - training on a subset: `train_ds.take(50)`
  - validation on a subset: `val_ds.take(20)`
  - `epochs = 4`
- The model was compiled with:
  - optimizer: `adam`
  - loss: `SparseCategoricalCrossentropy(from_logits=False)`
  - metric: `accuracy`

### 3. Model saved

- Saved trained model to `plant_model.keras`
- Verified model file size: `96MB`
- The app now can load this file and perform predictions

## Training Results

- Test accuracy: `0.8576`
- Saved model path: `./plant_model.keras`

## Current App Behavior

- When `plant_model.keras` is present, `app.py` loads it and enables real predictions.
- When no trained model file exists, the app shows:
  - `Cannot run prediction because no valid trained model weights are available. Place a model file in the app folder and reload the page.`

## How to Run

1. Activate the virtual environment:

```bash
source ./venv/bin/activate
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Open the browser at:http://localhost:8501

## Files Summary

| File | Purpose |
|------|---------|
| `app.py` | Streamlit app with model loading and prediction UI |
| `plant.ipynb` | Notebook containing dataset loading and model training code |
| `plant_model.keras` | Trained model artifact saved from the notebook-based training run |
| `README.md` | Project documentation and original instructions |
| `download_dataset.py` | Script for dataset download if needed |

## Notes

- The current workspace includes the dataset and trained model artifact, so the app can be run locally.
- The original README refers to another project path (`D:\plant_diseases_det`), but the required files exist here in the local clone.
- The editor may still show `tensorflow.keras` import diagnostics if VS Code is not using the correct interpreter; runtime verification confirmed the imports work in the virtual environment.

## Next Steps

- Run `streamlit run app.py` to verify the web app loads and predicts correctly.
- Optionally remove the `.keras` file from git tracking if you plan to store only the notebook and source code.
- Optionally extend the app to show class labels in a user-friendly format.
