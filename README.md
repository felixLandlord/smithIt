# smithIt
Forge your project structure like a blacksmith.

# WITH PIP & .VENV
# 1. python3 -m venv .venv                
# 2. source .venv/bin/activate
# 3. pip install -r requirements.txt
# 4. pip install .
# 5. smith smith.yaml

# WITH POETRY
# 1. poetry init & define dependencies              
# 2. poetry install
# 3. poetry shell
# 4. poetry build
# 6. pip install smithIt/dist/smithit-0.1.0-py3-none-any.whl

# IF CHANGES?
# poetry build
# poetry shell
# pip install /Users/landlord/Desktop/mega_projects/smithIt/dist/smithit-0.1.0-py3-none-any.whl --force-reinstall


smith --help
smith --output /path/to/output smith.yaml
smith --verbose smith.yaml
smith --force smith.yaml
smith --version
smith --config smith.yaml
smith --delete src/main.py
smith --delete src/utils
smith --delete src/main.py src/utils.py tests/test_main.py
smith --delete src/utils src/models tests/unit
smith --delete src/utils src/main.py tests/test_main.py
smith --rename src/main.py src/main_script.py
smith --rename src/utils src/utility_functions
smith create
smith create --config smith.yaml
smith move src/main.py src/utils.py /path/to/destination
smith add src/new_file.py src/new_dir
smith sync --config smith.yaml