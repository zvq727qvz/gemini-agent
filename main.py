import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


def main():
    load_dotenv()

    args = []
    has_verbose = False

    try:
        has_verbose = "--verbose" in sys.argv

        for arg in sys.argv[1:]:
            if not arg.startswith("--"):
                args.append(arg)

    except:
        print("user prompt not provided")
        sys.exit(1)

    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, user_prompt, has_verbose)

def generate_content(client, messages, user_prompt, has_verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages
    )

    if has_verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
