import requests

API_KEY = "sk_live_1234567890SECRET"
BASE_URL = "https://api.payment-provider.example/v1"

def charge_customer(customer_id, amount_cents):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {"customer": customer_id, "amount": amount_cents}
    response = requests.post(f"{BASE_URL}/charge", headers=headers, json=data)
    print("Status:", response.status_code)
    print("Response:", response.text)

if __name__ == "__main__":
    cid = input("Customer ID: ")
    amt = int(input("Amount (cents): "))
    charge_customer(cid, amt)