# 🛠️ PromptForge

### Design. Test. Optimize. Ship Better Prompts.

**PromptForge** is a Streamlit-based AI prompt engineering platform designed to help developers, students, researchers, and AI enthusiasts **create, optimize, execute, evaluate, and compare prompts** in one place.

Instead of manually experimenting with prompts across different AI tools, PromptForge provides a centralized playground where users can explore different prompting techniques, improve existing prompts, run them through an AI model, evaluate generated responses, and perform **A/B testing** to compare prompt performance.

---

## 🚀 Why PromptForge?

The quality of an AI-generated response depends heavily on how the prompt is designed.

PromptForge simplifies the prompt engineering workflow:

**Create → Optimize → Run → Evaluate → Compare → Improve**

It provides a structured environment for experimenting with prompts and understanding how changes in prompt design can affect AI-generated responses.

---

## ✨ Features

### 🧠 1. Prompt Generation

Generate multiple prompt variations for the same task using different prompting strategies.

Currently supported approaches include:

- **Zero-Shot Prompting**
- **Role Prompting**
- **Few-Shot Prompting**
- **Constraint-Based Prompting**
- **Structured-Output Prompting**

This allows users to experiment with different ways of instructing an AI model.

---

### ✨ 2. Prompt Optimization

Already have a prompt?

Enter it into PromptForge and generate an optimized version.

The optimization workflow provides:

- Original prompt
- Optimized prompt
- Explanation of why the optimized prompt is improved

This helps users understand how prompt structure, context, and constraints can influence prompt quality.

---

### ▶️ 3. Prompt Playground

The **Prompt Playground** allows users to directly execute prompts against the configured AI API.

Users can:

1. Enter a prompt
2. Execute it
3. Receive the AI-generated response
4. Review the output

This provides a simple environment for rapid prompt experimentation.

---

### 📊 4. AI Response Evaluation

PromptForge includes a local heuristic-based evaluation system for analyzing generated responses.

Responses are evaluated across six criteria:

| Criterion                 | Description                                           |
| ------------------------- | ----------------------------------------------------- |
| **Relevance**             | How closely the response relates to the prompt        |
| **Clarity**               | How understandable and readable the response is       |
| **Specificity**           | Whether the response provides concrete details        |
| **Completeness**          | How thoroughly the response addresses the task        |
| **Instruction Following** | How well the response follows the requested structure |
| **Factual Reliability**   | Heuristic assessment based on available indicators    |

Each criterion receives a score from **1–10**, along with an overall score.

> **Note:** The current evaluator is heuristic-based and should be treated as an experimental evaluation mechanism rather than a definitive measure of factual accuracy.

---

### ⚖️ 5. A/B Prompt Testing

PromptForge allows users to compare two different prompts for the same task.

Users can provide:

```text
Prompt A
Prompt B
```

The application then:

1. Executes Prompt A
2. Executes Prompt B
3. Evaluates both responses
4. Calculates overall scores
5. Displays the results side-by-side
6. Identifies which prompt received the higher heuristic score

This makes it easier to experiment with different prompt structures and determine which produces the stronger evaluated response.

---

## 🖥️ Application Structure

PromptForge is organized into four main sections:

```text
PromptForge
│
├── 📊 Dashboard
│   └── Application overview
│
├── 🧪 Prompt Playground
│   ├── Generate prompts
│   ├── Optimize prompts
│   └── Run prompts
│
├── ⚖️ A/B Testing
│   ├── Prompt A
│   ├── Prompt B
│   ├── Responses
│   └── Comparative scores
│
└── 📈 Evaluation
    ├── Relevance
    ├── Clarity
    ├── Specificity
    ├── Completeness
    ├── Instruction Following
    ├── Factual Reliability
    └── Overall Score
```

---

## 🏗️ Technology Stack

PromptForge is built using:

- **Python** — Core application logic
- **Streamlit** — Interactive web application interface
- **Requests** — API communication
- **python-dotenv** — Environment variable management
- **Regular Expressions (`re`)** — Response analysis and heuristic evaluation
- **xAI API** — AI prompt execution

### Architecture

```text
                    ┌─────────────────────┐
                    │      User Input     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit UI    │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      Prompt Generation   Optimization      Prompt Execution
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                         ┌─────────────┐
                         │   xAI API   │
                         └──────┬──────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │ Generated       │
                       │ Response        │
                       └────────┬────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
              Evaluation               A/B Testing
                    │                       │
                    └───────────┬───────────┘
                                ▼
                         Performance Score
```

---

## 📁 Project Structure

A recommended project structure is:

```text
PromptForge/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
└── assets/
    └── screenshots/
```

### Important Files

| File               | Purpose                                                     |
| ------------------ | ----------------------------------------------------------- |
| `app.py`           | Main Streamlit application                                  |
| `requirements.txt` | Python dependencies                                         |
| `.env`             | Local API credentials                                       |
| `.gitignore`       | Prevents secrets and unnecessary files from being committed |
| `README.md`        | Project documentation                                       |

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/PromptForge.git
cd PromptForge
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure the API Key

Create a `.env` file in the root directory:

```env
XAI_API_KEY=your_api_key_here
```

PromptForge reads the API key using `python-dotenv`.

**Never commit your API key to GitHub.**

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# ☁️ Deploy on Streamlit Community Cloud

PromptForge can be deployed using Streamlit Community Cloud.

### Step 1 — Push the project to GitHub

Make sure your repository contains:

```text
app.py
requirements.txt
README.md
.gitignore
```

Do **not** commit:

```text
.env
API keys
secrets
```

---

### Step 2 — Create a Streamlit App

Open Streamlit Community Cloud and select:

```text
New app
```

Choose your GitHub repository and set:

```text
Main file path:
app.py
```

---

### Step 3 — Configure Secrets

Under **Advanced Settings → Secrets**, add:

```toml
XAI_API_KEY = "your_api_key_here"
```

Streamlit will expose the secret to the application environment.

---

# 🔐 Security

API credentials should never be hard-coded into the source code.

Use environment variables locally:

```env
XAI_API_KEY=your_api_key
```

and Streamlit secrets in deployment:

```toml
XAI_API_KEY = "your_api_key"
```

Add `.env` to `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
venv/
.venv/
```

If an API key is accidentally committed to a public repository, **revoke and regenerate it immediately**.

---

# 🧪 Example Workflow

Suppose you want to create a prompt for generating Python interview questions.

### Step 1 — Enter the task

```text
Generate Python interview questions for a software engineering candidate.
```

### Step 2 — Generate prompt variations

PromptForge can produce variations based on:

```text
Zero-Shot
Role Prompting
Few-Shot
Constraint-Based
Structured Output
```

### Step 3 — Optimize

Select a prompt and improve its structure.

### Step 4 — Execute

Run the prompt against the configured AI model.

### Step 5 — Evaluate

Analyze the generated response across multiple criteria.

### Step 6 — A/B Test

Compare two prompt versions:

```text
Prompt A → Response A → Evaluation
Prompt B → Response B → Evaluation
```

This creates a simple experimental loop for improving prompt quality.

---

# 📊 Evaluation Methodology

The current evaluator uses lightweight heuristics rather than a separate AI judge.

For example, the evaluator considers signals such as:

- Prompt/response word overlap
- Response length
- Vocabulary diversity
- Presence of examples and specific details
- Structural formatting
- Presence of citations or URLs
- Instruction-oriented formatting

Scores are bounded between **1 and 10**.

The overall score is calculated as the average of the individual criteria and scaled to a 100-point range.

### Important Limitation

These metrics are **heuristic indicators**, not ground-truth measurements of response quality.

For example, a response containing a citation is not necessarily factually correct, and a longer response is not necessarily more complete.

Future versions can replace or supplement these heuristics with model-based evaluation, human feedback, benchmark datasets, or task-specific evaluation metrics.

---

# 🔮 Future Enhancements

Potential improvements for future versions include:

- [ ] LLM-based prompt optimization
- [ ] LLM-as-a-Judge evaluation
- [ ] Support for multiple AI providers
- [ ] Prompt history and version control
- [ ] Prompt templates and reusable libraries
- [ ] Export evaluation results
- [ ] Persistent experiment tracking
- [ ] Advanced A/B testing
- [ ] Batch prompt evaluation
- [ ] Custom evaluation criteria
- [ ] Human feedback scoring
- [ ] Token and latency tracking
- [ ] Cost estimation
- [ ] Prompt performance analytics
- [ ] Authentication and multi-user support
- [ ] Database-backed experiment storage

---

# 🎯 Use Cases

PromptForge can be useful for:

### 👨‍💻 Developers

Experiment with prompts used in AI-powered applications.

### 🎓 Students

Learn practical prompt engineering techniques and compare different prompting strategies.

### 🔬 Researchers

Experiment with prompt variations and response evaluation.

### 🤖 AI/ML Engineers

Prototype prompt-based workflows before integrating them into production systems.

### 🏢 Teams

Compare prompt versions and establish repeatable prompt testing workflows.

---

# 👨‍💻 Author

**Sidharth Satapathy**

Computer Science & Engineering Student
Interested in **AI/ML, Cloud Computing, Software Engineering, and Generative AI**.

---

## ⭐ If you find PromptForge useful

Give the repository a ⭐ on GitHub and feel free to contribute improvements, new evaluation strategies, and additional AI integrations.

---

### 💡 Project Vision

> **PromptForge aims to turn prompt engineering from trial-and-error experimentation into a structured process of designing, testing, evaluating, and improving AI prompts.**
