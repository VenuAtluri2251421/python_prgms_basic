from pyo import *

# Initialize the Pyo server
s = Server().boot()

# Create an input sound source
input_sound = Input()

# Apply some audio processing
processed_sound = input_sound * 0.5  # Example: Reducing the volume by half

# Create an output sound object
output_sound = Dac().out()

# Connect the processed sound to the output
output_sound.setInput(processed_sound)

# Start the Pyo server
s.start()
