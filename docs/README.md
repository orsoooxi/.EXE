# steps:
uses: actions/checkout@v2
## Set up Python
uses: actions/setup-python@v2
### with:
python3
## Install dependencies
run: 
    python -m pip install --upgrade pip
    pip install build
## Build package
run: 
###
    python -m build
## Publish package
