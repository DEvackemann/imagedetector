# Q&A Chatbot with Background GUI Image

# Import necessary libraries
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

# Load environment variables
load_dotenv()

# Import generative AI module
import google.generativeai as genai

# Configure API key for generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load OpenAI model and generate responses
def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

# Function to setup uploaded image
def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Invoice Detection")

# CSS for background image
background_image_style = """
    <style>
    body {
        background-image: url('https://cdn.dribbble.com/userupload/6786847/file/original-8b3aaa9f4dfac8e78ebbba1f25569466.jpg?crop=0x153-1080x963&resize=400x300&vertical=center'); /* Replace with your background image URL */
        background-size: cover;
        }
    </style>
    """

# Display background image using st.markdown
st.markdown(background_image_style, unsafe_allow_html=True)

# Header and user input for prompt
st.header("Gemini🫧 Invoice Detection 📑")
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """
input = st.text_input("Enter Prompt: ⤵ ", key="input")
uploaded_file = st.file_uploader("Choose an image📄...", type=["jpg", "jpeg", "png"])

# Display uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to generate responses
submit = st.button("Generate Responses to Enter Prompt⏳")

# Handle submission of prompt and image
if submit:
    try:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.subheader("The response to your prompt is...■■■■■100% ⌛🤖📢🛠️✔️")
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")

# Add additional GUI elements or functionality as needed
