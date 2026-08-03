import re
import requests
import tldextract

from bs4 import BeautifulSoup
from urllib.parse import urlparse


def extract_features(url):

    features = {}

    try:

        # ==============================
        # URL BASIC FEATURES
        # ==============================

        parsed = urlparse(url)

        domain = parsed.netloc

        ext = tldextract.extract(url)

        tld = ext.suffix


        features["URLLength"] = len(url)

        features["DomainLength"] = len(domain)


        # IP Address detection

        features["IsDomainIP"] = (
            1 if re.match(
                r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                domain
            )
            else 0
        )


        features["TLD"] = tld



        # ==============================
        # URL CHARACTER FEATURES
        # ==============================


        features["URLSimilarityIndex"] = 0.0


        features["CharContinuationRate"] = (
            max(
                [
                    len(x)
                    for x in re.findall(
                        r"(.)\1+",
                        url
                    )
                ],
                default=0
            )
        )


        features["TLDLegitimateProb"] = (
            1 if tld in [
                "com",
                "org",
                "net",
                "edu",
                "gov"
            ]
            else 0.5
        )


        features["URLCharProb"] = (
            len(set(url))/len(url)
            if len(url)>0 else 0
        )


        features["TLDLength"] = len(tld)


        features["NoOfSubDomain"] = (
            len(ext.subdomain.split("."))
            if ext.subdomain
            else 0
        )



        # ==============================
        # OBFUSCATION FEATURES
        # ==============================


        suspicious_chars = [
            "@",
            "%",
            "-",
            "_",
            "~"
        ]


        obfuscated_chars = sum(
            url.count(c)
            for c in suspicious_chars
        )


        features["HasObfuscation"] = (
            1 if obfuscated_chars > 0 else 0
        )


        features["NoOfObfuscatedChar"] = (
            obfuscated_chars
        )


        features["ObfuscationRatio"] = (
            obfuscated_chars / len(url)
            if len(url)>0 else 0
        )



        # ==============================
        # LETTER / DIGIT FEATURES
        # ==============================


        letters = sum(
            c.isalpha()
            for c in url
        )

        digits = sum(
            c.isdigit()
            for c in url
        )


        features["NoOfLettersInURL"] = letters

        features["LetterRatioInURL"] = (
            letters / len(url)
        )


        features["NoOfDegitsInURL"] = digits

        features["DegitRatioInURL"] = (
            digits / len(url)
        )



        features["NoOfEqualsInURL"] = url.count("=")

        features["NoOfQMarkInURL"] = url.count("?")

        features["NoOfAmpersandInURL"] = url.count("&")



        special = len(
            re.findall(
                r"[^a-zA-Z0-9]",
                url
            )
        )


        features["NoOfOtherSpecialCharsInURL"] = special


        features["SpacialCharRatioInURL"] = (
            special / len(url)
        )



        features["IsHTTPS"] = (
            1 if parsed.scheme=="https"
            else 0
        )



        # ==============================
        # HTML FEATURES
        # ==============================


        try:

            response = requests.get(
                url,
                timeout=8,
                headers={
                    "User-Agent":
                    "Mozilla/5.0"
                }
            )

            html = response.text


        except:

            html = ""


        soup = BeautifulSoup(
            html,
            "html.parser"
        )



        lines = html.split("\n")


        features["LineOfCode"] = len(lines)


        features["LargestLineLength"] = max(
            [
                len(x)
                for x in lines
            ],
            default=0
        )



        # ==============================
        # TITLE FEATURES
        # ==============================


        title = ""


        if soup.title:

            title = soup.title.text.lower()


        features["HasTitle"] = (
            1 if title else 0
        )


        domain_word = ext.domain.lower()


        features["DomainTitleMatchScore"] = (
            1 if domain_word in title
            else 0
        )


        features["URLTitleMatchScore"] = (
            1 if ext.domain.lower()
            in url.lower()
            else 0
        )



        # ==============================
        # PAGE STRUCTURE FEATURES
        # ==============================


        features["HasFavicon"] = (
            1 if soup.find(
                "link",
                rel=lambda x:x and "icon" in x
            )
            else 0
        )


        features["Robots"] = (
            1 if "robots"
            in html.lower()
            else 0
        )


        features["IsResponsive"] = (
            1 if "viewport"
            in html.lower()
            else 0
        )


        features["NoOfURLRedirect"] = (
            len(
                response.history
            )
            if 'response' in locals()
            else 0
        )


        features["NoOfSelfRedirect"] = 0



        features["HasDescription"] = (
            1 if soup.find(
                "meta",
                attrs={
                    "name":"description"
                }
            )
            else 0
        )



        features["NoOfPopup"] = (
            html.lower().count(
                "alert("
            )
        )


        features["NoOfiFrame"] = len(
            soup.find_all("iframe")
        )



        # ==============================
        # FORM FEATURES
        # ==============================


        features["HasExternalFormSubmit"] = 0


        for form in soup.find_all("form"):

            action = form.get(
                "action",
                ""
            )

            if "http" in action:

                features["HasExternalFormSubmit"] = 1



        features["HasSocialNet"] = (
            1 if any(
                x in html.lower()
                for x in [
                    "facebook",
                    "twitter",
                    "instagram",
                    "linkedin"
                ]
            )
            else 0
        )


        features["HasSubmitButton"] = (
            1 if soup.find(
                "input",
                type="submit"
            )
            else 0
        )


        features["HasHiddenFields"] = (
            1 if soup.find(
                "input",
                type="hidden"
            )
            else 0
        )


        features["HasPasswordField"] = (
            1 if soup.find(
                "input",
                type="password"
            )
            else 0
        )



        # ==============================
        # KEYWORD FEATURES
        # ==============================


        text = html.lower()


        features["Bank"] = (
            1 if "bank"
            in text else 0
        )


        features["Pay"] = (
            1 if any(
                x in text
                for x in [
                    "pay",
                    "payment",
                    "paypal"
                ]
            )
            else 0
        )


        features["Crypto"] = (
            1 if any(
                x in text
                for x in [
                    "bitcoin",
                    "crypto",
                    "wallet"
                ]
            )
            else 0
        )


        features["HasCopyrightInfo"] = (
            1 if "copyright"
            in text
            else 0
        )



        # ==============================
        # RESOURCE FEATURES
        # ==============================


        features["NoOfImage"] = len(
            soup.find_all("img")
        )


        features["NoOfCSS"] = len(
            soup.find_all(
                "link",
                rel="stylesheet"
            )
        )


        features["NoOfJS"] = len(
            soup.find_all(
                "script"
            )
        )


        links = soup.find_all("a")


        features["NoOfSelfRef"] = sum(
            1 for l in links
            if url in l.get(
                "href",
                ""
            )
        )


        features["NoOfEmptyRef"] = sum(
            1 for l in links
            if l.get("href")
            in [
                "",
                "#",
                None
            ]
        )


        features["NoOfExternalRef"] = sum(
            1 for l in links
            if "http"
            in l.get(
                "href",
                ""
            )
        )



        return features



    except Exception as e:

        print("Feature extraction error:",e)

        return None