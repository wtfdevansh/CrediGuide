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

![qr code](https://drive.google.com/file/d/19gqYk-wESRacfz-aiskbgPJ473pQijSh/view?usp=sharing)


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
