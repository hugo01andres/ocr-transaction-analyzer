# OCR Transaction Analyzer

🚀 Proof of Concept (POC) for automating **financial transaction compliance** using **OCR + AI**.  
The system extracts key data from money transfer receipts, applies risk scoring rules, and generates automatic explanations with a Large Language Model (LLM).  
This reduces the need for manual compliance agents to review every receipt image in detail.

---

## 📖 Problem Statement

In fintech and remittance companies, compliance teams must review transaction receipts to detect fraud and comply with AML regulations.  
Today, this process is often **manual, slow, and expensive**:
- Analysts open receipt images one by one.  
- They confirm **amount, sender, receiver, and date**.  
- They decide whether the case is low or high risk.  

This approach does not scale when processing thousands or millions of transactions per day.

---

## 🎯 POC Objective

The goal of this POC is to **simulate an automated pre-approval system** where:
- OCR extracts transaction data from receipt images.  
- A scoring module classifies the risk: `AUTO_APPROVED`, `REQUIRES_REVIEW`, or `REJECTED`.  
- An AI model generates a short compliance explanation.  
- Human reviewers only see structured data (amount, sender, receiver, date), not the full image — unless needed for audit.  

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **pytesseract + Pillow** → OCR engine  
- **LangChain + OpenAI GPT** → AI explanations  
- **Regex + simple rules** → risk scoring  
- **JSON output / SQLite (optional)** → persistence  

---

## ⚙️ How It Works (Flow)


Example output:

```json
{
  "transaction_id": "tx_20250921_001",
  "amount": 750.0,
  "currency": "USD",
  "date": "2025-09-21",
  "sender_name": "Juan Pérez",
  "receiver_name": "Maria Lopez",
  "score_label": "REQUIRES_REVIEW",
  "score_reason": "amount_above_threshold",
  "explanation": "The transaction exceeds the $500 threshold and requires additional review.",
  "ocr_text_snippet": "Monto: $750.00 USD\nFecha: 21/09/2025..."
}

---

## 📂 Repository Structure
ocr-transaction-analyzer/
│── pipeline.py             # Main pipeline (OCR → parser → scoring → AI)
│── generar_comprobantes.py # Script to generate fake receipts for testing
│── requirements.txt        # Python dependencies
│── samples/                # Example receipt images
│── docs/
│   └── POV_Scope.md        # POC Scope & Value document (AS-IS vs TO-BE)

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-user/ocr-transaction-analyzer.git
cd ocr-transaction-analyzer
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

Dependencies include:
- **easyocr** → OCR engine (pure Python, no extra installs)
- **langchain + openai** → AI explanations
- **pillow** → image handling

### 4. Generate sample receipts
```bash
python generar_comprobantes.py
```

This will create images like `samples/comprobante_750.jpg`.

### 5. Run the pipeline
```bash
python pipeline.py samples/comprobante_750.jpg
```

Expected output: structured JSON with amount, risk score, and AI explanation.

---

## ✅ Acceptance Criteria

- OCR with **EasyOCR** extracts **amount, sender, receiver, date** from receipt images.  
- Apply simple risk rules:  
  - ≤ 500 USD → `AUTO_APPROVED`  
  - 500–5000 USD → `REQUIRES_REVIEW`  
  - > 5000 USD → `REJECTED`  
- Generate **short AI explanation** (1–2 lines) with LangChain + GPT.  
- Output in **structured JSON** format for compliance teams.  
- Reviewer sees structured fields only (no need to open full image).  
- Processing time per receipt < 5 seconds in local environment.

---

## 📈 Roadmap (Future Work)

- 🔄 Replace EasyOCR with **AWS Textract** for production-grade OCR.  
- ☁️ Deploy pipeline on **AWS Lambda** (serverless) or **ECS** for scalability.  
- 🤖 Add ML-based **risk scoring** (e.g., LightGBM on historical transactions).  
- 🖥️ Build a small **web dashboard** for compliance reviewers (queue view).  
- 🔐 Implement **audit logging**, **access control**, and **data encryption**.  
- 📊 Add monitoring & metrics (accuracy, false positives, processing time).  
- 🌍 Extend language support for receipts in Spanish, English, and Portuguese.



