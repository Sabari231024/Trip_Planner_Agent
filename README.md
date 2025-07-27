# Trip Planner Agent

A modular Python project designed to assist with trip planning by providing tools for arithmetic operations, currency conversion, place search, weather information, and more. The project is structured for extensibility and clarity, making it easy to add new features and utilities.

## Project Structure

```
Trip_Planner_Agent/
│
├── agent/                  # Core agent logic (to be implemented)
│   └── __init__.py
│
├── app.py                  # (Empty) Placeholder for app entry point
├── main.py                 # Main script (prints a hello message)
│
├── config/                 # Configuration files
│   ├── __init__.py
│   └── config.yaml         # (Empty) Placeholder for configuration
│
├── notebook/               # Jupyter notebooks for experiments
│   └── experiments.ipynb   # (Empty)
│
├── prompt_library/         # Prompt templates and logic
│   ├── __init__.py
│   └── prompt.py           # (Empty)
│
├── tools/                  # Modular tools for the agent
│   ├── __init__.py
│   ├── arithmatic_op_tool.py         # (Empty)
│   ├── calculator_tool.py            # (Empty)
│   ├── currency_conversion_tool.py   # (Empty)
│   ├── place_search_tool.py          # (Empty)
│   └── weather_info_tool.py          # (Empty)
│
├── utils/                  # Utility modules
│   ├── __init__.py
│   ├── calculator.py                # (Empty)
│   ├── config_loader.py             # (Empty)
│   ├── currency_converter.py        # (Empty)
│   ├── model_loader.py              # (Empty)
│   ├── place_info.py                # (Empty)
│   └── save_to_document.py          # (Empty)
│
├── requirements.txt        # (Empty) Add dependencies here
├── pyproject.toml          # Project metadata/config (if using poetry or similar)
├── setup.py                # (Empty) Setup script for packaging
├── uv.lock                 # Lock file (if using uv or similar)
└── README.md               # Project documentation
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Trip_Planner_Agent
   ```
2. **(Optional) Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Add your dependencies to requirements.txt)*

## Usage

- The main entry point is `main.py`:
  ```bash
  python main.py
  ```
- This currently prints a hello message. Implement your agent logic in the `agent/` directory and tools in the `tools/` directory.

## Directory Overview

- **agent/**: Core agent logic and orchestration.
- **tools/**: Modular tools for calculations, currency conversion, place search, and weather info.
- **utils/**: Helper utilities for calculations, config loading, currency conversion, etc.
- **prompt_library/**: Prompt templates and logic for LLMs or other agents.
- **config/**: Configuration files (YAML, etc.).
- **notebook/**: Jupyter notebooks for prototyping and experiments.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## License

Specify your license here (e.g., MIT, Apache 2.0, etc.)

---

*This README is a template based on the current project structure. Update it as you implement features and add documentation for each module/tool.*
