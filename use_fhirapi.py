import requests
import json
import argparse
from generate_fhir_ref import generate_referral
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def send_referral(api_url, referral):
    """Send the referral to the specified API."""
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(api_url, headers=headers, data=json.dumps(referral))
    return response

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate and send FHIR referrals.")
    parser.add_argument("-n", "--number", type=int, default=1, 
                        help="Number of referrals to generate and send (default: 1).")
    args = parser.parse_args()

    # Get API URL from environment variables
    api_url = os.getenv("API_URL")
    if not api_url:
        print("Error: API_URL not found in environment variables. Please check your .env file.")
        return

    # Generate and send referrals
    for i in range(args.number):
        referral = generate_referral()
        response = send_referral(api_url, referral)
        print(f"Attempt {i + 1}:")
        print(f"Referral ID: {referral['id']}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")
        print("-" * 50)

if __name__ == "__main__":
    main()
