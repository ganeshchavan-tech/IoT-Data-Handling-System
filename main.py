from handlers.message_handler import start_message_consumer

def main():
    print("Message consumption initiated...")
    start_message_consumer()
    print("Message consumption stopped.")

if __name__ == "__main__":
    main()