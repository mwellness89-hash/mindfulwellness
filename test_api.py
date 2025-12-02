"""
Simple API Tests for MindfulWellness MVP (100% FREE)
Run: python test_api.py
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    print("\n1. Testing HEALTH endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200

def test_mood_checkin():
    print("\n2. Testing MOOD CHECK-IN endpoint (Powered by Groq FREE)...")
    data = {
        "user_id": "test_user_001",
        "mood_score": 6,
        "stress_reason": "Stressed about monthly bills and EMI"
    }
    response = requests.post(f"{BASE_URL}/api/mood-checkin", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["mood_logged"] == True

def test_thought_reframe():
    print("\n3. Testing THOUGHT REFRAME endpoint (Powered by Groq FREE)...")
    data = {
        "user_id": "test_user_001",
        "negative_thought": "My financial situation is hopeless and will never improve"
    }
    response = requests.post(f"{BASE_URL}/api/thought-reframe", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert len(response.json()["alternatives"]) > 0

def test_financial_leaks():
    print("\n4. Testing FINANCIAL LEAK FINDER endpoint (Powered by Groq FREE)...")
    csv_data = """Date,Merchant,Amount,Category
2025-01-15,Netflix,-499,Entertainment
2025-01-15,Gym App,-299,Health
2025-01-16,Netflix,-499,Entertainment
2025-01-20,Unknown Subscription,-1499,Other
2025-01-25,Gym App,-299,Health"""
    
    data = {
        "user_id": "test_user_001",
        "csv_data": csv_data
    }
    response = requests.post(f"{BASE_URL}/api/financial-leaks", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200

def test_find_match():
    print("\n5. Testing FIND MATCH endpoint (Peer matching)...")
    data = {
        "user_id": "test_user_001",
        "profession": "Software Engineer",
        "salary_range": "200k-250k",
        "main_stress": "debt",
        "mood_average": 6
    }
    response = requests.post(f"{BASE_URL}/api/find-match", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["match_score"] > 0
    print("✅ FIND MATCH test passed")

def test_send_message():
    print("\n6. Testing SEND MESSAGE endpoint (Anonymous chat)...")
    data = {
        "sender_id": "anon_user_001",
        "match_id": 1,
        "message": "Hey, I also struggle with financial stress. How are you coping?"
    }
    response = requests.post(f"{BASE_URL}/api/send-message", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    assert response.status_code == 200
    assert response.json()["success"] == True
    print("✅ SEND MESSAGE test passed")

if __name__ == "__main__":
    try:
        test_health()
        test_mood_checkin()
        test_thought_reframe()
        test_financial_leaks()
        test_find_match()
        test_send_message()
        print("\n" + "="*50)
        print("✅ ALL 6 TESTS PASSED!")

        print("💰 COST: $0")
        print("🚀 POWERED BY: Groq (Free)")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")

