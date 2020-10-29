from collections import defaultdict

BATCH_SIZE = 128
MAX_LENGTH = 502
MAX_GPT2_LENGTH = 1000

MAX_PARAPHRASE_LENGTH = 100

BASE_CONFIG = {
    "keys": [
        {"key": "sent1_tokens", "position": 3, "tokenize": True, "metadata": False},
        {"key": "sent2_tokens", "position": 4, "tokenize": True, "metadata": False},
        {"key": "f1_score", "position": 5, "tokenize": False, "metadata": True},
        {"key": "kt_score", "position": 6, "tokenize": False, "metadata": True},
        {"key": "ed_score", "position": 7, "tokenize": False, "metadata": True},
        {"key": "langid", "position": 8, "tokenize": False, "metadata": True},
    ],
    "max_total_length": MAX_PARAPHRASE_LENGTH,
    "max_prefix_length": int(MAX_PARAPHRASE_LENGTH / 2),
    "max_suffix_length": int(MAX_PARAPHRASE_LENGTH / 2),
    "max_dense_length": 2
}

DATASET_CONFIG = {
    "paranmt": {
        "keys": [
            {"key": "sent1_tokens", "position": 0, "tokenize": True, "metadata": False},
            {"key": "sent2_tokens", "position": 1, "tokenize": True, "metadata": False},
            {"key": "f1_score", "position": 4, "tokenize": False, "metadata": True},
            {"key": "ed_score", "position": 5, "tokenize": False, "metadata": True},
            {"key": "f1_bucket", "position": 6, "tokenize": False, "metadata": True},
            {"key": "ed_bucket", "position": 7, "tokenize": False, "metadata": True}
        ]
    },
    "datasets/paranmt_filtered": BASE_CONFIG,
    "shakespeare/supervised": {
        "keys": [
            {"key": "sent1_tokens", "position": 0, "tokenize": True, "metadata": False},
            {"key": "sent2_tokens", "position": 1, "tokenize": True, "metadata": False},
            {"key": "f1_score", "position": 2, "tokenize": False, "metadata": True},
            {"key": "ed_score", "position": 3, "tokenize": False, "metadata": True}
        ]
    },
    "shakespeare/supervised_filtered": {
        "keys": [
            {"key": "sent1_tokens", "position": 0, "tokenize": True, "metadata": False},
            {"key": "sent2_tokens", "position": 1, "tokenize": True, "metadata": False},
            {"key": "f1_score", "position": 2, "tokenize": False, "metadata": True},
            {"key": "ed_score", "position": 3, "tokenize": False, "metadata": True}
        ]
    },
    # Shakespeare unsupervised data
    "shakespeare/unsupervised_filtered": BASE_CONFIG,
    "shakespeare/unsupervised_prior": BASE_CONFIG,
    "shakespeare/unsupervised_prior_detokenize": BASE_CONFIG,
    "formality/formality": BASE_CONFIG,
    "formality/formality_prior": BASE_CONFIG,
    "formality/formality_prior2_lowercase": BASE_CONFIG,
    "formality/formality_prior_detokenize": BASE_CONFIG,
    "dataset_pools/shakespeare_aae_tweets_bible_romantic-poetry_switchboard_coha_3_bins_lyrics_full": BASE_CONFIG,
    "dataset_pools/aae": BASE_CONFIG,
    "dataset_pools/bible": BASE_CONFIG,
    "dataset_pools/romantic-poetry": BASE_CONFIG,
    "dataset_pools/switchboard": BASE_CONFIG,
    "dataset_pools/english_tweets": BASE_CONFIG,
    "dataset_pools/lyrics_full": BASE_CONFIG,
    "dataset_pools/joyce": BASE_CONFIG,
    "dataset_pools/congress-bills": BASE_CONFIG,
    "dataset_pools/shakespeare": BASE_CONFIG,
    "dataset_pools/coha_3_bins_1810s-1820s": BASE_CONFIG,
    "dataset_pools/coha_3_bins_1890s-1900s": BASE_CONFIG,
    "dataset_pools/coha_3_bins_1990s-2000s": BASE_CONFIG
}

BASE_HP_CONFIG = {
    "max_total_length": MAX_GPT2_LENGTH,
    "max_prefix_length": int(MAX_GPT2_LENGTH / 2),
    "max_suffix_length": int(MAX_GPT2_LENGTH / 2),
    "max_dense_length": 4
}

# Fill in DATASET_CONFIG with keys it was missing previously
for dataset, config in DATASET_CONFIG.items():
    for base_key, base_value in BASE_CONFIG.items():
        if base_key not in config:
            config[base_key] = base_value
