# This dictionary maps scales to question numbers considered "True" for that trait
SCORING_KEYS = {
    'Depressive': {
        'questions': [2, 5, 10],
        'interpretation': lambda score: (
            "Elevated depressive traits." if score >= 2 else
            "Mild depressive tendencies." if score == 1 else
            "No significant depressive features."
        ),
        'br_conversion': lambda raw: 75 if raw >= 3 else 60 if raw == 2 else 35
    },
    'Narcissistic': {
        'questions': [3, 8, 15],
        'interpretation': lambda score: (
            "High self-focus and need for admiration." if score >= 2 else
            "Some narcissistic features." if score == 1 else
            "No strong narcissistic traits."
        ),
        'br_conversion': lambda raw: 85 if raw == 3 else 60 if raw == 2 else 40
    },
    'Paranoid': {
        'questions': [1, 6, 11],
        'interpretation': lambda score: (
            "Suspiciousness and mistrust are prominent." if score >= 2 else
            "Mildly guarded or skeptical." if score == 1 else
            "No significant paranoid features."
        ),
        'br_conversion': lambda raw: 90 if raw == 3 else 65 if raw == 2 else 35
    },
}
