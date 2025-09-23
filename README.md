# OCR Transaction Analyzer

Proof of Concept (POC) to process transaction receipts using **OCR** and business rules.  
The system extracts key data (date, sender, recipient, amount, folio) from a receipt and determines whether the transaction should be **pre-approved, rejected, or sent for manual review**.

---

## 🚀 Features

- Generate fake transaction receipts for testing.
- OCR with two backends:
  - **Mock OCR** (hardcoded text for quick tests).
  - **AWS Textract** (pending account activation).
- Regex-based parser to convert plain text into structured JSON.
- Business rules scorer:
  - Rejects if data is missing or the date is invalid.
  - Flags manual review if amount > $10,000.
  - Pre-approves if all rules are satisfied.
- Orchestrated pipeline with a single entry point (`main.py`).
- Modular structure with `src/` and `tests/`.

---

## 📂 Project Structure

ocr-transaction-analyzer/
│
├── main.py # Entry point
├── samples/ # Test receipts
│ └── comprobante_120.jpg
│
├── src/
│ ├── config.py # Loads credentials from .env
│ ├── parser.py # Converts plain text to JSON
│ ├── pipeline.py # Orchestrates the entire flow
│ ├── scorer.py # Applies business validation rules
│ └── utils/
│ ├── generar_comprobantes.py # Fake receipt generator
│ ├── ocr_mock.py # Simulated OCR (hardcoded text)
│ └── ocr_extractor.py # AWS Textract integration (TODO)
│
├── tests/
│ └── test_connection.py # AWS S3/Textract connection test
│
└── README.md


---

## 📊 System Flow

```mermaid
flowchart TD

    A[📄 Receipt (image/PDF)] --> B[🔍 OCR]
    B -->|Mock (simulated)| B1[Extracted text (mock)]
    B -->|AWS Textract (TODO)| B2[Extracted text (real)]

    B1 --> C[📝 Parser]
    B2 --> C[📝 Parser]

    C -->|Regex + rules| D{Structured JSON}
    D --> E[⚖️ Scorer]

    E -->|Amount > 10,000| F[❗ Manual Review]
    E -->|Invalid date or missing fields| G[❌ Rejected]
    E -->|All rules passed| H[✅ Pre-approved]

    H --> I[📊 Final Result]
    G --> I
    F --> I
```
---

## 🛠️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ocr-transaction-analyzer.git
cd ocr-transaction-analyzer
```

### 2. Create virtualenv
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
### 2. Install requirements
```bash
pip install -r requirements.txt
```

```bash
AWS_ACCESS_KEY_ID=your-key
AWS_SECRET_ACCESS_KEY=your-secret
AWS_REGION=us-east-1
```
```bash
python main.py --file samples/comprobante_120.jpg --backend mock
```
```bash
python main.py --file samples/comprobante_120.jpg --backend aws
```

## 🗺️ Roadmap

1. **Mock POC** → Implement the full flow using a simulated OCR (mock).  
2. **AWS Textract Integration** → Replace the mock with real OCR extraction.  
3. **Persistence Layer** → Store structured results into a database.  
4. **REST API** → Expose the service using Flask or FastAPI.  
5. **Frontend Demo** → Build a simple dashboard for uploading and validating receipts.  


## 📚 Tech Stack

- **Languages:** Python  
- **Backend Frameworks:** Flask (future), FastAPI (future)  
- **Frontend Frameworks:** Angular (for potential dashboard)  
- **Orchestration / Automation:** argparse (CLI), n8n (future integration)  
- **OCR:** Mock (current), AWS Textract (future)  
- **Infrastructure:** AWS S3, IAM, (future) Bedrock/SageMaker  
- **Libraries:** LangChain, LangGraph, Regex, boto3  
- **Testing:** pytest