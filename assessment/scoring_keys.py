# MCMI-III Comprehensive Scoring System

# Modifying Indices
MODIFYING_INDICES = {
    'Validity Index (V)': {
        'questions': [65, 110, 157],  # These are representative items
        'threshold': 2,  # Invalid if 2 or more specific items are endorsed
        'interpretation': lambda score: "Invalid test - random responding likely." if score >= 2 else "Valid test response pattern."
    },
    'Disclosure Index (X)': {
        'questions': list(range(1, 175)),  # All items factor into disclosure
        'threshold': {'low': 34, 'high': 178},
        'interpretation': lambda score: (
            "Defensive response style - underreporting." if score < 34 else
            "Excessive disclosure - overreporting." if score > 178 else
            "Normal disclosure level."
        )
    },
    'Desirability Index (Y)': {
        'questions': [5, 12, 24, 36, 71, 89, 117, 130, 152, 173],  # Representative items
        'threshold': {'low': 20, 'high': 75},
        'interpretation': lambda score: (
            "Attempts to present self favorably." if score > 75 else
            "Unusually self-critical." if score < 20 else
            "Normal self-presentation."
        )
    },
    'Debasement Index (Z)': {
        'questions': [7, 22, 38, 53, 92, 127, 141, 158, 171],  # Representative items
        'threshold': 75,
        'interpretation': lambda score: (
            "Tendency to devalue self/exaggerate problems." if score > 75 else
            "No significant self-devaluation."
        )
    }
}

# Clinical Personality Pattern Scales
PERSONALITY_PATTERNS = {
    'Schizoid (1)': {
        'questions': [16, 25, 33, 46, 55, 64, 79, 99, 112, 124, 146, 159, 168],
        'interpretation': lambda score: (
            "Prominent schizoid personality pattern." if score >= 85 else
            "Present schizoid personality pattern." if score >= 75 else
            "Mild or moderate schizoid traits." if score >= 60 else
            "No significant schizoid features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6),
            'female': min(115, 32 + raw * 6.5)
        }[gender]
    },
    'Avoidant (2A)': {
        'questions': [7, 21, 40, 57, 87, 96, 104, 118, 133, 145, 151, 166],
        'interpretation': lambda score: (
            "Prominent avoidant personality pattern." if score >= 85 else
            "Present avoidant personality pattern." if score >= 75 else
            "Mild or moderate avoidant traits." if score >= 60 else
            "No significant avoidant features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 30 + raw * 7),
            'female': min(115, 28 + raw * 7.2)
        }[gender]
    },
    'Depressive (2B)': {
        'questions': [2, 5, 10, 22, 37, 54, 70, 89, 100, 111, 125, 136, 161, 170],
        'interpretation': lambda score: (
            "Prominent depressive personality pattern." if score >= 85 else
            "Present depressive personality pattern." if score >= 75 else
            "Mild or moderate depressive traits." if score >= 60 else
            "No significant depressive features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 5.5),
            'female': min(115, 32 + raw * 5.8)
        }[gender]
    },
    'Dependent (3)': {
        'questions': [4, 15, 20, 35, 50, 62, 81, 93, 115, 127, 138, 147, 165],
        'interpretation': lambda score: (
            "Prominent dependent personality pattern." if score >= 85 else
            "Present dependent personality pattern." if score >= 75 else
            "Mild or moderate dependent traits." if score >= 60 else
            "No significant dependent features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 6),
            'female': min(115, 30 + raw * 6.5)
        }[gender]
    },
    'Histrionic (4)': {
        'questions': [6, 19, 36, 58, 74, 82, 94, 116, 128, 139, 148, 167],
        'interpretation': lambda score: (
            "Prominent histrionic personality pattern." if score >= 85 else
            "Present histrionic personality pattern." if score >= 75 else
            "Mild or moderate histrionic traits." if score >= 60 else
            "No significant histrionic features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 30 + raw * 7),
            'female': min(115, 28 + raw * 7.5)
        }[gender]
    },
    'Narcissistic (5)': {
        'questions': [3, 8, 15, 30, 41, 59, 73, 88, 101, 119, 140, 149, 156, 163],
        'interpretation': lambda score: (
            "Prominent narcissistic personality pattern." if score >= 85 else
            "Present narcissistic personality pattern." if score >= 75 else
            "Mild or moderate narcissistic traits." if score >= 60 else
            "No significant narcissistic features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 5.5),
            'female': min(115, 32 + raw * 6)
        }[gender]
    },
    'Antisocial (6A)': {
        'questions': [9, 17, 31, 42, 60, 76, 86, 102, 120, 129, 141, 154, 164],
        'interpretation': lambda score: (
            "Prominent antisocial personality pattern." if score >= 85 else
            "Present antisocial personality pattern." if score >= 75 else
            "Mild or moderate antisocial traits." if score >= 60 else
            "No significant antisocial features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 6),
            'female': min(115, 30 + raw * 6.5)
        }[gender]
    },
    'Sadistic (6B)': {
        'questions': [11, 26, 32, 43, 51, 61, 77, 95, 103, 121, 142, 150, 155],
        'interpretation': lambda score: (
            "Prominent sadistic personality pattern." if score >= 85 else
            "Present sadistic personality pattern." if score >= 75 else
            "Mild or moderate sadistic traits." if score >= 60 else
            "No significant sadistic features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6),
            'female': min(115, 32 + raw * 6.5)
        }[gender]
    },
    'Compulsive (7)': {
        'questions': [12, 27, 44, 52, 67, 83, 106, 122, 130, 143, 157],
        'interpretation': lambda score: (
            "Prominent compulsive personality pattern." if score >= 85 else
            "Present compulsive personality pattern." if score >= 75 else
            "Mild or moderate compulsive traits." if score >= 60 else
            "No significant compulsive features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 7),
            'female': min(115, 30 + raw * 7.5)
        }[gender]
    },
    'Negativistic (8A)': {
        'questions': [13, 23, 45, 68, 84, 97, 107, 123, 131, 144, 153, 169],
        'interpretation': lambda score: (
            "Prominent negativistic personality pattern." if score >= 85 else
            "Present negativistic personality pattern." if score >= 75 else
            "Mild or moderate negativistic traits." if score >= 60 else
            "No significant negativistic features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6.5),
            'female': min(115, 32 + raw * 7)
        }[gender]
    },
    'Masochistic (8B)': {
        'questions': [14, 28, 34, 47, 56, 69, 85, 98, 108, 124, 132, 171],
        'interpretation': lambda score: (
            "Prominent masochistic personality pattern." if score >= 85 else
            "Present masochistic personality pattern." if score >= 75 else
            "Mild or moderate masochistic traits." if score >= 60 else
            "No significant masochistic features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6.5),
            'female': min(115, 32 + raw * 7)
        }[gender]
    }
}

# Severe Personality Pathology Scales
SEVERE_PATHOLOGY = {
    'Schizotypal (S)': {
        'questions': [18, 38, 53, 63, 72, 78, 92, 109, 117, 137],
        'interpretation': lambda score: (
            "Prominent schizotypal features." if score >= 85 else
            "Present schizotypal features." if score >= 75 else
            "Mild or moderate schizotypal traits." if score >= 60 else
            "No significant schizotypal features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 30 + raw * 8.5),
            'female': min(115, 28 + raw * 9)
        }[gender]
    },
    'Borderline (C)': {
        'questions': [1, 24, 48, 66, 80, 90, 105, 126, 134, 162],
        'interpretation': lambda score: (
            "Prominent borderline features." if score >= 85 else
            "Present borderline features." if score >= 75 else
            "Mild or moderate borderline traits." if score >= 60 else
            "No significant borderline features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 8),
            'female': min(115, 30 + raw * 8.5)
        }[gender]
    },
    'Paranoid (P)': {
        'questions': [1, 6, 11, 29, 39, 49, 65, 75, 91, 113, 135, 160],
        'interpretation': lambda score: (
            "Prominent paranoid features." if score >= 85 else
            "Present paranoid features." if score >= 75 else
            "Mild or moderate paranoid traits." if score >= 60 else
            "No significant paranoid features."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 32 + raw * 7),
            'female': min(115, 30 + raw * 7.5)
        }[gender]
    }
}

# Clinical Syndrome Scales
CLINICAL_SYNDROMES = {
    'Anxiety (A)': {
        'questions': [8, 23, 39, 57, 82, 95, 110, 122, 134, 145, 158],
        'interpretation': lambda score: (
            "Prominent anxiety disorder symptoms." if score >= 85 else
            "Present anxiety symptoms." if score >= 75 else
            "Mild or moderate anxiety." if score >= 60 else
            "No significant anxiety symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 7),
            'female': min(115, 32 + raw * 7.5)
        }[gender]
    },
    'Somatoform (H)': {
        'questions': [5, 21, 44, 65, 81, 99, 116, 139, 152, 161, 167],
        'interpretation': lambda score: (
            "Prominent somatoform symptoms." if score >= 85 else
            "Present somatoform symptoms." if score >= 75 else
            "Mild or moderate somatic concerns." if score >= 60 else
            "No significant somatoform symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 7.5),
            'female': min(115, 30 + raw * 8)
        }[gender]
    },
    'Bipolar: Manic (N)': {
        'questions': [2, 16, 30, 45, 58, 74, 93, 106, 117, 132, 153],
        'interpretation': lambda score: (
            "Prominent manic symptoms." if score >= 85 else
            "Present manic symptoms." if score >= 75 else
            "Mild or moderate mood elevation." if score >= 60 else
            "No significant manic symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 7),
            'female': min(115, 32 + raw * 7.5)
        }[gender]
    },
    'Dysthymia (D)': {
        'questions': [9, 29, 37, 46, 63, 79, 100, 111, 125, 140, 158],
        'interpretation': lambda score: (
            "Prominent dysthymic symptoms." if score >= 85 else
            "Present dysthymic symptoms." if score >= 75 else
            "Mild or moderate depressive symptoms." if score >= 60 else
            "No significant dysthymic symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 7.5),
            'female': min(115, 30 + raw * 8)
        }[gender]
    },
    'Alcohol Dependence (B)': {
        'questions': [4, 18, 31, 49, 66, 83, 97, 114, 120, 135, 151],
        'interpretation': lambda score: (
            "Prominent alcohol dependence issues." if score >= 85 else
            "Present alcohol use problems." if score >= 75 else
            "Mild or moderate alcohol use patterns." if score >= 60 else
            "No significant alcohol dependence issues."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 7),
            'female': min(115, 32 + raw * 7.5)
        }[gender]
    },
    'Drug Dependence (T)': {
        'questions': [7, 22, 26, 54, 71, 87, 107, 128, 138, 149, 165],
        'interpretation': lambda score: (
            "Prominent drug dependence issues." if score >= 85 else
            "Present drug use problems." if score >= 75 else
            "Mild or moderate substance use patterns." if score >= 60 else
            "No significant drug dependence issues."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 7.5),
            'female': min(115, 30 + raw * 8)
        }[gender]
    },
    'Post-Traumatic Stress (R)': {
        'questions': [6, 12, 32, 42, 51, 77, 85, 98, 109, 127, 136, 150],
        'interpretation': lambda score: (
            "Prominent PTSD symptoms." if score >= 85 else
            "Present PTSD symptoms." if score >= 75 else
            "Mild or moderate trauma-related symptoms." if score >= 60 else
            "No significant PTSD symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6.5),
            'female': min(115, 32 + raw * 7)
        }[gender]
    }
}

# Severe Clinical Syndrome Scales
SEVERE_SYNDROMES = {
    'Thought Disorder (SS)': {
        'questions': [3, 17, 35, 53, 72, 96, 113, 126, 141, 156, 169],
        'interpretation': lambda score: (
            "Prominent thought disorder symptoms." if score >= 85 else
            "Present thought disorder symptoms." if score >= 75 else
            "Mild or moderate thought disturbance." if score >= 60 else
            "No significant thought disorder symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 7.5),
            'female': min(115, 30 + raw * 8)
        }[gender]
    },
    'Major Depression (CC)': {
        'questions': [10, 24, 34, 48, 56, 80, 94, 108, 123, 142, 159, 164],
        'interpretation': lambda score: (
            "Prominent major depression symptoms." if score >= 85 else
            "Present major depression symptoms." if score >= 75 else
            "Mild or moderate depressive patterns." if score >= 60 else
            "No significant major depression symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 35 + raw * 6.5),
            'female': min(115, 32 + raw * 7)
        }[gender]
    },
    'Delusional Disorder (PP)': {
        'questions': [13, 25, 38, 47, 64, 69, 78, 91, 105, 115, 129, 143, 157, 163],
        'interpretation': lambda score: (
            "Prominent delusional symptoms." if score >= 85 else
            "Present delusional symptoms." if score >= 75 else
            "Mild or moderate unusual beliefs." if score >= 60 else
            "No significant delusional symptoms."
        ),
        'br_conversion': lambda raw, gender: {
            'male': min(115, 33 + raw * 6),
            'female': min(115, 30 + raw * 6.5)
        }[gender]
    }
}

# Combine all scales into one comprehensive dictionary
MCMI_III_SCORING_KEYS = {
    **MODIFYING_INDICES,
    **PERSONALITY_PATTERNS,
    **SEVERE_PATHOLOGY,
    **CLINICAL_SYNDROMES,
    **SEVERE_SYNDROMES
}

# Function to score an MCMI-III test
def score_mcmi_iii(responses, gender='female'):
    """
    Score an MCMI-III test based on responses.

    Parameters:
    responses (dict): Dictionary with question numbers as keys and True/False responses as values
    gender (str): 'male' or 'female' for gender-specific BR score conversion

    Returns:
    dict: Dictionary with scale scores, BR scores, and interpretations
    """
    results = {}

    # Check validity first
    v_scale_score = sum(1 for q in MODIFYING_INDICES['Validity Index (V)']['questions'] if responses.get(q, False))
    if v_scale_score >= MODIFYING_INDICES['Validity Index (V)']['threshold']:
        return {
            'valid': False,
            'message': "Test results invalid - random responding likely. Validity Index (V) score exceeds threshold."
        }

    # Score each scale
    for scale_name, scale_info in MCMI_III_SCORING_KEYS.items():
        if 'questions' in scale_info:
            # Calculate raw score
            raw_score = sum(1 for q in scale_info['questions'] if responses.get(q, False))

            # Calculate BR score if applicable
            br_score = None
            if 'br_conversion' in scale_info:
                try:
                    br_score = scale_info['br_conversion'](raw_score, gender)
                except KeyError:
                    br_score = None

            # Get interpretation if applicable
            interpretation = None
            if 'interpretation' in scale_info:
                interpretation = scale_info['interpretation'](br_score if br_score is not None else raw_score)

            section_mapping = {
                'Disclosure Index (X)': 'Modifying Indices',
                'Desirability Index (Y)': 'Modifying Indices',
                'Debasement Index (Z)': 'Modifying Indices',

                'Schizoid': 'Personality Patterns',
                'Avoidant': 'Personality Patterns',
                'Depressive': 'Personality Patterns',
                'Dependent': 'Personality Patterns',
                'Histrionic': 'Personality Patterns',
                'Narcissistic': 'Personality Patterns',
                'Antisocial': 'Personality Patterns',
                'Sadistic (Aggressive)': 'Personality Patterns',
                'Compulsive': 'Personality Patterns',
                'Negativistic (Passive-Aggressive)': 'Personality Patterns',
                'Masochistic (Self-Defeating)': 'Personality Patterns',

                'Anxiety': 'Clinical Syndromes',
                'Somatoform': 'Clinical Syndromes',
                'Bipolar: Manic': 'Clinical Syndromes',
                'Dysthymia': 'Clinical Syndromes',
                'Alcohol Dependence': 'Clinical Syndromes',
                'Drug Dependence': 'Clinical Syndromes',
                'Post-Traumatic Stress Disorder': 'Clinical Syndromes',
                'Thought Disorder': 'Clinical Syndromes',
                'Major Depression': 'Clinical Syndromes',
                'Delusional Disorder': 'Clinical Syndromes',
            }

            # Store results
            results[scale_name] = {
                'raw_score': raw_score,
                'br_score': br_score,
                'interpretation': interpretation,
                "section": section_mapping.get(scale_name, "Unknown")
            }

    # Generate summary
    elevated_scales = [
        scale for scale, data in results.items()
        if 'br_score' in data and isinstance(data['br_score'], (int, float)) and data['br_score'] >= 75
    ]

    clinical_concerns = any(
        isinstance(data.get('br_score'), (int, float)) and data['br_score'] >= 85
        for data in results.values()
    )


    summary = {
        'valid': True,
        'elevated_scales': elevated_scales,
        'clinical_concerns': clinical_concerns,
        'results': results
    }

    return summary

# Example usage:
"""
# Example responses (True/False for 175 questions)
responses = {1: True, 2: False, 3: True, ...}  # Fill in with actual responses

# Score the test
result = score_mcmi_iii(responses, gender='female')

# Print results
if result['valid']:
    print("Valid test results")
    print(f"Elevated scales: {result['elevated_scales']}")
    
    for scale, data in result['results'].items():
        if 'br_score' in data and data['br_score'] >= 60:
            print(f"{scale}: BR Score {data['br_score']} - {data['interpretation']}")
else:
    print(result['message'])
"""