🌍 Autonomous Climate Disaster Risk Intelligence System

A research-oriented multi-agent framework for statistically robust climate disaster trend analysis integrating classical statistical testing, structured reasoning, and LLM-assisted interpretation.

This project investigates the detection of significant long-term trends in climate disaster frequency using multi-method validation and interpretable AI orchestration.

🚀 Live Demo

🔗 (https://geetha-03--climate-disaster-risk-intelligence-app-16bgzb.streamlit.app/)

🎯 Research Motivation

Climate disaster trend detection is statistically challenging due to:

Non-normal distributions

Autocorrelation

Structural shifts

Gradual vs abrupt regime changes

Single-method inference can produce unstable conclusions.

This project explores a multi-method statistical triangulation approach combined with LLM-based structured reasoning to produce robust, interpretable risk assessments.

🧠 Core Research Question

Can multi-method statistical validation combined with structured LLM auditing improve interpretability and robustness in climate disaster trend detection?

🏗 Methodological Framework

The system implements a modular LangGraph-based research pipeline:

Data Ingestion
→ Yearly Aggregation
→ Linear Regression Trend Estimation
→ Mann–Kendall Non-Parametric Trend Test
→ Mean Shift T-Test (Structural Comparison)
→ Deterministic Risk Classification
→ Confidence Scoring
→ LLM-Based Statistical Reflection
→ Executive Risk Interpretation

Each stage operates on a shared structured ClimateState object, enabling reproducibility and modular experimentation.

📊 Statistical Methodology
1️⃣ Linear Regression (Parametric Trend Estimation)

Estimates temporal slope of disaster frequency

Evaluates statistical significance via p-value

Sensitive to linear structure

2️⃣ Mann–Kendall Test (Non-Parametric Trend Detection)

Distribution-free

Robust to non-normality

Widely used in hydro-climatology research

Detects monotonic trends

3️⃣ Mean Shift T-Test (Structural Mean Comparison)

Splits time series into early vs recent periods

Tests for statistically significant regime-level differences

Distinguishes gradual monotonic trends from abrupt structural shifts

🔬 Statistical Triangulation Strategy

The system does not rely on a single inferential method.

Instead, it evaluates:

Agreement across parametric and non-parametric tests

Strength of evidence across p-values

Consistency between monotonic trend and mean-shift inference

Risk level and confidence are determined through deterministic rule-based logic to preserve reproducibility.

🤖 LLM-Augmented Analytical Layer

Groq-hosted LLaMA models are used for:

Cross-method consistency auditing

Statistical reasoning summarization

Interpretation of agreement/disagreement between tests

Structured executive-style synthesis

Important:

The LLM operates on computed statistical outputs and does not influence the numerical results.
This preserves methodological integrity while enhancing interpretability.

🧩 Stateful Multi-Agent Orchestration

The system is built using LangGraph with a shared ClimateState schema.

This design enables:

Explicit intermediate state tracking

Modular extensibility

Reproducible analytical pipelines

Experimental agent insertion (e.g., anomaly detection, change-point models)

🖥 Experimental Interface

A Streamlit-based interface allows interactive experimentation across:

Regions

Disaster types

Statistical configurations

Visualization is rendered dynamically using matplotlib without filesystem dependencies.

📂 Repository Structure

climate-disaster-risk-intelligence/
│
├── app.py
├── main_pipeline.py
│
├── agents/
│ ├── ingestion_agent.py
│ ├── trend_agent.py
│ ├── statistical_agent.py
│ ├── mean_shift_agent.py
│ ├── risk_agent.py
│ ├── reflection_agent.py
│ ├── interpretation_agent.py
│ └── visualization_agent.py
│
├── graph/
│ ├── climate_graph.py
│ └── state.py
│
├── llm/
│ └── groq_llm.py
│
├── data/
│ └── emdat_raw.csv
│
├── requirements.txt
└── README.md

⚙️ Reproducibility

Clone the repository:

git clone <your_repo_url>
cd climate-disaster-risk-intelligence

Install dependencies:

pip install -r requirements.txt

Create .env:

GROQ_API_KEY=your_api_key_here

Run:

streamlit run app.py

📚 Data Source

EM-DAT: The International Disaster Database
https://www.emdat.be

🔮 Future Research Extensions

Change-point detection (Bayesian structural breaks)

ARIMA / ETS time-series modeling

Robust regression under heteroskedasticity

Bootstrapped significance validation

Anomaly detection via isolation forest

Cross-region comparative modeling

Automated statistical method selection

💡 Research Contributions

Hybrid symbolic-statistical + LLM analytical framework

Multi-method statistical triangulation approach

Deterministic risk classification with confidence scoring

Interpretable AI-assisted trend auditing

Modular stateful agent architecture for experimentation
