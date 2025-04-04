from js import document
import random

greetings = [
    "Welcome, hidden one.",
    "The stars have whispered of your return.",
    "Another seeker awakens...",
    "A wizard walks among mortals once more.",
]

intro_text = """
You have entered the Hall of Doors — a place between worlds.
Each door leads to a spell that sharpens your powers in both the magical and mortal realm.
Choose wisely. Return often.
"""

# Inject text into the page
document.body.innerHTML += f"""
<div class='wizard-intro'>
    <p class='greeting'>{random.choice(greetings)}</p>
    <p>{intro_text}</p>
    <button onclick="alert('The first door opens soon...')">Enter the First Door</button>
</div>
"""
