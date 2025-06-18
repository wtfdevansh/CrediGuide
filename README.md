# Credi Guide 💳

Credi Guide is a user-friendly chatbot designed to help you find the perfect credit card based on your financial profile and spending habits. Interact with our intelligent assistant to receive personalized recommendations.

## Features

*   Interactive chatbot interface powered by Streamlit.
*   Personalized credit card recommendations using a Langchain agent.
*   Detailed information for each recommended card:
    *   Card Name and Issuer
    *   Card Image
    *   Rewards Summary
    *   Annual Fee
    *   Reason for Recommendation
*   Clear and structured presentation of recommendations.

## Technologies Used

*   Python
*   Streamlit (for the web application)
*   Langchain (for the AI agent and logic)
*   Langchain-OpenAI (for interacting with OpenAI models)
*   Pydantic (for data validation and schema)
*   Dotenv (for environment variable management)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <YOUR_REPOSITORY_URL> # Replace with the actual URL
    cd <YOUR_REPOSITORY_DIRECTORY>   # Replace with the actual directory name
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    Create a file named `.env` in the root directory of the project and add your OpenAI API key:
    ```env
    OPENAI_API_KEY="your_openai_api_key_here"
    ```
    Replace `"your_openai_api_key_here"` with your actual OpenAI API key.

## How to Run

*   Ensure your virtual environment is activated and you are in the project's root directory.
*   Run the Streamlit application using the following command:
    ```bash
    streamlit run app.py
    ```
*   Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## Access using whatsapp

![alt text](data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20viewBox%3D%220%200%2033%2033%22%20shape-rendering%3D%22crispEdges%22%3E%3Cpath%20fill%3D%22%23ffffff%22%20d%3D%22M0%200h33v33H0z%22%2F%3E%3Cpath%20stroke%3D%22%23000000%22%20d%3D%22M0%200.5h7m3%200h1m1%200h1m1%200h3m2%200h1m3%200h2m1%200h7M0%201.5h1m5%200h1m2%200h1m8%200h1m7%200h1m5%200h1M0%202.5h1m1%200h3m1%200h1m1%200h1m3%200h1m1%200h3m6%200h1m2%200h1m1%200h3m1%200h1M0%203.5h1m1%200h3m1%200h1m1%200h3m4%200h1m2%200h2m2%200h3m1%200h1m1%200h3m1%200h1M0%204.5h1m1%200h3m1%200h1m1%200h1m1%200h7m3%200h1m5%200h1m1%200h3m1%200h1M0%205.5h1m5%200h1m1%200h2m1%200h1m1%200h2m2%200h3m3%200h2m1%200h1m5%200h1M0%206.5h7m1%200h1m1%200h1m1%200h1m1%200h1m1%200h1m1%200h1m1%200h1m1%200h1m1%200h1m1%200h7M8%207.5h1m3%200h2m2%200h1m1%200h5m1%200h1M0%208.5h1m1%200h5m3%200h1m3%200h1m1%200h2m1%200h1m1%200h1m2%200h1m1%200h5M0%209.5h1m3%200h1m2%200h1m3%200h1m1%200h5m2%200h7m2%200h2m1%200h1M0%2010.5h2m3%200h2m1%200h7m2%200h1m1%200h1m1%200h2m2%200h2m1%200h1m1%200h2M1%2011.5h3m1%200h1m2%200h3m2%200h1m3%200h3m6%200h1m1%200h3m1%200h1M3%2012.5h2m1%200h2m1%200h2m3%200h1m1%200h1m2%200h4m2%200h2m2%200h1m2%200h1M0%2013.5h2m1%200h3m5%200h1m1%200h1m1%200h1m1%200h2m2%200h1m3%200h1m2%200h5M0%2014.5h1m1%200h2m2%200h2m1%200h1m1%200h2m2%200h3m2%200h2m1%200h3m1%200h1m2%200h2M0%2015.5h2m1%200h1m1%200h1m2%200h1m3%200h1m1%200h2m1%200h2m2%200h1m2%200h4m1%200h2M0%2016.5h2m1%200h1m1%200h2m2%200h2m1%200h1m2%200h3m5%200h3m1%200h2m3%200h1M1%2017.5h2m1%200h1m2%200h5m1%200h1m2%200h1m1%200h1m1%200h1m2%200h1m2%200h2m1%200h2M4%2018.5h1m1%200h6m3%200h1m2%200h1m6%200h2m1%200h1m1%200h2M0%2019.5h4m1%200h1m1%200h1m4%200h2m1%200h1m5%200h1m4%200h1m1%200h3M0%2020.5h2m1%200h1m2%200h3m1%200h1m1%200h1m1%200h1m3%200h2m1%200h1m1%200h4m2%200h1m1%200h2M0%2021.5h1m2%200h2m2%200h2m2%200h1m1%200h5m2%200h1m2%200h1m1%200h1m2%200h1m1%200h1m1%200h1M0%2022.5h1m2%200h1m2%200h1m1%200h2m2%200h3m3%200h2m1%200h4m2%200h2m1%200h2M0%2023.5h1m1%200h3m5%200h1m2%200h2m1%200h5m2%200h3m3%200h1m2%200h1M0%2024.5h1m2%200h1m1%200h2m1%200h4m2%200h1m4%200h3m1%200h6m2%200h2M8%2025.5h2m2%200h1m1%200h1m1%200h3m5%200h1m3%200h1m1%200h2M0%2026.5h7m4%200h1m1%200h1m3%200h1m4%200h3m1%200h1m1%200h1m1%200h3M0%2027.5h1m5%200h1m1%200h2m3%200h1m1%200h1m1%200h3m3%200h2m3%200h1m1%200h1m1%200h1M0%2028.5h1m1%200h3m1%200h1m1%200h2m1%200h1m2%200h3m2%200h4m1%200h6M0%2029.5h1m1%200h3m1%200h1m1%200h3m2%200h3m1%200h2m8%200h4M0%2030.5h1m1%200h3m1%200h1m1%200h2m1%200h3m1%200h4m1%200h4m2%200h2M0%2031.5h1m5%200h1m3%200h1m4%200h1m1%200h2m3%200h3m1%200h4M0%2032.5h7m1%200h2m3%200h5m3%200h1m1%200h2m2%200h2m1%200h2%22%2F%3E%3C%2Fsvg%3E)


## Project Structure

```
.
├── app.py                # Main Streamlit application file
├── llm_agent.py          # Defines the Langchain agent and its tools
├── card_agent/           # Module for card recommendation logic
│   ├── recommender.py    # Core recommendation engine
│   ├── data_loader.py    # Loads card data
│   └── ...
├── data/
│   └── sampleData.json   # Sample data for credit cards
├── requirements.txt      # Project dependencies
├── schema/               # Pydantic schemas for data validation
│   └── schema.py
├── assets/               # Images and static files for the UI
└── README.md             # This file
```

## Contributing

*   Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to:
    *   Open an issue on the project's GitHub page.
    *   Fork the repository, make your changes, and submit a pull request.
 
## Demo video
