# Reaction Time Game with Flask

This is a simple web application built with Flask that allows users to play a reaction time game. The game records reaction times and displays them over time in an interactive graph.

## Getting Started

### Prerequisites

- Python (>=3.6)
- Flask
- Plotly
- Other dependencies (install using `pip install -r requirements.txt`)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/reaction-time-game.git
    ```

2. Change into the project directory:

    ```bash
    cd reaction-time-game
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the Reaction Time Game.

3. Enter the port number, press "Start Game," and follow the on-screen instructions.

4. Optionally, press the "Generate Graph" button to see the reaction times plotted over time.

### Arduino Code

Check the `arduino-code` folder for a sample Arduino code that can be used with this project.

## Project Structure

- `app.py`: Main Flask application.
- `reaction.py`: Module containing the reaction time calculation logic.
- `templates/`: HTML templates for rendering the web pages.
- `arduino-code/`: Folder containing a sample Arduino code.



## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
