# 🌍 Trip Planner Agent

An intelligent AI-powered travel planning application that creates comprehensive, personalized travel itineraries using real-time data from multiple sources. The application combines weather information, place search, expense calculations, and currency conversion to provide detailed travel plans with both mainstream and offbeat options.

## ✨ Features

- **🌤️ Real-time Weather Data**: Get current weather and forecasts for any destination
- **🏛️ Place Information**: Search attractions, restaurants, activities, and transportation options
- **💰 Expense Calculator**: Detailed cost breakdowns and budget planning
- **💱 Currency Conversion**: Real-time currency conversion for international travel
- **🎯 Dual Itinerary Plans**: Both mainstream tourist and offbeat adventure options
- **📱 Web Interface**: Streamlit-based frontend for easy interaction
- **🔧 REST API**: FastAPI backend for programmatic access
- **🤖 Agentic Workflow**: LangGraph-powered intelligent planning system

## 🏗️ Project Structure

```
Trip_Planner_Agent/
│
├── agent/                          # Core agent logic and workflow
│   ├── __init__.py
│   └── agentic_workflow.py         # LangGraph-based agent orchestration
│
├── app.py                          # Streamlit frontend application
├── main.py                         # FastAPI backend server
│
├── config/                         # Configuration files
│   ├── __init__.py
│   └── config.yaml                 # LLM and model configurations
│
├── images/                         # UI-related images and screenshots
│   ├── my_graph.png               # Generated workflow graphs
│   └── Screenshot from 2025-07-29 23-12-43.png  # UI screenshots
│
├── notebook/                       # Jupyter notebooks for experiments
│   └── experiments.ipynb          # Development and testing notebooks
│
├── prompt_library/                 # Prompt templates and system prompts
│   ├── __init__.py
│   └── prompt.py                   # System prompts for travel planning
│
├── tools/                          # Modular tools for the agent
│   ├── __init__.py
│   ├── arithmatic_op_tool.py      # Mathematical operations
│   ├── currency_conversion_tool.py # Currency conversion tools
│   ├── expense_calculator_tool.py  # Expense calculation tools
│   ├── place_search_tool.py       # Place and attraction search
│   └── weather_info_tool.py       # Weather information tools
│
├── utils/                          # Utility modules and helpers
│   ├── __init__.py
│   ├── config_loader.py           # Configuration loading utilities
│   ├── currency_converter.py      # Currency conversion utilities
│   ├── expense_calculator.py      # Expense calculation utilities
│   ├── model_loader.py            # LLM model loading utilities
│   ├── place_info_search.py       # Place search utilities
│   ├── save_to_document.py        # Document saving utilities
│   └── weather_info.py            # Weather information utilities
│
├── exception/                      # Custom exception handling
├── logger/                         # Logging utilities
├── env/                           # Environment configurations
│
├── requirements.txt                # Python dependencies
├── pyproject.toml                 # Project metadata and configuration
├── setup.py                       # Package setup script
├── uv.lock                        # Dependency lock file
├── .python-version                # Python version specification
├── .gitignore                     # Git ignore rules
└── README.md                      # Project documentation
```

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- API keys for external services (see Environment Variables section)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Trip_Planner_Agent
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with the following API keys:
   ```env
   OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
   GPLACES_API_KEY=your_google_places_api_key
   EXCHANGE_RATE_API_KEY=your_exchange_rate_api_key
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

## 🔧 Usage

### Running the Application

1. **Start the FastAPI backend:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start the Streamlit frontend:**
   ```bash
   streamlit run app.py
   ```

3. **Access the application:**
   - Frontend: http://localhost:8501
   - Backend API: http://localhost:8000

### API Usage

The application provides a REST API endpoint for programmatic access:

```python
import requests

# Example API call
response = requests.post(
    "http://localhost:8000/query",
    json={"question": "Plan a 3-day trip to Andaman Islands"}
)

result = response.json()
print(result["answer"])
```

## 🛠️ Core Components

### Agent System
- **LangGraph Workflow**: Intelligent agent orchestration using LangGraph
- **Tool Integration**: Seamless integration of multiple specialized tools
- **State Management**: Efficient message state management for conversations

### Available Tools

1. **Weather Information Tool**
   - Current weather data for any city
   - 5-day weather forecasts
   - Temperature and condition details

2. **Place Search Tool**
   - Attractions and landmarks
   - Restaurant recommendations
   - Activity suggestions
   - Transportation options
   - Fallback to Tavily search when Google Places fails

3. **Expense Calculator Tool**
   - Hotel cost estimation
   - Total trip expense calculation
   - Daily budget planning

4. **Currency Conversion Tool**
   - Real-time currency conversion
   - Support for multiple currencies

### Frontend Features

- **🌍 Modern UI**: Clean, responsive Streamlit interface
- **💬 Chat Interface**: Interactive conversation with the travel agent
- **📊 Markdown Output**: Formatted travel plans with detailed information
- **⏱️ Real-time Processing**: Live response generation with progress indicators

## 📋 Example Output

The application generates comprehensive travel plans including:

- **Weather Forecast**: Current and forecasted weather conditions
- **Dual Itinerary Plans**: 
  - Plan 1: Mainstream tourist itinerary
  - Plan 2: Offbeat adventure options
- **Accommodation Details**: Hotel recommendations with pricing
- **Activity Breakdown**: Day-by-day itinerary with timing
- **Cost Analysis**: Detailed expense breakdown and budget planning
- **Transportation Options**: Available transport modes and costs
- **Restaurant Recommendations**: Dining options with price ranges

## 🔑 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENWEATHERMAP_API_KEY` | OpenWeatherMap API key for weather data | Yes |
| `GPLACES_API_KEY` | Google Places API key for location data | Yes |
| `EXCHANGE_RATE_API_KEY` | Exchange rate API key for currency conversion | Yes |
| `GROQ_API_KEY` | Groq API key for LLM processing | Yes |
| `TAVILY_API_KEY` | Tavily API key for search fallback | Yes |

## 🛠️ Development

### Adding New Tools

1. Create a new tool class in the `tools/` directory
2. Implement the tool logic in the corresponding `utils/` file
3. Register the tool in the `GraphBuilder` class
4. Update the system prompt if needed

### Project Dependencies

Key dependencies include:
- **LangChain**: LLM integration and tool management
- **LangGraph**: Agent workflow orchestration
- **FastAPI**: Backend API framework
- **Streamlit**: Frontend web interface
- **Groq**: LLM provider for intelligent responses

## 📸 UI Images

The `images/` folder contains:
- **my_graph.png**: Generated workflow graphs showing the agent's decision process
- **Screenshots**: UI screenshots demonstrating the application interface

These images are used for:
- Documentation purposes
- UI/UX reference
- Workflow visualization
- Development tracking

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 coding standards
- Add comprehensive docstrings
- Include type hints for all functions
- Write tests for new features
- Update documentation for any changes

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **LangChain**: For the excellent LLM integration framework
- **LangGraph**: For the powerful agent orchestration capabilities
- **Streamlit**: For the intuitive web interface framework
- **FastAPI**: For the high-performance API framework

---

*This travel planning application uses AI to generate comprehensive travel itineraries. Please verify all information, especially prices, operating hours, and travel requirements before your trip.*
