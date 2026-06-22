"""Validates raw form input before it reaches the model."""

from config import fields, features


def validate(form) -> tuple[dict, list]:
    """
    Validates submitted form data against expected ranges.
    Returns (clean_values, errors). If errors is non-empty, clean_values
    should not be used for prediction.
    """
    values = {}
    errors = []

    for field in features:
        raw = form.get(field, '').strip()
        meta = fields[field]

        if raw == '':
            errors.append(f'{meta["label"]} is required.')
            continue

        try:
            num = float(raw)
        except ValueError:
            errors.append(f'{meta["label"]} must be a number.')
            continue

        if num < meta['min'] or num > meta['max']:
            errors.append(
                f'{meta["label"]} should be between {meta["min"]} and {meta["max"]}{meta["unit"]}.'
            )
            continue

        values[field] = num

    return values, errors