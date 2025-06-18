from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_chatbot_model(model_name="microsoft/DialoGPT-small"):
    
    print(f"Loading model: {model_name} ...")

    # Load tokenizer and model from Hugging Face
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Create a text-generation pipeline
    chatbot = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )

    print("Model loaded successfully.")
    return chatbot
