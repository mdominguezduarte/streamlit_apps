# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:40:25 2022

@author: DKu_7
"""

# Math Flashcards App
# Choices: Add, Subtract, Multiply, Divide
# Choices 2: Add/Subt Integers, Mult/Div Integers, Basic Exponents, Quad Factors

import streamlit as st
from streamlit_option_menu import option_menu
import random

st.write("""
# Math Flashcards App
""")

with st.expander("About The Flashcards Application"):
     st.write("""
         A simple flashcards application for learning purposes. Click on New Question to obtain a new question.
         Click on the expand box to see the answer.
         
         I tried to implement a number input or multiple choice answers but it didn't work out. Instead I am doing a flashcards style format.
     """)

## Sidebar Choices
# Navigation Bars:
# Reference: https://www.youtube.com/watch?v=hEPoto5xp3k
# Guide: https://discuss.streamlit.io/t/streamlit-option-menu-is-a-simple-streamlit-component-that-allows-users-to-select-a-single-item-from-a-list-of-options-in-a-menu/20514


with st.sidebar:
    selected = option_menu("Select Flashcard", 
                           ["Addition", 'Subtraction', "Multiplication", 'Division',
                            'Add & Subtract Integers', 'Multiply & Divide Integers',
                            'Evaluating Exponents', 'Quadratic Factors' ], 
                            icons=['bi bi-plus', 'bi bi-dash', 'bi bi-arrow-right-circle',
                                   'bi bi-arrow-right-circle', 'bi bi-123', 'bi bi-123',
                                   'bi bi-arrow-right-square', 'bi bi-arrow-right-square'], 
                            menu_icon="cast", default_index=0)


# Random Numbers

def rand_pack_one():
    rand1 = random.randint(0, 10)
    rand2 = random.randint(1, 10)
    return(rand1, rand2)

# Negative Numbers random numbers:
def rand_pack_two():
    rand_neg1 = random.randint(-10, 10)
    rand_neg2 = random.randint(-10, 10)
    return(rand_neg1, rand_neg2)

    
# Random Numbers

### Function dependent on option menu:
    
def get_addition(num1, num2):
    st.write(f"""### What is {num1} + {num2} ?""")
    
    with st.expander("Click To See Answer"):
        st.write(f"""{num1 + num2}""")
     
def get_subtraction(num1, num2):
    
    higher = max(num1, num2)
    lower = min(num1, num2)
    
    st.write(f"""### What is {higher} - {lower} ?""")
    
    with st.expander("Click To See Answer"):
        st.write(f"""{higher -lower}""")

def get_multiplication(num1, num2):
    st.write(f"""### How much is {num1} x {num2} ?""")
    with st.expander("Click To See Answer"):
        st.write(f"""{num1 * num2}""")
        
def get_division(num1, num2):
    product = num1 * num2
    st.write(f"""### How much is {product} ÷ {num2} ?""")
    with st.expander("Click To See Answer"):
        st.write(f"""{int(product / num2)}""")

def get_integers(num1, num2):
    is_addition = random.randint(0, 1)
    if is_addition == 1:
        st.write(f"""### How much is {num1} + {num2} ?""")
        with st.expander("Click To See Answer"):
            st.write(f"""{num1 + num2}""")
    else:
        st.write(f"""### How much is {num1} - {num2} ?""")
        with st.expander("Click To See Answer"):
            st.write(f"""{num1 - num2}""")
            
def get_integers2(num1, num2):
    is_multiply = random.randint(0, 1)
    if is_multiply == 1:
        st.write(f"""### How much is {num1} x {num2} ?""")
        with st.expander("Click To See Answer"):
            st.write(f"""{num1 * num2}""")
    else:
        product = num1 * num2
        st.write(f"""### How much is {product} ÷ {num2} ?""")
        with st.expander("Click To See Answer"):
            st.write(f"""{int(product / num2)}""")

        
# Exponents Flashcards Cade:
    
def exponents_fc(num1, num2):
    st.latex(r'''\text{What is } x^y''')
    st.write(f"""#### where x = {(num1)} and y = {num2} ?""")
    with st.expander("Click To See Answer"):
        st.write(f"""{num1 ** num2}""")
        
def quadratic_factors(num1, num2):
    intercept = num1 * num2
    bx = num1 + num2
    st.latex(r'''\text{Factor } x^2 + bx + c''')
    st.write(f"""#### where b = {bx} and c = {intercept} ?""")
    st.write(f"""Alternatively what are two numbers that add up to {bx} and multiply to {intercept}.""")
    with st.expander("Click To See Answer"):
        st.write(f"""(x + {(num1)})(x + {(num2)}) or {num1} and {num2}""")
# Quadratics Factoring


### Front Page:
    
## Flashcards Type depends on choice from left sidebar:

    
if selected == "Addition":
    st.write("## Addition Flashcards")
    num1, num2 = rand_pack_one()
    # Function Call
    get_addition(num1, num2)
elif selected == "Subtraction":
    st.write("## Subtraction Flashcards")
    num1, num2 = rand_pack_one()
    # Function Call
    get_subtraction(num1, num2)
elif selected == "Multiplication":
    st.write("## Multiplication Flashcards")
    num1, num2 = rand_pack_one()
    # Function Call
    get_multiplication(num1, num2)
elif selected == "Division":
    st.write("## Division Flashcards")
    num1, num2 = rand_pack_one()
    # Function Call
    get_division(num1, num2)
elif selected == "Add & Subtract Integers":
    st.write("## Add & Subtract Negative Numbers Flashcards")
    num1, num2 = rand_pack_two()
    # Function Call
    get_integers(num1, num2)
elif selected == "Multiply & Divide Integers":
    st.write("## Multiply & Divide Negative Numbers Flashcards")
    num1 = random.randint(-10, 10)
    # Num 2 is a non-zero number to avoid division by 0
    list2 = list(range(-10, 0)) + list(range(1, 11))
    num2 = random.choice(list2)
    # Function Call
    get_integers2(num1, num2)
elif selected == "Evaluating Exponents":
    st.write("## Simple Exponents Flashcards")
    num1 = random.randint(-5, 5)
    # Num 2 is a non-zero number to avoid division by 0
    list2 = list(range(-5, 0)) + list(range(1, 5))
    num2 = random.choice(list2)
    # Function Call
    exponents_fc(num1, num2)
elif selected == "Quadratic Factors":
    st.write("## Quadratic Factoring Flashcards")
    num1 = random.randint(-5, 5)
    # Num 2 is a non-zero number to avoid division by 0
    list2 = list(range(-5, 0)) + list(range(1, 5))
    num2 = random.choice(list2)
    # Function Call
    quadratic_factors(num1, num2)    
    
# Button to obtain new question by refreshing:
if st.button('New Question'):
   print("") #Auto refresh page

