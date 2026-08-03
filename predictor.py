import os
import joblib
import pandas as pd
from urllib.parse import urlparse
from feature_extractor import extract_features


KNOWN_SHORTENERS = {
    "bit.ly", "tinyurl.com", "t.co", "goo.gl", "ow.ly", "is.gd",
    "buff.ly", "adf.ly", "bl.ink", "rebrand.ly", "cutt.ly", "shorte.st",
    "s.id", "tiny.cc", "lnkd.in", "rb.gy", "shorturl.at", "v.gd",
}


class Predictor:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "models", "phishing_decision_tree_pipeline.pkl")
        self.model = joblib.load(model_path)

    def _is_shortened_url(self, url):
        try:
            domain = urlparse(url).netloc.lower()
            domain = domain.replace("www.", "")
            return domain in KNOWN_SHORTENERS
        except Exception:
            return False

    def predict(self, url):
        features = extract_features(url)

        if features is None:
            return None

        df = pd.DataFrame([features])

        prediction = self.model.predict(df)[0]

        if hasattr(self.model, "predict_proba"):
            probability = self.model.predict_proba(df)[0]
            confidence = float(max(probability))
        else:
            confidence = 1.0

        is_shortened = self._is_shortened_url(url)
        is_unreachable = features.get("FetchFailed") == 1

     
        if is_shortened and prediction == 0:
            return {
                "prediction": 1,
                "confidence": confidence,
                "features": features,
                "warning": (
                    "This is a shortened URL. The real destination is hidden, "
                    "so it is flagged as suspicious regardless of the model's "
                    "content-based prediction."
                ),
                "overridden": True,
            }

    
        if is_unreachable and prediction == 0:
            return {
                "prediction": 1,
                "confidence": confidence,
                "features": features,
                "warning": (
                    "The site could not be reached, so content-based signals "
                    "(images, scripts, forms, title, etc.) were all empty. "
                    "This makes a 'Legitimate' verdict unreliable here, so "
                    "it is flagged as suspicious instead."
                ),
                "overridden": True,
            }

        return {
            "prediction": int(prediction),
            "confidence": confidence,
            "features": features,
            "warning": None,
            "overridden": False,
        }
