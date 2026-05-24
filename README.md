# Differential Privacy with PyTorch Opacus

> **Author: Mubashir Mohsin, Computer Science, Dalhousie University**<br>
> **Starting Date: 23 May 2026**


This repository documents the progressive learning journey and implementation of Differential Privacy (DP) using PyTorch Opacus. The ultimate objective is to master DP-SGD and advanced privacy-preserving machine learning techniques to support ongoing research and my _HealCyD (Healthcare, Cybersecurity, Data Privacy)_ research framework.

## 🗂️ Repository Structure

### The Backbone Skeleton
```
/Differential-Privacy-with-PyTorch-Opacus
├── Tutorials/                        # Progressive Opacus learning notebooks
│   ├── data/                         # Datasets used across the tutorials
│   ├── content/                      # Attachments, images, and supplementary resources
│   ├── documents/                    # Cheat sheets, DP-SGD theory, and notes
│   ├── 00_notebook.ipynb
│   ├── 01_notebook.ipynb
│   └── ...                           # (All the tutorial notebooks)
├── Projects/                         # Applied bridging projects
│   └── Deep_RL_Mini_Project/         # End-of-term Deep RL project
│       ├── data/
│       ├── src/
│       └── notebooks/
├── Specialization/                   # HealCyD framework and Medical AI focus
│   ├── HF_Base_Models/               # Workflows for Hugging Face (e.g., Llama-3-8B)
│   ├── Private_Finetuning/           # Parameter-efficient techniques (DP-LoRA)
│   └── Alignment/                    # DP-RLHF and PPO stage implementations
├── requirements.txt                  # opacus, torch, transformers, etc.
├── README.md                         # Repository roadmap and objectives
└── .gitignore
```

### 1. Tutorials
This directory contains a progressive series of Jupyter Notebooks (`.ipynb`) designed to build foundational to advanced knowledge of Opacus. Each notebook is focused, modular, and designed for a 10-15 minute learning session.
* **`data/`**: Datasets used across the tutorials.
* **`content/`**: Attachments, images, and supplementary resources for the notebooks.
* **`documents/`**: Cheat sheets, theoretical notes on DP-SGD, and official documentation summaries.

#### 🗺️ Tutorial Roadmap (In Progress)
* `00. Opacus Fundamentals - Concepts and Privacy Engine.ipynb` (✅ Completed)
* `01. Opacus Fundamentals - DP-SGD and Hyperparameters.ipynb` (✅ Completed)
* `02. Opacus Fundamentals - Model Compatibility and ModuleValidator.ipynb` (✅ Completed)
* `03. Opacus Training - End-to-End Image Classification.ipynb` (Pending)
* `04. Opacus Advanced - Custom Layers and Virtual Batch Sizes.ipynb` (Pending)
* `05. Opacus Advanced - Accounting (RDP vs PRV) and Budgeting.ipynb` (Pending)

### 2. Projects
Contains applied projects built during the learning phase, bridging the gap between isolated tutorials and full-scale implementation. This will house the Deep RL mini-project and other intermediate milestones.

### 3. Specialization
Dedicated to the intersection of Differential Privacy and Large Language Models, serving as the technical foundation for securing medical AI systems.
* **Medical LLMs**: Training and aligning domain-specific models.
* **DP-RLHF & PPO Stages**: Applying strict privacy constraints to Reinforcement Learning from Human Feedback.
* **Hugging Face Integration**: Workflows for base models like Llama-3-8B.
* **Private Fine-Tuning**: Parameter-efficient private fine-tuning techniques (e.g., DP-LoRA).
