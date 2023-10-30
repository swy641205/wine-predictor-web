# Given coefficients and values
coefficients = {
    'const': 150.1928,
    'fixed acidity': 0.0655,
    'volatile acidity': -1.8632,
    'residual sugar': 0.0815,
    'free sulfur dioxide': 0.0037,
    'density': -150.2842,
    'pH': 0.6863,
    'sulphates': 0.6315,
    'alcohol': 0.1935
}

values = {
    'fixed acidity': 7,
    'volatile acidity': 0.27,
    'residual sugar': 20.7,
    'free sulfur dioxide': 45,
    'density': 1.001,
    'pH': 3,
    'sulphates': 0.45,
    'alcohol': 8.8
}

# Compute predicted quality
predicted_quality = coefficients['const']
for key, value in values.items():
    predicted_quality += coefficients[key] * value

print(predicted_quality)
