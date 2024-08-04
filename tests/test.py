import asyncio
import httpx

async def add_major(major_name: str, major_description: str):
    url = 'http://127.0.0.1:8000/majors/add/'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        "major_name": major_name,
        "major_description": major_description,
        "count_students": 0
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to add major: {response.status_code}", "details": response.text}

async def main():
    majors = [
        {"major_name": "Computer Science", "major_description": "Study of computer science"},
        {"major_name": "Mathematics", "major_description": "Study of mathematics and its applications"},
        {"major_name": "Physics", "major_description": "Study of physical laws and phenomena"},
        {"major_name": "Chemistry", "major_description": "Study of chemical substances and reactions"},
        {"major_name": "Biology", "major_description": "Study of life and living organisms"},
        {"major_name": "Economics", "major_description": "Study of production, distribution, and consumption of goods and services"},
        {"major_name": "Psychology", "major_description": "Study of human behavior and mind"},
        {"major_name": "History", "major_description": "Study of past human societies"},
        {"major_name": "Literature", "major_description": "Analysis and study of literary works"},
        {"major_name": "Sociology", "major_description": "Study of society and social relationships"},
        {"major_name": "Biohacking", "major_description": "Study of human enhancement"},
        {"major_name": "Philosophy", "major_description": "Study of fundamental questions of existence and knowledge"}
    ]

    tasks = [add_major(major["major_name"], major["major_description"]) for major in majors]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

# запуск main
if __name__ == "__main__":
    asyncio.run(main())







