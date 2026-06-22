"Application configuration and constants."

# input fields the model expects, in order
features = ['Temperature', 'RH', 'Ws', 'Rain', 'FFMC', 'DMC', 'ISI']

# field definitions: label, unit, valid range, and helper text for the form
fields = {
    'Temperature': {
        'label': 'Temperature', 'unit': '°C', 'min': 0, 'max': 50, 'step': 0.1,
        'help': 'Noon air temperature'
    },
    'RH': {
        'label': 'Relative Humidity', 'unit': '%', 'min': 0, 'max': 100, 'step': 1,
        'help': 'Noon relative humidity'
    },
    'Ws': {
        'label': 'Wind Speed', 'unit': 'km/h', 'min': 0, 'max': 60, 'step': 0.1,
        'help': 'Noon wind speed'
    },
    'Rain': {
        'label': 'Rainfall', 'unit': 'mm', 'min': 0, 'max': 100, 'step': 0.1,
        'help': 'Rainfall in the last 24 hours'
    },
    'FFMC': {
        'label': 'FFMC', 'unit': '', 'min': 0, 'max': 101, 'step': 0.1,
        'help': 'Fine Fuel Moisture Code — surface litter dryness'
    },
    'DMC': {
        'label': 'DMC', 'unit': '', 'min': 0, 'max': 120, 'step': 0.1,
        'help': 'Duff Moisture Code — loosely packed organic layer'
    },
    'ISI': {
        'label': 'ISI', 'unit': '', 'min': 0, 'max': 40, 'step': 0.1,
        'help': 'Initial Spread Index — expected rate of fire spread'
    },
}

# FWI risk bands — thresholds follow standard FWI interpretation guidance
risk_bands = [
    {'max': 5, 'level': 'Low', 'action': 'Routine monitoring is sufficient.'},
    {'max': 12, 'level': 'Moderate', 'action': 'Increase patrol frequency in dry zones.'},
    {'max': 20, 'level': 'High', 'action': 'Restrict open burning. Brief field crews.'},
    {'max': float('inf'), 'level': 'Very High', 'action': 'Issue public advisory. Pre-position response teams.'},
]

max_fwi_scale = 31  # used for the visual scale bar

# Model file locations
model_path = 'models/model.pkl'
scaler_path = 'models/scaler.pkl'