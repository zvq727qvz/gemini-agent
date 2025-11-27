import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions
from config import MAX_LOOPS

messages = []


def main():
    try:
        load_dotenv()
        loop_count = 0

        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        user_prompt, verbose = get_user_prompt()

        messages.append(
            types.Content(role="user", parts=[types.Part(text=user_prompt)])
        )

        while True:
            loop_count += 1
            if loop_count >= MAX_LOOPS:
                print("Max loop count reached. Goodbye")
                sys.exit(1)

            final_response = generate_content(client, verbose)

            if final_response:
                print(f"Model: {final_response}")
                break

    except Exception as e:
        return f"Error: during main runtime: {e}"


def get_user_prompt():
    try:
        verbose = "--verbose" in sys.argv
        args = []
        for arg in sys.argv[1:]:
            if not arg.startswith("--"):
                args.append(arg)

        if not args:
            print("AI Code Assistant")
            print('\nUsage: python main.py "your prompt here" [--verbose]')
            print('Example: python main.py "How do I fix the calculator?"')
            sys.exit(1)

        user_prompt = " ".join(args)

        print(f"User: {user_prompt}")

        return user_prompt, verbose
    except Exception as e:
        return f"Error: getting user_prompt: {e}"


def generate_content(client, verbose):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )
        if verbose:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)

        for candidate in response.candidates:
            messages.append(candidate.content)

        if not response.function_calls and response.text:
            return response.text

        function_responses = []
        for function_call_part in response.function_calls:
            function_call_result = call_function(function_call_part, verbose)
            if verbose and function_call_result.parts[0].function_response.response:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            function_responses.append(function_call_result.parts[0])

        if len(function_responses) > 0:
            messages.append(types.Content(role="user", parts=function_responses))

        return None

    except Exception as e:
        return f"Error: generating AI content: {e}"


if __name__ == "__main__":
    main()
