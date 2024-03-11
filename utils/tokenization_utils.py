import os
import json
import uuid
import nltk

class TokenizationUtils:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        self.current_entry = None
        self.token_limit = 2000  # Adjust the token limit based on your model's context window
        nltk.download('punkt')  # Download the required NLTK data

    def is_token_limit_reached(self, text):
        tokens = nltk.word_tokenize(text)
        return len(tokens) >= self.token_limit

    def preprocess_text(self, text):
        # Strip unnecessary whitespace and non-text characters
        clean_text = " ".join(text.split())
        return clean_text

    def tokenize_and_store_text(self, text, timestamp, source, metadata=None, context_switch=False):
        clean_text = self.preprocess_text(text)

        if self.current_entry is None or context_switch:
            if self.current_entry is not None:
                self.store_entry(self.current_entry)
            self.current_entry = {
                "id": str(uuid.uuid4()),
                "timestamp": timestamp,
                "source": source,
                "text": clean_text,
                "metadata": metadata
            }
        else:
            self.current_entry["text"] += " " + clean_text

        # Print the current entry to the console
        print(json.dumps(self.current_entry, indent=2))

        # Check if the current entry reaches the token limit
        if self.is_token_limit_reached(self.current_entry["text"]):
            self.store_entry(self.current_entry)
            self.current_entry = None

    def store_entry(self, entry):
        # Generate a unique filename based on the entry's timestamp
        filename = f"entry_{entry['timestamp']}.json"
        filepath = os.path.join(self.output_dir, filename)

        # Tokenize the text and add the tokens to the entry
        entry["tokens"] = nltk.word_tokenize(entry["text"])

        # Write the entry to a JSON file
        with open(filepath, 'w') as file:
            json.dump(entry, file, indent=2)

    def process_text_capture(self, text, timestamp, metadata=None, context_switch=False):
        self.tokenize_and_store_text(text, timestamp, "Text Capture", metadata, context_switch)


    def process_ocr_text(self, text, timestamp, metadata=None):
        self.tokenize_and_store_text(text, timestamp, "OCR", metadata)

    def process_whisper_transcript(self, text, timestamp, metadata=None):
        self.tokenize_and_store_text(text, timestamp, "Whisper Transcript", metadata)