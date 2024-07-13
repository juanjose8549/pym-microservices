from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


# Test case for fetching advisors
def test_fetch_advisors():
    query = '''
    query {
        allAdvisors {
            id
            name
            expertise
        }
    }
    '''
    
    response = client.post("/", json={"query": query})

    assert response.status_code == 200
    json_data = response.json()

    assert json_data["data"]["allAdvisors"][0]["name"] == "Advisor One"
    assert json_data["data"]["allAdvisors"][1]["name"] == "Advisor Two"
