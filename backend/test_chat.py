import asyncio
import httpx

async def main():
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:
            print("Sending request to /chat...")
            response = await client.post(
                "http://localhost:8000/chat",
                json={"message": "Bonjour", "history": []},
                headers={"X-API-Key": "changeme-32-chars-minimum-secret"},
            )
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
