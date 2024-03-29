from cgi import test
import os

import streamlit as st

from html_mardown import app_off,app_off2, model_predicting, loading_bar, result_pred, image_uploaded_success, more_options, class0, class1, class2, class3, class4, s_load_bar, class0_side, class1_side, class2_side, class3_side, class4_side, unknown, unknown_side, unknown_w, unknown_msg
from pagination import paginator
from score_translation import score_translation
from streamlit_pin2ctr import st_gauge_chart


def do_stuff_on_page_load():
    st.set_page_config(layout="wide")

do_stuff_on_page_load()

my_path = 'images/'
logo_path =  my_path + '1b7601e035a83c13c208b4ec905ee6d9.png'
image_1 = my_path + 'Dog/'
image_2 = my_path + 'Coffee/'
image_3 = my_path + "Women's Fashion/"

with st.sidebar:
        st.sidebar.image(logo_path, use_column_width=True)
        st.markdown("""
        <style>
        .big-font {
            font-size:40px !important;
            text-align: center;
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
                <style>
                .big-font2 {
                    font-size:15px !important;
                    text-align: center;
                }
                </style>
                """, unsafe_allow_html=True)
        st.markdown('<p class="big-font">Image2CTR</p>', unsafe_allow_html=True)
        st.markdown('<p class="big-font2">Predict ad engagement for afar</p>', unsafe_allow_html=True)


#App description
st.write("This app can help evaluate performance for a given creative using Image processing. ")
st.write('Project Info: *Add slide* | Code Repo: *Add Repo | Contact Info: *Add Contact*')
st.markdown('***')


#Set the selectbox for demo images
st.write('**Select an image for a DEMO**')
menu = ['Select an Image','Dog', 'Coffee', "Women's Fashion"]
choice = st.selectbox('Select an image', menu)



#Set the box for the user to upload an image
st.write("**Upload your Image**")
uploaded_image = st.file_uploader("Upload your image in JPG or PNG format", type=["jpg", "png"])


def Loader(img_path=None,uploaded_image=None, upload_state=False, demo_state=True):
        test_loader = {}
        if choice == 'Dog':
           test_loader['image_dir'] = image_1
           test_loader['score'] = 100

        elif choice == 'Coffee':
           test_loader['image_dir'] = image_2
           test_loader['score'] = 65


        elif choice == "Women's Fashion":
           test_loader['image_dir'] = image_3
           test_loader['score'] = 35

        return test_loader

def deploy(file_path=None,uploaded_image=uploaded_image, uploaded=False, demo=True):
        st.markdown('***')
        if demo:
            test_loader = Loader()

        st.sidebar.success("Image uploaded Successfully!")
        st.sidebar.image(f'{test_loader["image_dir"] + choice}.png', width=301, channels='BGR')
        good_images_dir = test_loader["image_dir"] + 'good_images'
        bad_images_dir = test_loader["image_dir"] + 'bad_images'
        good_images = []
        bad_images = []
        # st.image(os.path.join(good_images,images), use_column_width=True)
        for image in os.listdir(good_images_dir):
            if image.endswith('.png'):
                good_image = os.path.join(good_images_dir,image)
                good_images.append(good_image)

        for image in os.listdir(bad_images_dir):
            if image.endswith('.png'):
                bad_image = os.path.join(bad_images_dir,image)
                bad_images.append(bad_image)


        st.write('<p class="big-font">Better performing similar imagery</p>', unsafe_allow_html=True)
        # image_iterator = paginator("Select a dog image", good_images)
        # indices_on_page, images_on_page = map(list, zip(*image_iterator))

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.image(good_images[0], width=300)
        with col2:
            st.image(good_images[1], width=300)
        with col3:
            st.image(good_images[2], width=300)

        st.markdown("""""")
        st.write('<p class="big-font">Worst performing similar imagery</p>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            st.image(bad_images[0], width=300)
        with col2:
            st.image(bad_images[1], width=300)
        with col3:
            st.image(bad_images[2], width=300)


        st.title("Summary")
        st.write(score_translation(test_loader["score"]))


#Deploy the model if the user uploads an image
if uploaded_image is not None:
    #Close the demo
    choice='Select an Image'
    #Deploy the model with the uploaded image
    deploy(uploaded_image, uploaded=True, demo=False)
    del uploaded_image


if choice != 'Select an Image':
    test_loader = Loader()
    v_custom = st_gauge_chart('Here are your results!', test_loader['score'])
    st.write(v_custom)
    deploy()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':



