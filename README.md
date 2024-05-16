# BitWars Player Python

## How it works

### Run it locally
Run the player directly:
```bash
gunicorn -b 0.0.0.0:3000 main:app
```
### Functionality
This application template provides a HTTP server with a single POST endpoint (/) on port `3000`.
The bit-dealer sends a POST request containing the current game state as a JSON object.
Your task is to implement a function which returns a `PlayerAction` as a response.
You'll find a predefined function `decide()` in this file: `/logic/strategy.py`.
In this file you can add unit-tests to quickly debug your application locally.
Run all unit-tests with the following command (executed in the root path of this project):
```bash
python -m unittest logic.strategy_test
```
