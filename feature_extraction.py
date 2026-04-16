import re
import numpy as np
import tldextract
import math
import datetime
import whois

SUSPICIOUS_WORDS = ['login','verify','update','secure','free','account','confirm']

BRAND_WORDS = ['paypal','bank','amazon','google','microsoft','github']

# 🔥 NEW: Trusted domains
TRUSTED_DOMAINS = [
    'google','youtube','facebook','amazon','microsoft',
    'github','wikipedia','twitter','instagram','linkedin'
]


def calculate_entropy(url):
    prob = [float(url.count(c)) / len(url) for c in set(url)]
    return -sum([p * math.log2(p) for p in prob])


def get_domain_age(domain):
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date is None:
            return 0

        today = datetime.datetime.now()
        return (today - creation_date).days
    except:
        return 0


def extract_features(url, use_whois=True):

    if not url.startswith("http"):
        url = "http://" + url

    features = []

    url_length = len(url)
    features.append(url_length)

    ext = tldextract.extract(url)
    domain = ext.domain
    tld = ext.suffix
    subdomain = ext.subdomain

    features.append(len(domain))

    is_ip = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', domain) else 0
    features.append(is_ip)

    features.append(len(tld))

    features.append(subdomain.count('.') + 1 if subdomain else 0)

    has_obfuscation = 1 if '@' in url or '-' in url else 0
    features.append(has_obfuscation)

    letters = sum(c.isalpha() for c in url)
    features.append(letters)
    features.append(letters / url_length if url_length else 0)

    digits = sum(c.isdigit() for c in url)
    features.append(digits)
    features.append(digits / url_length if url_length else 0)

    features.append(url.count('='))
    features.append(url.count('?'))
    features.append(url.count('&'))

    special_chars = sum(url.count(c) for c in ['%','!','$','#','^','*'])
    features.append(special_chars)
    features.append(special_chars / url_length if url_length else 0)

    # HTTPS
    features.append(1 if url.startswith('https') else 0)

    # Suspicious score
    features.append(sum(word in url.lower() for word in SUSPICIOUS_WORDS))

    # Brand score
    features.append(sum(word in url.lower() for word in BRAND_WORDS))

    # 🔥 NEW: Trusted domain score
    trusted_score = 1 if domain.lower() in TRUSTED_DOMAINS else 0
    features.append(trusted_score)

    # Entropy
    features.append(calculate_entropy(url))

    # Domain age
    full_domain = domain + "." + tld

    if use_whois:
        age_days = get_domain_age(full_domain)
        domain_age = 1 if age_days > 365 else 0
    else:
        domain_age = 1 if domain.lower() in TRUSTED_DOMAINS else 0

    features.append(domain_age)

    return np.array(features).reshape(1, -1)