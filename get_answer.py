import requests

def get_token():
    with open('key.txt','r') as f:
        tmpk = f.read()
    f.close()
    return tmpk

token = get_token()

print(token)

headers = {"Authorization": "Bearer {}".format(token)}

body = {
    "text": "123 Easy Street:Service Address \
             872 Gentry Street:",
    "top_p": 1,
    "top_k": 40,
    "temperature": 0.24,
    "repetition_penalty": 1,
    "length": 65,
    "stop_sequences": [""]
}

res = requests.post(
        "https://9a70e249-nertest-en-pro.forefront.link/answer",
        json=body,
        headers=headers
    )

print(res)

print(res.text)