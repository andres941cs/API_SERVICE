# from openai import OpenAI
# client = OpenAI()


# response = client.chat.completions.create(
#   model="gpt-4",
#   messages=[
#     {
#       "role": "system",
#       "content": "You will be provided with a sentence in English, and your task is to translate it into French."
#     },
#     {
#       "role": "user",
#       "content": "My name is Jane. What is yours?"
#     }
#   ],
#   temperature=0.7,
#   max_tokens=64,
#   top_p=1
# )
# import os
# import openai

# class TraductorOpenAI:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         openai.api_key = api_key

#     def romanization(self, lyric):
#         instruccion = f"Con este único prompt, puedes ingresar el texto en el idioma deseado y recibir la romanización correspondiente: {lyric}"
#         solicitud = openai.CompletionRequest(prompt=instruccion)
#         respuesta = openai.Completion.create(model="chatgpt", requests=[solicitud])
#         traduccion = respuesta["choices"][0]["text"]
#         return traduccion

# # Ejemplo de uso
# traductor = TraductorOpenAI(YOUR_API_KEY)

# lyricRomanized = traductor.romanization(lyric)

# print(f"ROMANIZED: {lyricRomanized}")

from openai import OpenAI
client = OpenAI()
client.api_key = "OPENAI_API_KEY" # [VARIABLE DE ENTORNO]
song = "cancion" # [PARAMETRO DE ENTRADA]
response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" },
  messages=[
    # {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "user", "content": "Romanize the following song: " + song}
  ]
)
print(response.choices[0].message.content)