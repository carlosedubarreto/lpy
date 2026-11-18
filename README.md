# L-Py

[![License: GPL](https://img.shields.io/badge/License-GPL-blue.svg)](https://opensource.org/licenses/GPL-3.0)
[![CI Status](https://github.com/openalea/lpy/actions/workflows/openalea_ci.yml/badge.svg)](https://github.com/openalea/lpy/actions/workflows/openalea_ci.yml)
[![Documentation Status](https://readthedocs.org/projects/lpy/badge/?version=latest)](https://lpy.readthedocs.io/en/latest/?badge=latest)

L-systems were conceived as a mathematical framework for modeling the growth of plants. **L-Py** is a simulation software that mixes L-systems construction with the Python high-level modeling language.

In addition to this simulation engine, an integrated visual development environment (**L-Py Studio**) facilitates the creation, visualization, debugging, and parameter optimization of plant models.

---

## Features

- **L-System Simulation Engine**: Dynamic Python-integrated Lindenmayer systems.
- **L-Py Studio IDE**: Code editor with syntax highlighting, visual debugger, and parameter management panels.
- **3D Visualization**: Integrated with PlantGL for real-time 3D plant growth visualization.
- **Interactive Python Shell**: Embedded QtConsole/Jupyter shell for interactive exploration.
- **Dark & Light Themes**: Full dark mode support across the main window, code editor, parameter panels, and Python shell.

---

## Installation & Running (with Dark Mode)

Because L-Py relies on precompiled C++ libraries (Boost.Python, PlantGL), the recommended installation uses Conda for the compiled dependencies while linking this repository's GUI (including the Dark Theme).

### 1. Create the Conda Environment

```bash
conda create -n lpy python=3.10 openalea.lpy -c openalea3 -c conda-forge -y
conda activate lpy
```

### 2. Link This Source Code (with Dark Theme)

Link your local `gui` folder directly into the conda environment so that the new Dark Theme and all your changes are used:

#### Windows (PowerShell):
```powershell
# Remove the default GUI folder in the conda environment
Remove-Item -Recurse -Force "$env:USERPROFILE\miniconda3\envs\lpy\Lib\site-packages\openalea\lpy\gui"

# Create a live directory junction to this repo's GUI folder
New-Item -ItemType Junction -Path "$env:USERPROFILE\miniconda3\envs\lpy\Lib\site-packages\openalea\lpy\gui" -Target "D:\_Code\Meu\lpy\src\openalea\lpy\gui"
```

#### Windows (Command Prompt - `cmd.exe`):
```cmd
rmdir /s /q "%USERPROFILE%\miniconda3\envs\lpy\Lib\site-packages\openalea\lpy\gui"
mklink /J "%USERPROFILE%\miniconda3\envs\lpy\Lib\site-packages\openalea\lpy\gui" "D:\_Code\Meu\lpy\src\openalea\lpy\gui"
```

#### Linux / macOS:
```bash
CONDA_GUI=$(python -c "import openalea.lpy, os; print(os.path.join(os.path.dirname(openalea.lpy.__file__), 'gui'))")
rm -rf "$CONDA_GUI"
ln -s "$(pwd)/src/openalea/lpy/gui" "$CONDA_GUI"
```

*(Alternatively, you can simply copy the modified files from `src/openalea/lpy/gui/` into the environment's `site-packages/openalea/lpy/gui/` directory).*

---

## Running L-Py

Activate the environment and start L-Py Studio:

```bash
conda activate lpy
lpy
```

### Dark Mode Controls

- **Automatic**: Starts in Dark Theme by default.
- **Menu Toggle**: Switch between dark and light themes at any time from the menu: **View → Dark Theme**.
- **CLI Options**:
  ```bash
  lpy --dark     # Force Dark Theme
  lpy --light    # Force Light Theme
  ```
- **Persistence**: Your selected theme is automatically saved in your settings and remembered across restarts.

### Useful Shortcuts

- **`Ctrl+;`**: **Toggle Comment** — comments the current line or selected lines with `#`. Pressing it again uncomments them. Also accessible from **Edit → Toggle Comment**.

---

## Documentation

Full documentation is available at [http://lpy.readthedocs.io/en/latest/](http://lpy.readthedocs.io/en/latest/).

## Authors

L-Py was mainly developed by Frédéric Boudon with contributions from Christophe Godin, Christophe Pradal et al.

## Citation

If you find our work useful in your research, please consider citing:

> F. Boudon, T. Cokelaer, C. Pradal, P. Prusinkiewicz and C. Godin, *L-Py: an L-system simulation framework for modeling plant architecture development based on a dynamic language*, Frontiers in Plant Science, 30 May 2012.
