import openai
import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading

veri_listesi = []

# OpenAI API anahtarını ayarlayın
openai.api_key = "my api key. Since it is a paid content, you can contact us if needed."

# Chatbot işlevini tanımlayın
def chatbot(user_input):
    # OpenAI API'sine istek gönderin
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{user_input}"},
        ]
    )

    # Yanıtı döndürün
    return response['choices'][0]['message']['content']

# Masaüstü uygulamasını başlatın
root = tk.Tk()
root.configure(bg='black')
root.title("AI GÖKTÜRK")
root.iconbitmap('ai-gokturk.ico')

# Marka adını ekleyin
brand_label = tk.Label(root, text="AI GÖKTÜRK", bg="black", fg="white", font=("Helvetica", 16))
brand_label.pack(pady=10)

# Chatbot yanıtını görüntülemek için bir metin kutusu oluşturun
chatbot_response = scrolledtext.ScrolledText(root, height=20, bg="black", fg="white")
chatbot_response.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Kullanıcı girişi için bir metin kutusu oluşturun
user_input = tk.Entry(root, font=("Helvetica", 14))
user_input.pack(side=tk.LEFT, fill=tk.X, padx=10, expand=True)

# Kullanıcı girişini alın ve chatbot'tan yanıt alın
def get_response(event=None):
    user_text = user_input.get()
    if user_text.strip() != "":
        chatbot_response.insert(tk.INSERT, "\nYou: " + user_text)
        chatbot_response.insert(tk.INSERT, "\nChatbot: Yükleniyor...")
        root.update()
        response = chatbot(user_text)
        chatbot_response.delete('end-1l', 'end')
        chatbot_response.insert(tk.INSERT, "\nChatbot: " + response)
        user_input.delete(0, tk.END)

        file = open("GPT-3.5-Turbo.txt", "a") #istenirse dosya yolu eklenebilir
        file.write("\nYou: " + user_text + "\n")
        file.write("Chatbot: " + response + "\n")
        file.close()

root.bind('<Return>', get_response)

# Yanıt almak için bir düğme oluşturun
get_response_button = tk.Button(root, text="Gönder", command=get_response)
get_response_button.pack(side=tk.RIGHT)

root.mainloop()
