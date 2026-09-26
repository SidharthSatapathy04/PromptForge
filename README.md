# PromptForge

PromptForge is a Streamlit application for generating, optimizing, running, evaluating, and A/B testing AI prompts.

## Run locally

1. Create a `.env` file with:

   ```text
   XAI_API_KEY=your_api_key
   ```

2. Install dependencies:

   ```text
   pip install -r requirements.txt
   ```

3. Start the app:

   ```text
   streamlit run app.py
   ```

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, choose **New app** and select this repository.
3. Set the main file to `app.py`.
4. In **Advanced settings**, add this secret:

   ```toml
   XAI_API_KEY = "your_api_key"
   ```

Never commit `.env` or API keys to GitHub.