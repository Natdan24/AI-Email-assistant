import streamlit as st
import requests

# Streamlit UI
st.title("📝 AI Email Assistant (Local)")

tone = st.selectbox("Choose email tone:", ["Formal", "Friendly", "Apologetic", "Confident"])
bullet_points = st.text_area("Enter bullet points or key ideas:", height=200)

if st.button("Generate Email"):
    with st.spinner("Generating your email..."):
        prompt = f"Write a {tone.lower()} email based on the following points:\n{bullet_points}\n\nEmail:"

        # Send to LM Studio API
        try:
            response = requests.post(
                "http://localhost:1234/v1/chat/completions",
                headers={"Content-Type": "application/json"},
                json={
                    "model": "local-model",  # This can be left as-is for LM Studio
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
            )

            if response.status_code == 200:
                email = response.json()["choices"][0]["message"]["content"]
                st.markdown("### ✉️ Generated Email:")
                st.write(email)
            else:
                st.error(f"Error: {response.status_code}\n{response.text}")

        except requests.exceptions.ConnectionError:
            st.error("Could not connect to LM Studio. Make sure it's running with the local server enabled.")
