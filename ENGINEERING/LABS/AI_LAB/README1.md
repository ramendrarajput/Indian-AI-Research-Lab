# 🕉️ Project BRAHMA

> **B**harat **R**esearch **A**nd **H**olistic **M**ulti-Agent **A**I

### Building an Open, Modular and Production-Ready AI Operating System from India 🇮🇳

---

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![Google](https://img.shields.io/badge/Google-Gemini-orange)
![Architecture](https://img.shields.io/badge/Architecture-Modular-success)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

![GitHub last commit](https://img.shields.io/github/last-commit/ramendrarajput/Indian-AI-Research-Lab)
![GitHub commit-activity](https://img.shields.io/github/commit-activity/m/ramendrarajput/Indian-AI-Research-Lab)
![GitHub repo size](https://img.shields.io/github/repo-size/ramendrarajput/Indian-AI-Research-Lab)
![GitHub code size](https://img.shields.io/github/languages/code-size/ramendrarajput/Indian-AI-Research-Lab)
![GitHub top language](https://img.shields.io/github/languages/top/ramendrarajput/Indian-AI-Research-Lab)
![GitHub language count](https://img.shields.io/github/languages/count/ramendrarajput/Indian-AI-Research-Lab)

---

# 🚀 Repository Banner

> *(Coming Soon)*

```
assets/banner.png
```

---

# 🌟 About Project BRAHMA

Project BRAHMA is an open-source, modular Artificial Intelligence platform being developed under the **Indian AI Research Lab** initiative.

Its objective is to build a production-grade AI ecosystem capable of integrating modern Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Multi-Agent Systems, Computer Vision, Voice Intelligence, Knowledge Retrieval, and domain-specific Expert Systems into one unified architecture.

Rather than being a single chatbot, Project BRAHMA is designed as a complete AI Operating System where individual AI capabilities work together through a scalable modular architecture.

---

# 🎯 Vision

Our long-term vision is to build an open AI platform from India that enables developers, researchers, students, organizations, and government institutions to create intelligent AI applications without rebuilding the core infrastructure every time.

Project BRAHMA emphasizes:

- Modular Architecture
- Reusable AI Components
- Multi-Agent Intelligence
- Production Engineering
- Open Source Collaboration
- Indian Research & Innovation

---

# 💡 Why Project BRAHMA?

Modern AI projects often become difficult to maintain because all AI logic, APIs, prompts, memory, and workflows are tightly coupled into a single application.

Project BRAHMA solves this by separating every major responsibility into independent modules.

This architecture makes the platform:

- Easy to maintain
- Easy to extend
- Easier to test
- Easier to deploy
- Ready for future AI providers

---

# ✨ Current Features

## Core AI

- Google Gemini Integration
- Unified AI Gateway
- Modular LLM Architecture
- Prompt Management
- Persistent Conversation Memory

## Knowledge & Research

- Wikipedia Search
- Research Agent
- arXiv Research Agent
- PDF Question Answering
- Retrieval-Augmented Generation (RAG)

## Multi-Agent System

- Agentic AI
- Multi-Agent Workflow
- Finance Agent
- Stock Investment Adviser
- Recipe Agent
- Medical Diagnosis Agent

## Vision & Media

- Image Understanding
- Image Generation
- Image Editing
- Image-to-Video
- Text-to-Image

## Voice

- Speech-to-Text
- Text-to-Speech
- Voice Assistant

## Utilities

- Environment Validation
- Modular Services
- Centralized Configuration
- FAISS Vector Database
- Production Memory Engine

---

# 🔥 Upcoming Features

- LangGraph Integration
- CrewAI Workflows
- Google ADK
- Model Context Protocol (MCP)
- Local LLM Support
- Ollama Integration
- Deep Research Agent
- Autonomous Planning Agent
- Long-Term Memory Engine
- AI Workflow Automation

---

# 📊 Project Highlights

| Category | Status |
|-----------|--------|
| Architecture | ✅ Modular |
| AI Provider | Google Gemini |
| Memory | Persistent |
| Vector Database | FAISS |
| UI | Streamlit |
| Agent Framework | Custom |
| Configuration | Centralized |
| Documentation | Active |
| License | MIT |

---

# ⭐ Project Goals

Project BRAHMA is not intended to be "another chatbot."

Its goal is to become a complete AI platform capable of supporting:

- AI Research
- AI Education
- AI Automation
- AI Assistants
- Expert Systems
- Enterprise AI
- Government AI Solutions
- Personal AI Workflows

---

# 🏗️ System Architecture

Project BRAHMA follows a layered modular architecture where every major component has a single responsibility.

```text
                        User
                         │
                         ▼
                 Streamlit Interface
                         │
                         ▼
                Navigation / UI Pages
                         │
                         ▼
                  AI Gateway (core/)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   Gemini Provider   Future Providers   Local Models
                         │
                         ▼
                  Agent Framework
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
    Research       Expert Systems     Automation
      Agents
                         │
                         ▼
              Memory + RAG + Services
                         │
                         ▼
                 FAISS / Knowledge Base
                         │
                         ▼
                    Final Response
```

The architecture is designed so that new AI providers, agents, or expert systems can be integrated without affecting the existing codebase.

---

# 🧩 Architecture Principles

Project BRAHMA is built around a few core engineering principles.

### Separation of Concerns

Every module has a clearly defined responsibility.

- `config/` → Configuration
- `core/` → Reusable AI logic
- `services/` → External services
- `agents/` → AI Agents
- `ui/` → Streamlit interface
- `utils/` → Utility functions

---

### Modular Design

Every AI capability is implemented as an independent module.

Examples:

- Research Agent
- Wikipedia Service
- Speech Service
- Memory Engine
- Image Analysis
- RAG Engine

Each module can evolve independently.

---

### Provider Independence

The project is designed to support multiple AI providers.

Current provider:

- Google Gemini

Future providers:

- OpenAI
- Groq
- Ollama
- Hugging Face
- Anthropic Claude
- Azure OpenAI

Switching providers should require minimal code changes.

---

# 🧠 AI Provider Architecture

```text
User Request
      │
      ▼
AI Gateway
      │
      ▼
Provider Router
      │
 ┌────┴────┐
 ▼         ▼
Gemini   Future Providers
```

All AI requests pass through a centralized AI layer before reaching the provider.

This makes the application easier to maintain and extend.

---

# 🗂️ Project Structure

```text
Indian-AI-Research-Lab/

├── agents/                # AI agents
├── assets/                # Images, icons, banners
├── config/                # Project configuration
├── core/                  # Core AI engine
├── data/                  # Project datasets
├── docs/                  # Documentation
├── faiss_index/           # Vector database
├── logs/                  # Application logs
├── output/                # Generated outputs
├── prompts/               # Prompt templates
├── services/              # External services
├── tests/                 # Unit tests
├── tools/                 # Utility tools
├── ui/                    # Streamlit interface
├── utils/                 # Helper utilities

├── app.py
├── README.md
├── requirements.txt
└── .env.example
```

---

# ⚙️ Installation

Clone the repository.

```bash
git clone https://github.com/ramendrarajput/Indian-AI-Research-Lab.git
```

Move into the project directory.

```bash
cd Indian-AI-Research-Lab
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

---

# 🔑 Configuration

Create a `.env` file using `.env.example`.

Example:

```env
GOOGLE_API_KEY=YOUR_API_KEY

TAVILY_API_KEY=YOUR_API_KEY

HUGGING_FACE_API_KEY=YOUR_API_KEY

ELEVENLABS_API_KEY=YOUR_API_KEY
```

Project BRAHMA automatically loads environment variables using `python-dotenv`.

---

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.12 |
| UI | Streamlit |
| LLM | Google Gemini |
| Vector Database | FAISS |
| Embeddings | Gemini Embeddings |
| RAG | LangChain |
| PDF Processing | PyPDF2 |
| AI Framework | Custom Modular Architecture |
| Version Control | Git + GitHub |

---

# 🔄 Request Flow

Every request follows a common execution pipeline.

```text
User

↓

Streamlit UI

↓

Navigation

↓

AI Gateway

↓

Agent / Service

↓

Memory

↓

RAG (Optional)

↓

Gemini

↓

Response
```

This workflow keeps business logic separated from UI logic and makes future expansion significantly easier.

---

# 🤖 AI Agents

Project BRAHMA is built around a modular AI Agent architecture.

Each agent is designed to solve a specific problem independently while sharing common AI infrastructure such as memory, prompts, provider routing, and reusable services.

Current agents include:

| Agent | Status |
|--------|--------|
| Research Agent | ✅ |
| arXiv Research Agent | ✅ |
| Finance Agent | ✅ |
| Stock Investment Adviser | ✅ |
| Medical Diagnosis Agent | ✅ |
| Recipe Maker Agent | ✅ |
| Wikipedia Agent | ✅ |
| Image Analysis Agent | ✅ |
| RAG Agent | ✅ |

Future agent modules can be added without modifying the existing architecture.

---

# 🧠 Memory Engine

Project BRAHMA includes a reusable conversation memory engine.

Current capabilities:

- Persistent conversation history
- Context-aware responses
- Modular memory management
- Session-based storage

Future roadmap:

- Long-Term Memory
- Vector Memory
- User Profiles
- Cross-session Memory
- Semantic Memory Retrieval

---

# 📚 Retrieval-Augmented Generation (RAG)

The platform includes an integrated Retrieval-Augmented Generation pipeline.

Current capabilities:

- PDF Processing
- Text Chunking
- FAISS Vector Store
- Semantic Search
- Question Answering

Future improvements:

- Hybrid Search
- Metadata Filtering
- Multi-document Search
- Citation Support
- Incremental Indexing

---

# 🖼️ Vision AI

Project BRAHMA supports multiple computer vision workflows.

Current modules:

- Image Classification
- Image Understanding
- Image-to-Image
- Text-to-Image
- Image-to-Video

Planned additions:

- OCR
- Document Intelligence
- Object Detection
- Face Analysis
- Video Understanding

---

# 🎙️ Voice AI

Voice capabilities are modularized into reusable services.

Current features:

- Speech-to-Text
- Text-to-Speech

Future roadmap:

- Voice Conversation
- Wake Word Detection
- Voice Cloning
- Multi-language Support
- Real-time Streaming

---

# 🏛 Expert Systems

One of the long-term goals of Project BRAHMA is to build domain-specific expert systems.

Current work:

- Medical Expert System
- Philosophy Expert System
- Government Expert System

Planned systems:

- Agriculture Expert
- Law Expert
- Education Expert
- Finance Expert
- Music Expert
- Astrology Expert
- Programming Expert
- Cyber Security Expert

---

# 🛣️ Development Roadmap

## ✅ Phase 1 — Foundation

- Modular Project Structure
- AI Gateway
- Centralized Configuration
- Memory Engine
- Modular Services
- Provider Architecture
- Documentation

Status: **Completed**

---

## 🚧 Phase 2 — Core Intelligence

- Research Agent
- RAG
- Multi-Agent System
- Vision AI
- Voice AI

Status: **In Progress**

---

## 🔜 Phase 3 — Autonomous AI

Planned work includes:

- LangGraph Integration
- CrewAI Workflows
- Google ADK
- MCP Integration
- Local LLM Support
- Long-Term Memory
- Autonomous Planning

---

## 🌍 Phase 4 — AI Operating System

Long-term vision:

- Enterprise AI Platform
- Government AI Solutions
- AI Automation Platform
- Knowledge Operating System
- AI Marketplace
- Plugin Ecosystem

---

# 📖 Documentation

The repository includes dedicated documentation for architecture and development.

Current documents include:

- Project Architecture
- Engineering Decisions
- Changelog
- Development Notes

Additional documentation will continue to grow as the project evolves.

---

# 🤝 Contributing

Contributions are welcome from developers, researchers, students, and AI enthusiasts.

Typical contribution workflow:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your fork
5. Open a Pull Request

Please keep contributions modular and follow the existing project architecture.

---

# 🧪 Testing (Planned)

Future releases will include:

- Unit Tests
- Integration Tests
- CI/CD Pipelines
- GitHub Actions
- Automated Code Quality Checks

Our goal is to maintain production-grade engineering standards as the project grows.

---

# 📜 License

Project BRAHMA is released under the **MIT License**.

You are free to:

- Use
- Modify
- Distribute
- Learn from
- Build upon

this project in accordance with the terms of the MIT License.

See the **LICENSE** file for complete details.

---

# 🏆 Project Philosophy

Project BRAHMA is built on a simple belief:

> **Artificial Intelligence should be modular, reusable, transparent, and accessible to everyone.**

Rather than creating isolated AI applications, Project BRAHMA focuses on building reusable AI infrastructure that can support research, education, automation, expert systems, and future intelligent applications.

---

# ❤️ Support the Project

If you find Project BRAHMA useful, please consider supporting it.

You can help by:

⭐ Starring the repository

🍴 Forking the project

🐛 Reporting issues

💡 Suggesting new ideas

📝 Improving documentation

🤝 Contributing code

Every contribution—big or small—helps improve the project.

---

# 🌍 Future Vision

Project BRAHMA is being developed with a long-term vision of becoming an open AI ecosystem from India.

Future goals include:

- AI Operating System
- Multi-Agent Platform
- Enterprise AI Framework
- Government AI Platform
- Education & Research Platform
- AI Marketplace
- Plugin Ecosystem
- Open AI Community

---

# 🙏 Acknowledgements

Project BRAHMA is inspired by the global open-source AI community.

Special thanks to the creators and maintainers of:

- Python
- Streamlit
- Google Gemini
- LangChain
- FAISS
- Hugging Face
- PyTorch
- Open Source Community

Their work has made projects like BRAHMA possible.

---

# 👨‍💻 Developer

## Ramendra Singh Rajput

AI Engineer • MCA • Government of Madhya Pradesh

Founder of **Indian AI Research Lab**

### Connect

**GitHub**

https://github.com/ramendrarajput

**LinkedIn**

https://www.linkedin.com/in/ramendra-singh-rajput-026a6a22/

**Google Developer Profile**

https://g.dev/ramendrarajput

---

# 📬 Contact

For suggestions, collaborations, or discussions:

Please open an Issue or Discussion on GitHub.

Community contributions are always welcome.

---

# 📈 Current Development Status

Project BRAHMA is under active development.

The architecture is stable, while new AI capabilities are continuously being added.

Current focus areas include:

- Multi-Agent Intelligence
- Deep Research
- AI Automation
- Long-Term Memory
- Local LLM Integration
- Production Engineering

---

# 🚀 Version

Current Development Version

**v0.1.0-alpha**

---

# ⭐ If You Like This Project...

Please consider giving the repository a ⭐ on GitHub.

It helps more developers discover the project and motivates future development.

---

<div align="center">

# 🕉️ Project BRAHMA

### **Building the Future of Artificial Intelligence from India 🇮🇳**

**Made with ❤️ using Python, Streamlit and Google Gemini**

---

*"Knowledge becomes powerful only when it is shared."*

</div>