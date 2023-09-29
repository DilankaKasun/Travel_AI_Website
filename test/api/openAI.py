import os
import openai
import config
import jsonHandle


class AI_Handle():
    def required(self):
      storege_data= jsonHandle.Handle()
      x=storege_data.read()

      pass


openai.api_key = config.OpenAi.OPENAI_API_KEY
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "I want to see beautiful places in Sri Lanka. I like to go by train. I like walking in the mountains. I am staying in Sri Lanka for about 20 days. I want to visit Sri Lanka with very little time"
    },
    {
      "role": "user",
      "content": "I want to see beautiful places in Sri Lanka. I like to go by train. I like walking in the mountains. I am staying in Sri Lanka for about 20 days. I want to visit Sri Lanka with very little time"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "assistant",
      "content": "I apologize, but I am an AI language model and do not have a specific name. You can just refer to me as ChatGPT. How can I help you today?"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "assistant",
      "content": "Great! Sri Lanka has a lot to offer in terms of beautiful places and scenic train rides. Given your preferences and limited time, here is a suggested itinerary for your 20-day trip:\n\nDay 1-3: Colombo\n- Start your trip in the capital city of Colombo, explore its vibrant markets, colonial architecture, and enjoy the local cuisine.\n\nDay 4-7: Kandy\n- Take a train ride from Colombo to Kandy, which offers stunning views of lush green landscapes. \n- In Kandy, visit the Temple of the Tooth, explore the Royal Botanical Gardens, and take a leisurely walk around the Kandy Lake.\n\nDay 8-11: Ella\n- Take a picturesque train journey from Kandy to Ella, known for its breathtaking mountain views and tea plantations.\n- Once in Ella, enjoy hiking to popular spots like Ella Rock and Little Adam's Peak. Don't miss the iconic Nine Arches Bridge.\n\nDay 12-14: Nuwara Eliya\n- Proceed to Nuwara Eliya, often called the \"Little England\" of Sri Lanka. \n- Visit the tea estates, take a boat ride on Lake Gregory, and enjoy the cool climate.\n\nDay 15-16: Horton Plains"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response['choices'][0])