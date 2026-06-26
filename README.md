# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

The **AI-Powered Customer Support Automation System** is a LangGraph-based intelligent workflow designed to automate customer support operations for **ABC Technologies**, a Software-as-a-Service (SaaS) company providing cloud-based business management software.

The system automatically classifies customer queries, routes them to the appropriate support department, retrieves relevant information from company documents using Retrieval-Augmented Generation (RAG), stores customer conversation history using SQLite memory, performs Human-in-the-Loop approval for high-risk requests, and generates a final customer response through a Supervisor Agent.

This project was developed as part of the LangGraph Assignment.

---

# Business Problem

ABC Technologies receives a large number of customer support requests every day related to:

* Product information
* Pricing plans
* Technical issues
* Billing and refund requests
* Account management

Handling these requests manually increases response time and operational cost.

This project automates the complete support workflow using AI Agents built with LangGraph.

---

# Project Objectives

The system performs the following tasks:

* Accept customer queries
* Identify customer intent
* Route requests to the appropriate department
* Retrieve relevant information using RAG
* Maintain customer conversation history using SQLite
* Handle high-risk requests using Human-in-the-Loop approval
* Generate professional customer responses

---

# Features

* LangGraph-based workflow
* Intent Classification Agent
* Conditional Routing
* Specialized Support Agents

  * Sales Agent
  * Technical Support Agent
  * Billing Agent
  * Account Support Agent
* Retrieval-Augmented Generation (RAG)
* Chroma Vector Database
* HuggingFace Embeddings
* SQLite Conversation Memory
* Human-in-the-Loop Approval Workflow
* Supervisor Agent for response validation
* Persistent conversation history

---

# Technologies Used

* Python 3.x
* LangGraph
* LangChain
* Groq LLM
* ChromaDB
* HuggingFace Embeddings
* SQLite
* PyPDFLoader
* Recursive Character Text Splitter

---

# Project Structure

```text
AI-Customer-Support-Automation/

├── app.py
├── graph.py
├── config.py
├── state.py
├── build_vectorstore.py
├── memory.db
├── requirements.txt
│
├── documents/
│   ├── CompanyPolicy.pdf
│   ├── PricingGuide.pdf
│   ├── TechnicalManual.pdf
│   └── FAQ.pdf
│
├── nodes/
│   ├── classifier.py
│   ├── router.py
│   ├── sales_agent.py
│   ├── technical.py
│   ├── billing_agent.py
│   ├── account_agent.py
│   ├── rag.py
│   ├── approval.py
│   ├── human_review.py
│   ├── supervisor.py
│   ├── memory.py
│   └── final_response.py
│
└── vectorstore/
```

---

# Workflow

1. Customer submits a support query.
2. Intent Classification Agent identifies the request type.
3. LangGraph routes the request to the appropriate department.
4. Relevant information is retrieved from the knowledge base using RAG.
5. High-risk requests are sent for Human Approval.
6. Supervisor Agent validates the generated response.
7. Conversation history is stored in SQLite memory.
8. Final response is returned to the customer.

---

# Knowledge Base Documents

The RAG pipeline retrieves information from the following documents:

* CompanyPolicy.pdf
* PricingGuide.pdf
* TechnicalManual.pdf
* FAQ.pdf

---

# Human-in-the-Loop Requests

The following requests require manual approval:

* Refund Requests
* Subscription Cancellation
* Account Closure
* Compensation Requests
* Escalation to Management

---

# Memory Implementation

The project stores customer conversation history using SQLite.

Example:

Customer:

```
My name is David. I have a billing issue.
```

Later:

```
What was my previous support issue?
```

The system retrieves the previous interaction from SQLite memory.

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Customer-Support-Automation-LangGraph.git

cd AI-Customer-Support-Automation-LangGraph
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```text
GROQ_API_KEY=your_groq_api_key
```

---

## 5. Build the Vector Database

```bash
python build_vectorstore.py
```

This indexes all PDF documents and creates the Chroma vector database.

---

## 6. Run the Project

```bash
python app.py
```

---

# Sample Queries

Sales

```
What are the pricing plans available for your software?
```

Account

```
I forgot my account password.
```

Technical Support

```
My application crashes whenever I upload a file.
```

Billing (Human Approval)

```
I need a refund for my annual subscription.
```

Memory

```
What was my previous support issue?
```

---

# Expected Workflow

```
Customer Query

↓

Intent Classification

↓

Conditional Routing

↓

Support Agent

↓

RAG Retrieval

↓

Human Approval (if required)

↓

Supervisor Agent

↓

SQLite Memory

↓

Final Customer Response
```

---

# Future Improvements

* Multi-language customer support
* Voice-based support interface
* Email and chatbot integration
* Sentiment Analysis
* Ticket Prioritization
* Admin Dashboard
* Analytics and Reporting

---

