<div align="center">

# 🌿 Plant Disease Detection System

**AI-powered leaf disease classification for potato and tomato crops**

> **Full runnable project:** `D:\plant_diseases_det`  
> This folder is the original Git clone from GitHub. Models, dataset, and the web app live on `D:\`.

<br/>

[![Python](https://img.shields.io/badge/Python-3.13-blue?style=flat-square)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.21-orange?style=flat-square)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?style=flat-square)](https://streamlit.io/)

**[📖 Full documentation](D:/plant_diseases_det/README.md)**

</div>

---

## 📦 Dataset

**Dataset files are not on GitHub** — too large (~11k images). Download locally using one of the methods below.

### Where data is stored (on your PC)

| Item | Path |
|------|------|
| **Project root** | `D:\plant_diseases_det\` |
| **Training images** | `D:\plant_diseases_det\PlantVillage\` |
| **Downloaded archive** | `D:\plant_diseases_det\data.zip` (~2.1 GB) |
| **Download script** | `D:\plant_diseases_det\download_dataset.py` |
| **Trained models** | `D:\plant_diseases_det\potato_model.keras`, `tomato_model.keras` |
| **Temp files** | `D:\plant_diseases_det\tmp\` |

Inside `PlantVillage/` you get **6 class folders** (3 potato + 3 tomato), e.g.:

```
D:\plant_diseases_det\PlantVillage\
├── Potato___Early_blight\
├── Potato___Late_blight\
├── Potato___healthy\
├── Tomato___Bacterial_spot\
├── Tomato___Early_blight\
└── Tomato___healthy\
```

> This Git clone folder (`OneDrive\Desktop\det`) does **not** contain the dataset — only the notebook clone. All data and models are under **`D:\plant_diseases_det`**.

### How to download

| Source | Link |
|--------|------|
| **Automatic (recommended)** | Run `download_dataset.py` — fetches potato & tomato subset from Hugging Face |
| **Hugging Face (full)** | [mohanty/PlantVillage](https://huggingface.co/datasets/mohanty/PlantVillage) |
| **Kaggle** | [Tomato leaf disease (notebook)](https://www.kaggle.com/code/rohanpatnaik/tomato-leaf-disease-image-classification/data) |

```powershell
cd D:\plant_diseases_det
pip install -r requirements.txt
py -3.13 download_dataset.py
```

After download, images are extracted to `D:\plant_diseases_det\PlantVillage\` (excluded from Git via `.gitignore`).

---

## 🚦 How to Run

Choose the guide that matches your situation.

---

### 🆕 First Time — Fresh Install

Use this when you are **setting up the project for the first time** on this computer.

| Step | Action |
|------|--------|
| 1 | Install [Python 3.13](https://www.python.org/downloads/) |
| 2 | Open **PowerShell** |
| 3 | Run the commands below in order |
| 4 | Open your browser at **http://localhost:8501** |

```powershell
cd D:\plant_diseases_det

$env:TEMP = "D:\plant_diseases_det\tmp"
$env:TMP  = "D:\plant_diseases_det\tmp"

py -3.13 -m pip install -r requirements.txt
py -3.13 download_dataset.py
py -3.13 train_split_models.py
START.bat
```

**Or the easiest way:** after Python and packages are installed, double-click:

```text
D:\plant_diseases_det\START.bat
```

Training runs automatically if model files are missing.

| Stage | Approx. time |
|-------|----------------|
| Install packages | 5–10 min |
| Download data (~2 GB) | 10–30 min |
| Train models | 15–25 min |
| Launch app | seconds |

---

### ✅ Already Installed on This Computer

Use this when **`D:\plant_diseases_det`** already exists with:
- `potato_model.keras`
- `tomato_model.keras`

| Step | Action |
|------|--------|
| 1 | Open folder `D:\plant_diseases_det` |
| 2 | Double-click **`START.bat`** |
| 3 | Open **http://localhost:8501** |

```powershell
cd D:\plant_diseases_det
START.bat
```

No need to re-download data or re-train — the app starts immediately.

---

### 🔍 Quick Check — Is Everything Ready?

```powershell
cd D:\plant_diseases_det
Test-Path potato_model.keras
Test-Path tomato_model.keras
```

| Result | Meaning |
|--------|---------|
| `True` for both | Ready — run `START.bat` only |
| `False` | Run `train_split_models.py` once, or use `START.bat` |

---

### 📱 Using the App

1. Select **Potato** 🥔 or **Tomato** 🍅
2. Upload a leaf image (JPG / PNG)
3. Read the diagnosis and confidence score

---

### ⚠️ Common Issues

| Problem | Fix |
|---------|-----|
| `Models not found` | Run `py -3.13 train_split_models.py` |
| `PlantVillage not found` | Run `py -3.13 download_dataset.py` |
| C: drive full | Use `D:\` and set `tmp` folder (see commands above) |
| Port 8501 in use | Close old Streamlit process or change the port |

---

## 📖 Full Documentation

See **`D:\plant_diseases_det\README.md`** for Features, Installation, Deployment, API notes, License, and more.

---

Based on [plant_diseases_detiction](https://github.com/Dhairyagoel10/plant_diseases_detiction)
