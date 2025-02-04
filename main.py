import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, extract_body_content)
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL: ", autocomplete="off")

if st.button("Scrape Site"):
    
    st.write("Scraping the Website")
    
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    
    st.session_state.dom_content = cleaned_content
    
    parse_summary = "Give me a summary of this website"
    dom_chunks = split_dom_content(st.session_state.dom_content)
    result = parse_with_ollama(dom_chunks, parse_summary)
    
    with st.expander("View Summary"):
        st.text_area("Summary", result, height = 300)
    
if "dom_content" in st.session_state:
    parse_description = st.text_area("What would you like to know?")
    
    if st.button("Parse Content"):
        if parse_description:
            
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)
            
