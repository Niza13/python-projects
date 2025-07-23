import os
import json
import random
import pyttsx3
from PyPDF2 import PdfReader
import threading
import keyboard

# File paths
STATE_FILE = "state.json"

# Load or initialize state
def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_state(state):
    with open(STATE_FILE, "w") as file:
        json.dump(state, file)

# Read a page from the PDF
def read_pdf_page(pdf_reader, page_number):
    try:
        page = pdf_reader.pages[page_number]
        return page.extract_text()
    except IndexError:
        print("Reached the end of the PDF.")
        return None

# Text-to-Speech
def read_aloud(text, speed):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()

# Get PDF file list
def get_pdf_files(directory="."):
    return [file for file in os.listdir(directory) if file.endswith(".pdf")]

# Main function
def main():
    # Load state
    state = load_state()

    # Get list of PDFs
    pdf_files = get_pdf_files()
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return

    # Display available PDFs
    print("Available PDFs:")
    for idx, pdf in enumerate(pdf_files, start=1):
        print(f"{idx}. {pdf}")

    # Ask user to choose a PDF
    choice = input("Enter the number of the PDF to read: ")
    try:
        pdf_index = int(choice) - 1
        if pdf_index < 0 or pdf_index >= len(pdf_files):
            print("Invalid choice. Exiting.")
            return
    except ValueError:
        print("Invalid input. Exiting.")
        return

    # Selected PDF
    pdf_file = pdf_files[pdf_index]
    pdf_state = state.get(pdf_file, {"last_page": 0})

    # Open the PDF
    try:
        pdf_reader = PdfReader(pdf_file)
        total_pages = len(pdf_reader.pages)
    except FileNotFoundError:
        print(f"Error: {pdf_file} not found.")
        return

    # User choice for sequential or random
    print(f"PDF '{pdf_file}' loaded. Total pages: {total_pages}. Last read page: {pdf_state['last_page']}")
    mode = input("Enter 's' for sequential reading, 'r' for random reading: ").lower()

    if mode == 's':
        current_page = pdf_state["last_page"]
    elif mode == 'r':
        current_page = random.randint(0, total_pages - 1)
    else:
        print("Invalid choice. Exiting.")
        return

    # Ask for reading speed
    try:
        speed = int(input("Enter reading speed (default is 130, higher is faster): ").strip() or 130)
    except ValueError:
        print("Invalid input. Using default speed 130.")
        speed = 2130

    stop_reading = False

    def listen_for_keys():
        nonlocal stop_reading, current_page
        while not stop_reading:
            if keyboard.is_pressed('q'):
                print("Stopping...")
                stop_reading = True
                exit() # break
            if keyboard.is_pressed('enter'):
                print("Skipping to the next page...")
                current_page += 1
                if current_page >= total_pages:
                    current_page = 0  # Restart from the beginning

    # Start the key listener in a separate thread
    listener_thread = threading.Thread(target=listen_for_keys, daemon=True)
    listener_thread.start()

    # Continuous reading
    while not stop_reading:
        text = read_pdf_page(pdf_reader, current_page)
        if text:
            print(f"Reading page {current_page + 1}/{total_pages}:\n{text}")
            read_aloud("next page", speed)
            read_aloud(text, speed)
        else:
            # print("No more pages to read.")
            # break
            pass

        # Update state
        pdf_state["last_page"] = current_page
        state[pdf_file] = pdf_state
        save_state(state)

        # Wait a moment to prevent rapid skipping
        if not stop_reading:
            current_page += 1
            if current_page >= total_pages:
                current_page = 0  # Restart from the beginning

if __name__ == "__main__":
    main()
