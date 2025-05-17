from pyngrok import ngrok
import time

# Kill previous tunnels if rerun
ngrok.kill()

# Run Streamlit app
!streamlit run app.py &>/content/log.txt &

# Wait for Streamlit to launch
time.sleep(5)

# Expose app to public with ngrok
public_url = ngrok.connect(8501)
print(f"App is live at {public_url}")
