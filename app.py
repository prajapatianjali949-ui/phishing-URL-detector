from flask import Flask, request, render_template
import joblib
from feature_extraction import extract_features
from virustotal_api import check_url_virustotal

app = Flask(__name__)

# Load model
model = joblib.load("phishing_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    vt_result = None

    if request.method == "POST":

        url = request.form.get("url")

        try:
            # Extract features
            features = extract_features(url)

            # Prediction
            prediction = model.predict(features)[0]
            prediction_proba = model.predict_proba(features)[0]

            confidence = max(prediction_proba) * 100

            # 🔹 Smart confidence boost for safe sites
            if prediction == 0:
                if url.startswith("https"):
                    confidence += 10

                if confidence > 95:
                    confidence = 95

            # Result
            if prediction == 1:
                result = f"⚠ Phishing Website Detected (AI) - {confidence:.2f}% confidence"
            else:
                result = f"✅ Legitimate Website (AI) - {confidence:.2f}% confidence"

        except Exception :
            result = "Error analyzing URL"

        # VirusTotal
        try:
            vt_result = check_url_virustotal(url)
        except:
            vt_result = "VirusTotal scan unavailable"

    return render_template("index.html", result=result, vt_result=vt_result)


if __name__ == "__main__":
    app.run(debug=True)