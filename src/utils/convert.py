def convert_to_float(frac_str):
	"""Returns frac_str converted to a float
    
    Arguments:
    frac_str -- the string to convert
    """
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        return float(num) / float(denom)
