import streamlit as st
import json
from streamlit_player import st_player

# Load data from JSON file
with open('beta2.json', 'r', encoding='utf-8') as f:
    videos_info = json.load(f)

# Add autoplay parameter to each video URL
for video in videos_info:
    video["url"] = video["url"] + "&autoplay=1"

# Initialize session state to track the current page and video index
if 'page' not in st.session_state:
    st.session_state.page = 'search'

if 'index' not in st.session_state:
    st.session_state.index = 0

if 'matching_videos' not in st.session_state:
    st.session_state.matching_videos = []

if 'show_artist' not in st.session_state:
    st.session_state.show_artist = False

if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Add logo to the top right corner
logo_path = "logo.jpeg"  # Replace with the path to your logo file

# Create columns and place the logo in the right column
header_col1, header_col2 = st.columns([4, 1])
with header_col2:
    st.image(logo_path, width=100)  # Adjust width as needed for best look

# Function to switch pages


def switch_page(page_name):
    st.session_state.page = page_name


# Search Functionality Page with Cascading Tags
if st.session_state.page == 'search':
    st.title("🔍 Search Videos by Tags")

    # Main Category Selection
    main_category = st.selectbox("Select a category:", [
                                 "Wedding", "Party", "Live"])

    # Sub-category Selection based on main category
    sub_category = None
    sub_sub_category_options = []
    if main_category == "Wedding":
        sub_category = st.selectbox("Select a type:", ["Instrumental", "DJ"])
        if sub_category == "Instrumental":
            sub_sub_category_options = ["Guitar", "Piano", "Violin"]

    elif main_category == "Party":
        sub_category = st.selectbox("Select a type:", ["Birthday", "Dinner"])
        if sub_category == "Birthday":
            sub_sub_category_options = ["Kids", "Adults"]
        elif sub_category == "Dinner":
            sub_sub_category_options = ["Jazz", "Instrumental"]

    elif main_category == "Live":
        sub_category = st.selectbox("Select a type:", ["Bar", "Club"])
        if sub_category == "Bar":
            sub_sub_category_options = ["Singer/Songwriter", "Rock"]

    # Checkbox Selection for Third-Level Tags
    selected_tags = []
    if sub_sub_category_options:
        st.markdown("### Select Additional Tags:")
        for option in sub_sub_category_options:
            if st.checkbox(option, key=f"sub_sub_{option}"):
                selected_tags.append(option)

    if sub_category:
        # Filter videos that match the selected main category, sub-category, and optional additional tags
        st.session_state.matching_videos = [
            video for video in videos_info
            if main_category in video["tags"]
            and sub_category in video["tags"]
            and (all(tag in video["tags"] for tag in selected_tags) if selected_tags else True)
        ]

        # Display the "Here are your matches" button with the number of matches
        num_matches = len(st.session_state.matching_videos)
        if st.button(f"Found {num_matches} matches - View Matches"):
            # Reset index to 0 for the matching videos player
            st.session_state.index = 0
            st.session_state.show_artist = False  # Reset artist view
            st.session_state.form_submitted = False  # Reset form submission state
            switch_page('matches')

# Video Player for Matching Videos (Search Results)
if st.session_state.page == 'matches':
    matching_videos = st.session_state.matching_videos

    if matching_videos:
        # Display the current video from the matching list
        current_video_info = matching_videos[st.session_state.index]
        st_player(current_video_info["url"], playing=True)

        # Display the title, artist, description, and tags in an aesthetic way
        st.markdown(
            f"### 🎵 Now Playing: {current_video_info['title']} by {current_video_info['artist']}")
        st.markdown(f"**Description**: {current_video_info['description']}")

        # Display tags with some styling
        st.markdown("**Tags**:")
        tag_str = ", ".join([f"`{tag}`" for tag in current_video_info["tags"]])
        st.markdown(tag_str)

        # Navigation buttons using columns for better alignment
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            next_clicked = st.button(
                "Next Video", key=f"next_video_{st.session_state.index}")
        with col2:
            view_artist_clicked = st.button(
                "View Artist Profile", key=f"view_artist_{st.session_state.index}")
        with col3:
            back_to_search_clicked = st.button(
                "Back to Search Results", key="back_to_search")

        # Handle button clicks with if/elif to prevent multiple triggers
        if next_clicked:
            # Update the session state index for the next video
            st.session_state.index = (
                st.session_state.index + 1) % len(matching_videos)
            # Hide artist info and contact form when moving to the next video
            st.session_state.show_artist = False
            st.session_state.form_submitted = False
            switch_page('matches')
        elif view_artist_clicked:
            st.session_state.show_artist = not st.session_state.show_artist  # Toggle artist view
        elif back_to_search_clicked:
            switch_page('search')

        # Display Artist Profile below the video only if "View Artist Profile" button is clicked
        if st.session_state.show_artist:
            st.markdown(
                f"## ✏️ Artist Profile: {current_video_info['artist']}")
            st.markdown(f"**Artist Name**: {current_video_info['artist']}")
            st.markdown(
                f"**Description**: {current_video_info['artist_description']}")
            # Use a dialog-style interface for contact form

            @st.dialog("📞 Contact the Artist")
            def contact_artist():
                name = st.text_input("Your Name")
                email = st.text_input("Your Email")
                phone = st.text_input("Your Phone Number")
                if st.button("Submit"):
                    st.session_state.form_submitted = True
                    st.rerun()
            if not st.session_state.form_submitted:
                if st.button("Contact Artist"):
                    contact_artist()
