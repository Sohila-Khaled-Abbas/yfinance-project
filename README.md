# 📈 Finance BI Project  

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?logo=python&logoColor=white)  
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow?logo=powerbi)  
![Prefect](https://img.shields.io/badge/Prefect-Orchestration-brightgreen?logo=prefect)  
![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)  
![Tests](https://github.com/your-username/finance-bi-project/actions/workflows/tests.yml/badge.svg)  

---

## 🚀 Overview  

This project demonstrates an **end-to-end Finance Analytics solution**:  
🔹 **Python + yfinance** for financial data extraction  
🔹 **Prefect** for automation and scheduled refresh  
🔹 **Power BI** for data storytelling (Executive & Quant dashboards)  

The goal: **turn raw stock market data into insights** that help executives make strategic decisions and analysts perform deeper financial analysis.  

---

## 🛠️ Tech Stack  

| Layer               | Tool/Library                                             | Purpose                          |
| ------------------- | -------------------------------------------------------- | -------------------------------- |
| **Data Extraction** | [yfinance](https://github.com/ranaroussi/yfinance)       | Download OHLCV stock data        |
| **Orchestration**   | [Prefect](https://www.prefect.io/)                       | Schedule automated pipeline runs |
| **Storage**         | CSV / Parquet (via [pandas](https://pandas.pydata.org/)) | Efficient storage for BI         |
| **Visualization**   | [Power BI](https://powerbi.microsoft.com/)               | Executive and Quant dashboards   |
| **Testing**         | [pytest](https://docs.pytest.org/)                       | Unit testing of pipeline modules |

---

## 📂 Repository Structure  

```bash
finance-bi-project/
├── data/            # Raw + processed datasets
├── notebooks/       # Exploratory notebooks
├── src/             # Modular Python pipeline
├── tests/           # Unit tests
├── dashboards/      # Power BI dashboards (.pbix)
├── requirements.txt # Python dependencies
├── LICENSE
└── README.md
```

---

## 📊 Dashboards

### Executive Dashboard

✅ **KPIs**: YTD Return, Volume, Volatility
📈 **Charts**: Line (Price vs MA), Area (Cumulative Return)

### 📊 Quant Dashboard

📉 **Risk-Return Scatter**
📊 **Correlation Heatmap**
🕯️ **Candlestick OHLCV**
📦 **Return Distribution (Boxplot)**

---

## ⚙️ Setup & Installation

1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/finance-bi-project.git
cd finance-bi-project
```

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Run pipeline

```bash
python src/pipeline_prefect.py
```

---

## 🔄 Automation with Prefect

```bash
prefect deployment build src/pipeline_prefect.py:finance_pipeline -n finance-pipeline
prefect deployment apply finance_pipeline-deployment.yaml
prefect agent start -q "default"
```

---

## ✅ Testing

Run tests with:

```bash
pytest tests/
```

---

## 🛣️ Roadmap

- [ ] Integrate fundamentals (P/E, EPS)
- [ ] Add sector benchmarks
- [ ] CI/CD with GitHub Actions (lint + tests)
- [ ] Cloud storage integration (S3/GCS/Azure)

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch
3. Submit a PR 🚀

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
