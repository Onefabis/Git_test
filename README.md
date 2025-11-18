
![Structure](img/PFX_docs_structure.png)

# Project Structure

- **docs** – Raw, editable Markdown files.  
- **myst-editor** – WYSIWYG editor for Markdown files in the `docs` directory.  
- **sphinx** – Advanced documentation generator that converts Markdown in the `docs` directory into static HTML documentation.  

---

## Installation:

# Initial setup:

Install git.exe if it doesn't installed yet - https://git-scm.com/install/windows

```bash
git clone --recurse-submodules https://github.com/Onefabis/PFX_docs_project

```
# Quick Automatic Setup:

Simply run install.bat

# Quick Manual Setup:

## 1. Sphinx Setup

1. Install the latest Python version.  
2. Navigate to the Sphinx directory:  
   ```bash
   cd PFX_docs_project/sphinx
   ```

3. Create a Python virtual environment:

   ```bash
   python -m venv sphinx_venv
   ```
4. Activate the virtual environment:

   ```bash
   sphinx_venv/Scripts/activate
   ```
5. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
6. After installation, deactivate the environment:

   ```bash
   deactivate
   ```

## 2. Myst-Editor Setup

1. Navigate to the myst-editor directory:

   ```bash
   cd ../myst-editor
   ```
2. Create a Python virtual environment:

   ```bash
   python -m venv myst_venv
   ```
3. Activate the virtual environment (Windows):

   ```bash
   myst_venv/Scripts/activate
   ```
4. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## 3. Using the Tools

* **Launch WYSIWYG editor:**
  Run `launch_sphinx_editor_server.bat` to open the editor in your default browser.

* **Generate static HTML docs:**
  Run `build_sphinx.bat` to build HTML documentation from Markdown files.

---

# Myst-Editor Development

1. Navigate to the `myst-editor` folder.
2. Install required Node packages:

   ```bash
   npm install vite@^6.0.0
   ```
3. Before the first build, increase memory for the Vite build in PowerShell:

   ```powershell
   $env:NODE_OPTIONS="--max-old-space-size=8192"
   ```
4. Run the build:

   ```bash
   npm i && npm run build
   ```

   This will create a `dist` folder under `myst-editor/src/`.

