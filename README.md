Here’s an updated `README.md` for your repository that incorporates the updates you’ve shared, including Python 3.12 and the revised `requirements.txt`.

---

# FHIR Synthetic Data Generator

This repository contains a Python-based tool to generate FHIR-compliant synthetic data and send it to a configurable API endpoint. It is designed to simulate healthcare referrals for testing and development purposes.

---

## Features

- Generates FHIR-compliant synthetic referrals using the `faker` library.
- Sends the generated referrals to a specified API endpoint via HTTP POST requests.
- API endpoint is configurable using a `.env` file.
- Supports configurable referral generation via command-line arguments.

---

## Prerequisites

1. **Python 3.12** or higher installed on your system. [Download Python](https://www.python.org/downloads/).
2. **Required Python libraries**:
   - `requests`
   - `python-dotenv`
   - `faker`

---

## Setup Instructions

### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/gocallum/fhir-synthetic.git
cd fhir-synthetic
```

### Create a Virtual Environment
It is recommended to use a virtual environment:
```bash
python3.12 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### Configure the `.env` File
Create a `.env` file in the root directory and specify the API URL:
```
API_URL=https://your-api-url.com/path/to/api
```
Replace `https://your-api-url.com/path/to/api` with the actual API endpoint where the referrals will be sent.

---

## Usage

Run the script to generate and send referrals:

### Command-Line Arguments

| Argument         | Description                                         | Default |
|------------------|-----------------------------------------------------|---------|
| `-n`, `--number` | Number of referrals to generate and send.           | `1`     |

### Example Commands

1. **Send a Single Referral**:
   ```bash
   python use_fhirapi.py
   ```

2. **Send Multiple Referrals**:
   ```bash
   python use_fhirapi.py -n 5
   ```

---

## Output

For each referral, the script outputs:
- **Attempt Number**: The index of the referral attempt.
- **Referral ID**: The unique identifier of the generated referral.
- **Response Status Code**: The HTTP status code returned by the API.
- **Response Content**: The content returned by the API.

### Example Output
```
Attempt 1:
Referral ID: AURF-123
Response Status Code: 200
Response Content: {"status": "success"}
--------------------------------------------------
Attempt 2:
Referral ID: AURF-456
Response Status Code: 200
Response Content: {"status": "success"}
--------------------------------------------------
```

---

## Development Notes

### Folder Structure
- **`generate_fhir_ref.py`**: Contains the logic for generating synthetic FHIR referrals.
- **`use_fhirapi.py`**: The main script for sending referrals to the API.
- **`lib/common_health.py`**: Utility functions for generating healthcare-specific synthetic data.

### Adding More Dependencies
If you need additional dependencies, add them to `requirements.txt` and run:
```bash
pip install -r requirements.txt
```

### Debugging
Ensure that all log outputs (e.g., errors, stack traces) are visible in your terminal or your AWS CloudWatch logs when using this in a Lambda function.

---

## Troubleshooting

1. **Missing API URL**:
   - Ensure the `.env` file exists and contains the correct `API_URL` variable.
   - Example:
     ```
     API_URL=https://your-api-url.com/path/to/api
     ```

2. **Dependency Errors**:
   - Ensure all required libraries are installed:
     ```bash
     pip install -r requirements.txt
     ```

3. **Incorrect Python Version**:
   - Verify that you are using Python 3.12 or higher:
     ```bash
     python --version
     ```

---

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and create a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to copy and paste this updated README into your repository! It incorporates the use of Python 3.12, highlights the `.env` configuration, and reflects the current state of the project.