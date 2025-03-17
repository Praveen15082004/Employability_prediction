# Employability_prediction
This project utilizes a Machine Learning model to predict whether an individual is "Employable" or "Less Employable" based on their skills and attributes. It features an intuitive Gradio interface for quick and easy assessments.

Features

* Accepts ratings (1-5) for multiple employability factors.
* Utilizes a Logistic Regression model for reliable predictions.
* Provides a user-friendly Gradio interface.
* Easily deployable on Hugging Face Spaces.

How It Works

1.Enter ratings (1-5) for various attributes such as communication skills, confidence, and mental alertness.
2.Click "Submit" to receive an employability prediction.
3.The result will be displayed as:
    "Employable" (if you meet the criteria).
    "Less Employable" (if improvements are needed).

Deployment on Hugging Face Spaces

To deploy this project on Hugging Face Spaces, follow these steps:
1.Create a new Space on Hugging Face Spaces.
2.Select Gradio as the framework.
3.Upload all necessary project files:
   app.py
   requirements.txt
   Model files
4.Start the Space, and your Employability Predictor is live!

Requirements
Ensure you have the following dependencies installed before running the project:
pip install -r requirements.txt

Running the Project Locally
To run the project locally, execute:
python app.py
This will launch the Gradio interface in your browser.

Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

License
This project is open-source and available under the MIT License.

Developed with ❤️ for employability assessment.
