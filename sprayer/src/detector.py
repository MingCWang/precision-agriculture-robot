import base64
from openai import OpenAI



class Detector:
    def __init__(self):
        self.client = OpenAI(api_key = "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")
        self.MAX_RETRIES = 10
        self.plant_types = ['Cactus', 'Basil', 'Thyme', 'Parsley']


    def detect_plant(self, image):
        for i in range(self.MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Output the plant type and only the plant type in one word 'Cactus', 'Basil', 'Thyme', 'Parsley' if the image's object of interest contains the plant",
                        },
                        {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{image}"
                        },
                        },
                    ],
                    }
                ],
                )
                res = response.choices[0].message.content

                if res in self.plant_types:
                    return True, res
                else:
                    return False, None
                break
            except Exception as e:
                print('failed times: ', i, 'error: ', e)


    def is_plant(self, image): # expect base64 utf 8 string
        for i in range(self.MAX_RETRIES):
            try:
                response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "text",
                        "text": "Output in one word true or false if the image contains any plant",
                        },
                        {
                        "type": "image_url",
                        "image_url": {
                            "url":  f"data:image/jpeg;base64,{image}"
                        },
                        },
                    ],
                    }
                ],
                )
                res = response.choices[0].message.content

                if res in ["True", 'true']:
                    return True
                else:
                    return False
                break
            except Exception as e:
                print('failed times: ', i, 'error: ', e)



