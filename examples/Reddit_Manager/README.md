# Reddit Manager

A simple Streamlit app integrated with the Lyzr API and OpenAI API to manage and interact with Reddit queries. The app allows users to enter a query and receive responses powered by AI.

## Features

- **Text Input for Queries**: Users can input their Reddit-related queries into a text area.
- **AI-Powered Response**: The LyzrAgent processes the input using Lyzr API and OpenAI's GPT model to generate a relevant response.
- **Streamlit Interface**: A clean, user-friendly interface built with Streamlit, featuring a two-column layout for inputs and outputs.
- **Customizable Layout**: Layout set to wide for better user experience.
- **Environment Variables for API Keys**: Sensitive API keys are stored securely in environment variables using `dotenv`.


## Requirements

- Python 3.7 or higher
- Streamlit
- LyzrAgent SDK
- OpenAI API
- Python-dotenv

## Installation

1. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
   
2. Run create_agent.py file

   This File creates Environment, Agent and Returns agent_id. This Agent ID used in .env file.  

   ```bash
    python create_agent.py
    ```

3. Create a `.env` file in the root directory with the following content:

    ```
    LYZR_API_KEY=your_lyzr_api_key
    AGENT_ID=your_agent_id
    ```

4. Run the app using Streamlit:

    ```bash
    streamlit run app.py
    ```

## Usage

- Navigate to the app page where you will see two sections: one for input and one for output.
- Enter your Reddit-related query in the **"Enter Text Here"** text area and click **"Generate"**.
- The response from the LyzrAgent will be displayed in the second column under **"Response"**.

Powered by Lyzr and OpenAI

