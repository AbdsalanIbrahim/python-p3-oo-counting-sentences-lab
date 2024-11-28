import re
import sys
import io

class MyString:
    def __init__(self, value=''):
        # Initialize with the value, but validate the type when it's set
        self._value = ''
        self.value = value  # Use the setter to initialize the value

    @property
    def value(self):
        """Getter for the value."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Setter for the value that checks if it's a string."""
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        """Returns True if the value ends with a period, False otherwise."""
        return self.value.endswith('.')
    
    def is_question(self):
        """Returns True if the value ends with a question mark, False otherwise."""
        return self.value.endswith('?')
    
    def is_exclamation(self):
        """Returns True if the value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')
    
    def count_sentences(self):
        """Returns the number of sentences in the value."""
        # Split the value into a list of sentences based on sentence-ending punctuation
        sentences = re.split(r'[.!?]', self.value)
        
        # Remove empty strings caused by trailing punctuation or multiple punctuation marks
        sentences = [s.strip() for s in sentences if s.strip()]
        
        # Return the number of non-empty sentences
        return len(sentences)

# Testing the output with redirected stdout
if __name__ == "__main__":
    captured_out = io.StringIO()
    sys.stdout = captured_out

    # Example of testing the error handling
    string = MyString()
    string.value = 123  # Setting a non-string value

    sys.stdout = sys.__stdout__
    print(captured_out.getvalue())  # This should print the error message if it's working correctly
