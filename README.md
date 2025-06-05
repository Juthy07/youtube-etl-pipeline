# YouTube ETL Pipeline with Python, AWS & Docker 🚀

This project is a complete ETL (Extract, Transform, Load) pipeline that fetches YouTube video data based on a search query, processes it, and uploads it as a CSV file to an AWS S3 bucket. The entire workflow is containerized using Docker for portability and deployment.

---

## 📌 Features

- 🔍 Extracts real-time video data using the YouTube Data API
- 🧹 Transforms and enriches the data using Pandas
- ☁️ Uploads cleaned data to AWS S3 using `boto3`
- 🐳 Dockerized for easy execution anywhere
- 🛠️ Modular design with reusable scripts

---

## 📂 Project Structure

```
youtube-etl-project/
│
├── etl/
│   ├── extract.py       # Extract video data using YouTube API
│   ├── transform.py     # Clean and enhance the data
│   └── load.py          # Upload CSV to S3
│
├── config/
│   └── config.py        # API key configuration
│
├── data/                # Stores local CSVs
├── run_pipeline.py      # Main ETL runner script
├── Dockerfile           # Docker setup
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🚀 How to Run

### ✅ Locally (with Python)

1. Set AWS credentials in PowerShell or terminal:

   ```bash
   $env:AWS_ACCESS_KEY_ID="your-key"
   $env:AWS_SECRET_ACCESS_KEY="your-secret"
   $env:AWS_DEFAULT_REGION="your-region"
   ```

2. Run the pipeline:
   ```bash
   python run_pipeline.py
   ```

---

### 🐳 With Docker

1. Build the image:

   ```bash
   docker build -t youtube-etl .
   ```

2. Run the container:
   ```bash
   docker run -e AWS_ACCESS_KEY_ID=your_key -e AWS_SECRET_ACCESS_KEY=your_secret youtube-etl
   ```

---

## 🧠 Skills Demonstrated

- Python Scripting & API Integration
- Data Engineering Workflow (ETL)
- AWS Cloud (S3, IAM)
- Docker & Containerization
- Modular Code Structure

---

## 📈 Sample Output

A `.csv` file is saved locally and uploaded to your configured AWS S3 bucket. Example columns:

- `VideoID`
- `Title`
- `PublishedDate`
- `Channel`
- `SearchQuery`

---

## 📬 Contact

Built with ❤️ by [Juthy Shaji](https://github.com/Juthy07)  
🔗 [LinkedIn](https://www.linkedin.com/in/juthy-shaji/)  
📧 juthy07shaji@gmail.com

---

## 📄 License

This project is for educational and portfolio use. Feel free to fork and adapt!
