import unittest
from unittest.mock import patch
# from pynput import keyboard
from text.text_capture import TextCapture

class TestTextCapture(unittest.TestCase):
    def setUp(self):
        self.output_dir = "/path/to/test/output"
        self.text_capture = TextCapture(output_dir=self.output_dir)

    def tearDown(self):
        self.text_capture.stop_capture()

    @patch('text.text_capture.TextCapture.append_to_file')
    def test_on_key_press(self, mock_append_to_file):
        self.text_capture.on_key_press(keyboard.KeyCode.from_char('a'))
        mock_append_to_file.assert_called_with('a')

    @patch('text.text_capture.TextCapture.append_to_file')
    def test_on_key_press_special_keys(self, mock_append_to_file):
        self.text_capture.on_key_press(keyboard.Key.enter)
        mock_append_to_file.assert_called_with('\n')

        self.text_capture.on_key_press(keyboard.Key.space)
        mock_append_to_file.assert_called_with(' ')

        self.text_capture.on_key_press(keyboard.Key.ctrl_l)
        mock_append_to_file.assert_called_with('<CTRL>')

        def test_word_completion(self):
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('H'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('e'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('l'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('l'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('o'))
            self.text_capture.on_key_press(keyboard.Key.space)

            # Assert that the word "Hello" is captured and saved to the file

        def test_continuous_typing(self):
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('T'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('h'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('i'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('s'))
            self.text_capture.on_key_press(keyboard.Key.space)
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('i'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('s'))
            self.text_capture.on_key_press(keyboard.Key.space)
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('a'))
            self.text_capture.on_key_press(keyboard.Key.space)
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('t'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('e'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('s'))
            self.text_capture.on_key_press(keyboard.KeyCode.from_char('t'))
            self.text_capture.on_key_press(keyboard.Key.enter)

    # Assert that the text "This is a test" is captured and saved to the file

# Add more test cases for different scenarios, such as special characters, punctuation, etc.

    # Add more test cases for different scenarios and edge cases

if __name__ == "__main__":
    unittest.main()