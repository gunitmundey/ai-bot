from tkinter import Tk, Label, Entry, Button, StringVar, messagebox
import logging

class TradingBotUI:
    def __init__(self, master):
        self.master = master
        master.title("Trading Bot Configuration")

        self.api_key_var = StringVar()
        self.api_secret_var = StringVar()

        self.label_api_key = Label(master, text="API Key:")
        self.label_api_key.pack()

        self.entry_api_key = Entry(master, textvariable=self.api_key_var)
        self.entry_api_key.pack()

        self.label_api_secret = Label(master, text="API Secret:")
        self.label_api_secret.pack()

        self.entry_api_secret = Entry(master, textvariable=self.api_secret_var, show='*')
        self.entry_api_secret.pack()

        self.start_button = Button(master, text="Start Trading", command=self.start_trading)
        self.start_button.pack()

        logging.basicConfig(filename='trading_bot.log', level=logging.INFO)

    def start_trading(self):
        api_key = self.api_key_var.get()
        api_secret = self.api_secret_var.get()

        if not api_key or not api_secret:
            messagebox.showerror("Input Error", "Please enter both API Key and API Secret.")
            return

        try:
            # Here you would typically call the bot's trading logic with the provided keys
            messagebox.showinfo("Success", "Trading bot started with provided API keys.")
            logging.info("Trading bot started with provided API keys.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    trading_bot_ui = TradingBotUI(root)
    root.mainloop()