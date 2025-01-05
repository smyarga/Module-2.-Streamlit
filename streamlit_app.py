# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st
# from datetime import time, datetime

# st.markdown("*Streamlit* is **really** ***cool***.")
# st.header('st.write')


# code = '''def hello():
#     print("Hello, Streamlit!")'''
# st.code(code, language="python")
# # Example 1

# st.write('Hello, *World!* :sunglasses:')

# # Example 2

# st.write(1234)

# # Example 3

# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df)

# # Example 4

# st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# # Example 5

# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# # Example 1

# st.subheader('Slider')

# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')

# # Example 2

# st.subheader('Range slider')

# values = st.slider(
#      'Select a range of values',
#      0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)

# # Example 3

# st.subheader('Range time slider')

# appointment = st.slider(
#      "Schedule your appointment:",
#      value=(time(11, 30), time(12, 45)))
# st.write("You're scheduled for:", appointment)

# # Example 4

# st.subheader('Datetime slider')

# start_time = st.slider(
#      "When do you start?",
#      value=datetime(2020, 1, 1, 9, 30),
#      format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)

# st.header('st.selectbox')

# option = st.selectbox(
#      'What is your favorite color?',
#      ('Blue', 'Red', 'Green'))

# st.write('Your favorite color is ', option)

# st.header('st.multiselect')

# options = st.multiselect(
#      'What are your favorite colors',
#      ['Green', 'Yellow', 'Red', 'Blue'],
#      ['Yellow', 'Red'])

# st.write('You selected:', options)

# st.header('st.checkbox')

# st.write ('What would you like to order?')

# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')

# if icecream:
#      st.write("Great! Here's some more 🍦")

# if coffee: 
#      st.write("Okay, here's some coffee ☕")

# if cola:
#      st.write("Here you go 🥤")

# st.header('st.latex')

# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')

# st.title('Customizing the theme of Streamlit apps')

# st.write('Contents of the `.streamlit/config.toml` file of this app')

# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """)

# number = st.sidebar.slider('Select a number:', 0, 10, 5)
# st.write('Selected number from slider widget is:', number)

# # st.set_page_config(layout="wide")

# st.title('How to layout your Streamlit app')

# with st.expander('About this app'):
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Input')
# user_name = st.sidebar.text_input('What is your name?')
# user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# st.header('Output')

# col1, col2, col3 = st.columns(3)

# with col1:
#   if user_name != '':
#     st.write(f'👋 Hello {user_name}!')
#   else:
#     st.write('👈  Please enter your **name**!')

# with col2:
#   if user_emoji != '':
#     st.write(f'{user_emoji} is your favorite **emoji**!')
#   else:
#     st.write('👈 Please choose an **emoji**!')

# with col3:
#   if user_food != '':
#     st.write(f'🍴 **{user_food}** is your favorite **food**!')
#   else:
#     st.write('👈 Please choose your favorite **food**!')


# st.title('st.form')

# # Full example of using the with notation
# st.header('1. Example of using `with` notation')
# st.subheader('Coffee machine')

# with st.form('my_form'):
#     st.subheader('**Order your coffee**')

#     # Input widgets
#     coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
#     coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
#     brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
#     serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
#     milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
#     owncup_val = st.checkbox('Bring own cup')

#     # Every form must have a submit button
#     submitted = st.form_submit_button('Submit')

# if submitted:
#     st.markdown(f'''
#         ☕ You have ordered:
#         - Coffee bean: `{coffee_bean_val}`
#         - Coffee roast: `{coffee_roast_val}`
#         - Brewing: `{brewing_val}`
#         - Serving type: `{serving_type_val}`
#         - Milk: `{milk_val}`
#         - Bring own cup: `{owncup_val}`
#         ''')
# else:
#     st.write('☝️ Place your order!')


# # Short example of using an object notation
# st.header('2. Example of object notation')

# form = st.form('my_form_2')
# selected_val = form.slider('Select a value')
# form.form_submit_button('Submit')

# st.write('Selected value: ', selected_val)
import streamlit as st
import random

# ---------------- ASCII ART for each hangman stage ----------------
# Index == attempts_left
hangman_stages = [
    """
      _______
     |/      |
     |      ( )
     |      /|\\
     |       |
     |      / \\
     |
    _|___
    """,
    """
      _______
     |/      |
     |      ( )
     |      /|\\
     |       |
     |      /
     |
    _|___
    """,
    """
      _______
     |/      |
     |      ( )
     |      /|\\
     |       |
     |
     |
    _|___
    """,
    """
      _______
     |/      |
     |      ( )
     |      /|
     |       |
     |
     |
    _|___
    """,
    """
      _______
     |/      |
     |      ( )
     |       |
     |       |
     |
     |
    _|___
    """,
    """
      _______
     |/      |
     |      ( )
     |
     |
     |
     |
    _|___
    """,
    """
      _______
     |/      |
     |
     |
     |
     |
     |
    _|___
    """
]

# ---------------- WORD LIST ----------------
WORDS = [
    "streamlit", "python", "hangman", "visualize", "session", 
    "development", "code", "function", "virtual", "environment"
]

# ---------------- INITIALIZE / RESET GAME ----------------
def initialize_game_state():
    """
    Initializes (or resets) the game state in session_state.
    """
    st.session_state.secret_word = random.choice(WORDS).upper()
    st.session_state.guessed_letters = set()
    st.session_state.attempts_left = 6
    st.session_state.game_over = False

# ---------------- DISPLAY HANGMAN ----------------
def display_hangman():
    """
    Displays the ASCII art for the current number of attempts left.
    """
    index = st.session_state.attempts_left
    # Show as a code block for clearer formatting
    st.markdown(f"```{hangman_stages[index]}```")

# ---------------- DISPLAY CURRENT PROGRESS ----------------
def display_current_progress():
    """
    Displays the current progress of the guessed word (underscores for unguessed letters).
    """
    display_word = ""
    for char in st.session_state.secret_word:
        if char in st.session_state.guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    st.write("**Word:**", display_word.strip())

# ---------------- CHECK GAME STATUS ----------------
def check_game_status():
    """
    Checks if the user has guessed the word or if attempts have run out.
    """
    # If user guessed all letters
    if all(letter in st.session_state.guessed_letters for letter in st.session_state.secret_word):
        st.session_state.game_over = True
        st.success("Congratulations! You guessed the word!")
    
    # If no attempts left
    if st.session_state.attempts_left <= 0:
        st.session_state.game_over = True
        st.error(f"Game Over! The word was: {st.session_state.secret_word}")

# ---------------- PROCESS A SINGLE GUESS ----------------
def guess_letter(letter):
    """
    Processes a single letter guess:
    - Deducts an attempt if the guess is wrong.
    - Adds the guessed letter to the guessed_letters set.
    - Checks the game status afterward.
    """
    letter = letter.upper()

    if letter in st.session_state.guessed_letters:
        st.warning(f"You already guessed '{letter}'. Try a different letter.")
        return

    st.session_state.guessed_letters.add(letter)
    if letter not in st.session_state.secret_word:
        st.session_state.attempts_left -= 1
        st.warning(f"'{letter}' is NOT in the word. Attempts left: {st.session_state.attempts_left}")
    else:
        st.success(f"Good guess! '{letter}' is in the word. You will see it with the next guess")

    check_game_status()

# ---------------- STREAMLIT MAIN APP ----------------
def main():
    st.title("Hangman in Streamlit")

    # If game not started, or the user clicks 'Reset Game', initialize
    if "secret_word" not in st.session_state or st.button("Reset Game"):
        initialize_game_state()

    # Show hangman ASCII and current word state
    display_hangman()
    display_current_progress()

    # If the game is not yet over, show a form to guess a letter
    if not st.session_state.game_over:
        # Use a form so we don't manually overwrite session_state
        with st.form("guess_form"):
            letter_input = st.text_input("Guess a letter", max_chars=1)
            guess_button = st.form_submit_button("Guess")

            # When the user submits the form
            if guess_button and letter_input:
                guess_letter(letter_input)
    else:
        st.info("Click 'Reset Game' to start a new game.")

if __name__ == "__main__":
    main()