# Flashy - English Learning Flashcard
Flashy is a simple and interactive flashcard app designed to help users learn English vocabulary. The app utilizes a spaced repetition technique to reinforce memory by presenting words that need more practice more often.
# Features
Flashcards: The app displays flashcards with French words on the front and English translations on the back.
Flip Card: Users can click on the flashcard to flip and reveal the English translation.
Knowledge Assessment: Users can indicate if they know a word or not by clicking on corresponding buttons.
Data Persistence: The app saves progress by maintaining a CSV file (words_to_learn.csv) with words that need more practice.
# Usage
Launch the App:

Run the Python script to launch the Flashy app.
The flashcard will display a French word initially.
Flip the Flashcard:

Click on the flashcard to flip and reveal the English translation.
Assess Knowledge:

Click the "✔️" button if you know the word.
Click the "❌" button if you don't know the word.
Progress and Learning:

The app keeps track of your progress and focuses on words that need more practice.
Words that are known are removed from the flashcard list.
Exit the App:

Close the app window to exit.
# Data Files
The app uses CSV files (french_words.csv and words_to_learn.csv) to store French and English word pairs.
If words_to_learn.csv exists, the app will prioritize those words for practice.
# Requirements
Python 3.x
pandas library
tkinter library
