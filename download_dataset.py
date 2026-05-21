"""Download PlantVillage subset used by plant.ipynb into ./PlantVillage/."""
import shutil
import zipfile
from pathlib import Path

from huggingface_hub import hf_hub_download

TARGET_CLASSES = {
    "Potato___Early_blight": "Potato___Early_blight",
    "Potato___Late_blight": "Potato___Late_blight",
    "Potato___healthy": "Potato___healthy",
    "Tomato___Bacterial_spot": "Tomato_Bacterial_spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": "Tomato__Tomato_YellowLeaf__Curl_Virus",
    "Tomato___healthy": "Tomato_healthy",
}

WORK_DIR = Path(r"D:\plant_diseases_det")
OUTPUT_DIR = WORK_DIR / "PlantVillage"
ZIP_PATH = WORK_DIR / "data.zip"


def main() -> None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)

    if not ZIP_PATH.exists():
        print(f"Downloading PlantVillage data.zip from Hugging Face to {WORK_DIR}...")
        downloaded = hf_hub_download(
            repo_id="mohanty/PlantVillage",
            repo_type="dataset",
            filename="data.zip",
            local_dir=str(WORK_DIR),
        )
        zip_path = Path(downloaded)
        if zip_path.resolve() != ZIP_PATH.resolve():
            shutil.move(str(zip_path), str(ZIP_PATH))
    else:
        zip_path = ZIP_PATH
        print(f"Using existing archive: {zip_path}")

    print(f"Extracting required classes from {zip_path}...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as archive:
        for archive_class, notebook_class in TARGET_CLASSES.items():
            prefix = f"raw/color/{archive_class}/"
            members = [m for m in archive.namelist() if m.startswith(prefix)]
            if not members:
                raise RuntimeError(f"No files found in archive for class: {archive_class}")

            out_dir = OUTPUT_DIR / notebook_class
            out_dir.mkdir(parents=True, exist_ok=True)
            count = 0
            for member in members:
                if member.endswith("/"):
                    continue
                filename = Path(member).name
                target = out_dir / filename
                if target.exists():
                    count += 1
                    continue
                with archive.open(member) as src, open(target, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                count += 1

            print(f"  {notebook_class}: {count} images")

    total = sum(len(list((OUTPUT_DIR / c).glob("*"))) for c in TARGET_CLASSES.values())
    print(f"Saved {total} images to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
