import streamlit as st
import os
import requests
import re
from dotenv import load_dotenv

load_dotenv()

XAI_API_KEY = os.getenv("XAI_API_KEY")

if not XAI_API_KEY:
    st.error("Missing API key. Please set the XAI_API_KEY in the .env file.")
    st.stop()

st.set_page_config(page_title="PromptForge", page_icon="🛠️", layout="wide")

def generate_prompts(task):
    # Implement prompt generation logic here
    return {
        "Zero-shot": f"Generate a response for: {task}",
        "Role prompting": f"As a helpful assistant, {task}",
        "Few-shot": f"Here are examples of {task}: ...",
        "Constraint-based": f"Generate a response for {task} with constraints.",
        "Structured-output": f"Provide a structured response for: {task}",
    }

def optimize_prompt(prompt):
    # Implement prompt optimization logic here
    optimized_prompt = f"Optimized version of: {prompt}"
    return optimized_prompt, "This prompt is better because it includes more context."

def run_prompt(prompt):
    try:
        response = requests.post(
            "https://api.grok.ai/v1/execute",
            headers={"Authorization": f"Bearer {XAI_API_KEY}"},
            json={"prompt": prompt}
        )
        response.raise_for_status()
        return response.json().get("response", "No response received.")
    except requests.exceptions.RequestException as e:
        st.error(f"API error: {e}")
        return None

def evaluate_response(response, prompt=None):
    """Return heuristic scores that reflect the supplied response.

    The evaluator is intentionally local so it can still score responses when
    no separate judging-model API is configured.
    """
    if not response or not str(response).strip():
        return {criterion: 0 for criterion in (
            "Relevance", "Clarity", "Specificity", "Completeness",
            "Instruction following", "Factual reliability"
        )}, 0.0

    text = str(response).strip()
    words = re.findall(r"\b\w+\b", text.lower())
    unique_ratio = len(set(words)) / max(len(words), 1)
    sentences = [sentence for sentence in re.split(r"[.!?]+", text) if sentence.strip()]
    has_structure = bool(re.search(r"(^|\n)\s*(?:[-*] |\d+[.)] |#+\s)", text))
    has_specifics = bool(re.search(r"\b\d+(?:\.\d+)?\b|for example|such as|because|when|unless", text, re.I))
    has_sources = bool(re.search(r"https?://|\baccording to\b|\bcitation", text, re.I))
    prompt_words = set(re.findall(r"\b[a-z]{4,}\b", (prompt or "").lower()))
    response_words = set(words)
    overlap = len(prompt_words & response_words) / max(len(prompt_words), 1)

    def bounded(value):
        return round(max(1.0, min(10.0, value)), 1)

    scores = {
        "Relevance": bounded(4 + overlap * 6 if prompt else 5 + min(len(words), 80) / 40),
        "Clarity": bounded(4 + unique_ratio * 4 + (1 if len(sentences) <= 8 else 0)),
        "Specificity": bounded(4 + (2 if has_specifics else 0) + min(len(words), 120) / 60),
        "Completeness": bounded(2 + min(len(words), 180) / 45 + (1 if has_structure else 0)),
        "Instruction following": bounded(4 + (2 if has_structure else 0) + (1 if has_specifics else 0)),
        "Factual reliability": bounded(5 + (2 if has_sources else 0) + (1 if re.search(r"\bmay|might|likely\b", text, re.I) else 0)),
    }
    overall_score = round(sum(scores.values()) / len(scores) * 10, 1)
    return scores, overall_score

def ab_test(prompt_a, prompt_b):
    response_a = run_prompt(prompt_a)
    response_b = run_prompt(prompt_b)
    scores_a, overall_a = evaluate_response(response_a, prompt_a)
    scores_b, overall_b = evaluate_response(response_b, prompt_b)
    winner = "Prompt A" if overall_a > overall_b else "Prompt B"
    return (response_a, scores_a, overall_a), (response_b, scores_b, overall_b), winner

st.title("PromptForge")
st.subheader("Design. Test. Optimize. Ship better prompts.")

tabs = st.tabs(["Dashboard", "Prompt Playground", "A/B Testing", "Evaluation"])

with tabs[0]:
    st.write("Welcome to PromptForge! Use the tabs to navigate through the features.")

with tabs[1]:
    task = st.text_input("Enter a task:")
    if st.button("Generate Prompts"):
        if task:
            prompts = generate_prompts(task)
            for title, prompt in prompts.items():
                with st.expander(title):
                    st.write(prompt)
        else:
            st.error("Please enter a task.")

    existing_prompt = st.text_area("Enter an existing prompt:")
    if st.button("Optimize Prompt"):
        if existing_prompt:
            optimized, explanation = optimize_prompt(existing_prompt)
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Original Prompt")
                st.write(existing_prompt)
            with col2:
                st.subheader("Optimized Prompt")
                st.write(optimized)
                st.write(explanation)
        else:
            st.error("Please enter a prompt to optimize.")

    prompt_to_run = st.text_area("Enter a prompt to run:")
    if st.button("Run Prompt"):
        if prompt_to_run:
            response = run_prompt(prompt_to_run)
            if response:
                st.subheader("Response")
                st.write(response)
        else:
            st.error("Please enter a prompt to run.")

with tabs[2]:
    prompt_a = st.text_area("Enter Prompt A:")
    prompt_b = st.text_area("Enter Prompt B:")
    if st.button("Run A/B Test"):
        if prompt_a and prompt_b:
            (response_a, scores_a, overall_a), (response_b, scores_b, overall_b), winner = ab_test(prompt_a, prompt_b)
            st.subheader("Results")
            st.write("Prompt A Response:", response_a)
            st.write("Prompt B Response:", response_b)
            st.write("Winner:", winner)
            st.write("Prompt A Overall Score:", overall_a)
            st.write("Prompt B Overall Score:", overall_b)
        else:
            st.error("Please enter both prompts for A/B testing.")

with tabs[3]:
    response_to_evaluate = st.text_area("Enter a response to evaluate:")
    if st.button("Evaluate Response"):
        if response_to_evaluate:
            scores, overall_score = evaluate_response(response_to_evaluate)
            st.subheader("Evaluation Scores")
            for criterion, score in scores.items():
                st.metric(criterion, score)
            st.metric("Overall Score", overall_score)
        else:
            st.error("Please enter a response to evaluate.")