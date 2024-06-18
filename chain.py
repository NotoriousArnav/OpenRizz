from llm import llm
from prompt import prompt
from parse_output_to_json import parse_output_to_json, json

chain = prompt | llm | parse_output_to_json

if __name__ == "__main__":
    response = chain.invoke(
        {
            "description": "Aditi is a Cute girl from South Kolkata. She is 5'9 and a Content Writer",
            "response_type": "Pickup Line, funny"
        }
    )

    output = parse_output_to_json(response.content)

    print(json.dumps(output))
