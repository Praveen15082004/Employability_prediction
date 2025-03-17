import joblib
import gradio as gr
import numpy as np
import os

MODEL_FILE = os.path.join(os.getcwd(), "employability_model_selected.joblib")
ENCODER_FILE = os.path.join(os.getcwd(), "label_encoder_fixed.joblib")

classifier = joblib.load(MODEL_FILE)
encoder = joblib.load(ENCODER_FILE)

feature_columns = [
    "Manner of Speaking",
    "Self-Confidence",
    "Ability to Present Ideas",
    "Communication Skills",
    "Mental Alertness"
]

def assess_employability(speaking, confidence, idea_presentation, communication, alertness):
    
    data_input = np.array([[speaking, confidence, idea_presentation, communication, alertness]])
    
    import pandas as pd
    input_df = pd.DataFrame(data_input, columns=feature_columns)

    predicted_class = classifier.predict(input_df)[0]
    prediction_label = encoder.inverse_transform([predicted_class])[0]
    
    return f"🎯 {prediction_label}" if prediction_label == "Employable" else f"❌ {prediction_label}"

ui = gr.Interface(
    fn=assess_employability,
    inputs=[
        gr.Slider(1, 5, step=1, label="Manner of Speaking "),
        gr.Slider(1, 5, step=1, label="Self-Confidence "),
        gr.Slider(1, 5, step=1, label="Idea Presentation "),
        gr.Slider(1, 5, step=1, label="Communication Skills "),
        gr.Slider(1, 5, step=1, label="Mental Alertness ")
    ],
    outputs=gr.Textbox(label="Your Employability Status"),
    title="Employability Prediction",
    description="Evaluate your employability potential by rating yourself on key soft skills. Get instant feedback!"
)

if __name__ == "__main__":
    ui.launch()
