import streamlit as st
from streamlit import session_state
import functions

# Read existing todos
todos = functions.read_files()

# Function to add a new
def add_todo():
    new_todo = st.session_state["todoIn"].strip() + "\n"  # Keep newline for correct formatting
    if new_todo.strip():  # Avoid adding empty todos
        todos.append(new_todo)
        functions.add_todos(new_todo)
        functions.write_files(todos)
        st.session_state["todoIn"] = ""  # Clear input field

# Page configuration & title
st.set_page_config(page_title="My Todo App", page_icon="📝", layout="centered")
st.title("📝 My Todo App")
st.markdown("<h5 style='color:gray;'>Stay organized and boost productivity! 🚀</h5>", unsafe_allow_html=True)

# Horizontal separator
st.markdown("---")

# Display existing todos
for index, todo in enumerate(todos):
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.markdown(f"<p style='font-size:18px; color:#FFFFFF; font-weight:bold;'>• {todo.strip()}</p>", unsafe_allow_html=True)
    with col2:
        # Green checkmark button (✔)
        if st.button("✅", key=f"check_{index}", help="Mark as done"):
            todos.pop(index)
            functions.write_files(todos)
            session_state.pop(todo, None)  # Prevent KeyError
            st.rerun()

# Horizontal separator
st.markdown("---")

# Input field for new todos
st.text_input(label="", placeholder="✍️ Add a new task...", on_change=add_todo, key="todoIn")

# Footer with development credit
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit.</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:gray;'>Development Credit: Nafis Kamal</p>", unsafe_allow_html=True)

