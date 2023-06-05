import requests
import streamlit as st
from streamlit_lottie import st_lottie
from app3 import process
st.set_page_config(page_title="Shortest Path",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

# lottie file
lottie_code=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_0lvdwxbc.json")

#--header
st.title("Shortest Path")
st.write("The algorithm uses advance image recognisition system to identify the note and the path between them and uses it to calculate and identify the shortest path")
# st.write("[click to learn more](https://youtu.be/BBJa32lCaaY)")
# st_lottie(lottjeie_code,height=300, key="coding")


# Create a centered button to accept images
st.markdown(
    """
    <div style='display: flex; justify-content: center;'>
        <label for="file-upload" class="btn btn-primary">
          **UPLOAD IMAGE**
        </label>
    </div>
    """,
    unsafe_allow_html=True
)
i=0
j=0
def Reload():
    global i
    i+=1
# Process the uploaded image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
vertexIndex=st.number_input("StartVertex",min_value=0,step=1,on_change=Reload())
inputImage,outputImage=st.columns(2)

if uploaded_file is not None :
    inputImage.image(uploaded_file, caption=uploaded_file.name,use_column_width='always')
    image,res=process(uploaded_file,vertexIndex)
    outputImage.image(image, caption=uploaded_file.name,use_column_width='always')
    # images.image(uploaded_file,image)
    # res.sort()
    # for i in res:
    #     st.markdown("- " + str(i))
    st.text(f"Shortest path distances from vertex {vertexIndex} to all other vertices:")
    for i, distance in enumerate(res):
        st.text(f"Vertex {i}: {distance}")
    
# if j is not i:
#     st.image(uploaded_file, caption=uploaded_file.name)
#     image,res=process(uploaded_file)
#     st.image(image, caption=uploaded_file.name)
#     st.text(res)
#     i=j