# Tiles Visualizer

## Set Up
1. Clone the repository
2. Create a virtual environment (OPTIONAL) :

    ```
    python3 -m venv env
    ```
3. Activate the environment (OPTIONAL):
    ```
    source env/bin/activate
    ```
4. install pip dependencies:
    ```
    pip install -r requirements.txt
    ```

## Data preparation
There should be a `data.csv` file on the root directory (or same level as `main.py`). The following structure is mandatory:

```
[NUMBER OF CHUNKS (grid size)], [CHUNK ID], [X], [Y]
```
There is a data.csv with sample data to check the structure

## Running

Just type:

```
python main.py
```
