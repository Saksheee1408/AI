# Simple Electronics Store Keyword Chatbot
def electronics_chatbot():
    # Welcome message
    print("Welcome to Electronics Store Helper!")
    print("You can ask me about:")
    print("- Products (laptop, phone, headphones)")
    print("- Prices")
    print("- Warranty")
    print("- Delivery")
    print("- Contact")
    print("Type 'exit' to end the chat")
    
    # Main chat loop
    while True:
        # Get customer input
        user_message = input("\nCustomer: ").lower()
        
        # Exit condition
        if "exit" in user_message or "bye" in user_message:
            print("Bot: Thank you for chatting! Goodbye!")
            break
            
        # Product information
        elif "laptop" in user_message:
            print("Bot: Our laptops have:")
            print("- Intel i5 processor")
            print("- 8GB RAM")
            print("- 512GB SSD")
            print("Price: $800")
            
        elif "phone" in user_message:
            print("Bot: Our phones have:")
            print("- 6.5 inch screen")
            print("- 128GB storage")
            print("- 48MP camera")
            print("Price: $500")
            
        elif "headphones" in user_message:
            print("Bot: Our headphones are:")
            print("- Wireless")
            print("- 20-hour battery")
            print("- Noise cancelling")
            print("Price: $100")
            
        # Price related queries
        elif "price" in user_message or "cost" in user_message:
            print("Bot: Here are our prices:")
            print("- Laptop: $800")
            print("- Phone: $500")
            print("- Headphones: $100")
            
        # Warranty related queries
        elif "warranty" in user_message or "guarantee" in user_message:
            print("Bot: All our products have:")
            print("- 1 year warranty")
            print("- 30 days return policy")
            print("- Free repairs")
            
        # Delivery related queries
        elif "delivery" in user_message or "shipping" in user_message:
            print("Bot: Delivery information:")
            print("- Free delivery over $500")
            print("- 3-5 business days")
            print("- Tracking number provided")
            
        # Contact related queries
        elif "contact" in user_message or "help" in user_message:
            print("Bot: You can reach us at:")
            print("- Phone: 1-800-HELP")
            print("- Email: help@electronics.com")
            print("- Store: 123 Main Street")
            
        # Greetings
        elif "hello" in user_message or "hi" in user_message:
            print("Bot: Hello! How can I help you today?")
            
        # Thank you responses
        elif "thank" in user_message or "thanks" in user_message:
            print("Bot: You're welcome! Need anything else?")
            
        # Default response
        else:
            print("Bot: I'm not sure about that. You can ask about:")
            print("- Products (laptop, phone, headphones)")
            print("- Prices")
            print("- Warranty")
            print("- Delivery")
            print("- Contact")

# Run the chatbot
if __name__ == "__main__":
    electronics_chatbot()