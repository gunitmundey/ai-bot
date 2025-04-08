# Trading Bot

This project is a trading bot that utilizes algorithmic trading strategies to trade Bitcoin. The bot employs reinforcement learning to optimize trading decisions and connects to a broker using user-provided API keys.

## Project Structure

```
trading-bot
├── src
│   ├── bot.py          # Main logic for the trading bot
│   ├── ui.py           # User interface for API key input and trading status
│   ├── model.py        # Neural network model definition using TensorFlow
│   ├── data_fetcher.py  # Fetches historical and real-time data from Yahoo Finance
│   └── utils
│       └── __init__.py # Utility functions and constants
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Files to ignore in version control
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd trading-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the user interface to input your API keys:
   ```
   python src/ui.py
   ```

## Usage Guidelines

- After entering your API keys, the bot will start trading Bitcoin based on the defined strategies.
- The bot uses reinforcement learning to adapt its trading strategy over time.
- Monitor the trading status and results through the user interface.
- Logs are stored in `trading_bot.log` for debugging and monitoring purposes.

## Overview of Functionality

- **API Key Input**: The bot prompts users for their broker API keys to establish a connection.
- **Trading Logic**: The bot implements a trading strategy using a neural network model trained on historical data.
- **Data Fetching**: Historical and real-time Bitcoin price data is fetched from Yahoo Finance for analysis and trading decisions.
- **Logging and Error Handling**: The bot includes logging for monitoring and debugging, and handles errors gracefully.

