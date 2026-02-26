from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).parent
UI_DIR = BASE_DIR / "src" / "pos_settings" / "ui"
OUT_DIR = BASE_DIR / "src" / "pos_settings" / "ui_generated"

OUT_DIR.mkdir(exist_ok=True)

for ui_file in UI_DIR.rglob("*.ui"):
    output_file = OUT_DIR / f"ui_{ui_file.stem}.py"

    print(f"Compiling {ui_file.name} -> {output_file.name}")

    subprocess.run([
        "pyside6-uic",
        str(ui_file),
        "-o",
        str(output_file)
    ], check=True)

print("Done.")


# pyside6-designer