import os
from dotenv import load_dotenv
import openai
import config as conf


def get_open_ai_client():
    load_dotenv()  # load existing .env variables
    if not os.getenv('OPENAI_API_KEY'):
        api_key = input("Enter your OPENAI_API_KEY: ").strip()
        print('storing api key in .env file at root of this project...')
        with open('.env', 'a') as env_file:
            env_file.write(f'OPENAI_API_KEY={api_key}\n')
        load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    client = openai.OpenAI(api_key=api_key)
    return client


def get_chatgpt_response(client, model, query):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": query}],
        max_tokens=conf.max_tokens,
        n=conf.outputs
    )
    outputs = [choice.message.content.strip() for choice in response.choices]
    return outputs


def main():
    client = get_open_ai_client()
    correct, incorrect = 0, 0
    for question, answer in conf.questions_answers:
        query = f'{conf.prompt}{question}'
        print(f'QUESTION: "{question}"')
        outputs = get_chatgpt_response(client, conf.model, query)
        for i, output in enumerate(outputs):
            print(f'ANSWER[{i}]: {output}')
            print(f'Expected answer: {answer}')
            if output.lower() == answer:
                print('Correct!')
                correct += 1
            else:
                print('Incorrect!')
                incorrect += 1
            print('-------------------')
    print('')
    print(f'Correct answers: {correct}')
    print(f'Incorrect answers: {incorrect}')
    print(f'Accuracy: {correct / (correct + incorrect) * 100:.2f}%')


if __name__ == "__main__":
    main()
