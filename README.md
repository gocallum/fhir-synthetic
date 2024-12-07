# README

## FHIR Referral Generator and Sender

This Python script generates FHIR-compliant referrals and sends them to a specified API endpoint. The API URL is configurable via an `.env` file, making the script adaptable to different environments.

---

## Features

- Dynamically generates FHIR referrals using synthetic data.
- Sends the generated referrals to a specified API endpoint.
- Allows users to configure the number of referrals to send using a command-line argument.
- Supports configuration of the API URL via an `.env` file.

---

## Prerequisites

1. **Python 3.6 or higher** installed on your system.
2. **Required Python packages**:
   - `requests`
   - `python-dotenv`

   Install them using:
   ```bash
   pip install requests python-dotenv
   ```

---

## Setup Instructions

1. **Clone or download this repository**:
   ```bash
   git clone https://github.com/your-repo/fhir-referral-sender.git
   cd fhir-referral-sender
   ```

2. **Create a `.env` file**:
   - Create a file named `.env` in the root directory of the project.
   - Add the API URL to the file:
     ```
     API_URL=https://your-api-url.com/path/to/api
     ```

   Replace `https://your-api-url.com/path/to/api` with the actual API endpoint you want to use.

3. **Run the script**:
   - By default, the script sends one referral. You can run it using:
     ```bash
     python use_fhirapi.py
     ```

   - To send multiple referrals, use the `-n` or `--number` argument:
     ```bash
     python use_fhirapi.py -n 5
     ```

---

## Usage

### Command-Line Arguments

| Argument | Description                                       | Default |
|----------|---------------------------------------------------|---------|
| `-n`     | Number of referrals to generate and send.         | `1`     |

### Example Commands

1. **Send a single referral**:
   ```bash
   python use_fhirapi.py
   ```

2. **Send 10 referrals**:
   ```bash
   python use_fhirapi.py -n 10
   ```

---

## Output

For each referral, the script prints:
- Attempt number.
- Referral ID.
- Response status code from the API.
- API response content.

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

## Troubleshooting

1. **Missing API URL**:
   - Ensure the `.env` file is present and contains the `API_URL` variable.

2. **Dependency Errors**:
   - Ensure all required packages are installed:
     ```bash
     pip install requests python-dotenv
     ```

3. **API Connection Issues**:
   - Verify the API URL in the `.env` file.
   - Check your internet connection and API endpoint accessibility.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.