class DataException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def fit_trendline(year_timestamps, data):
    try:
        result = linregress(year_timestamps, data)
    except TypeError:
        raise DataException("Got an invalid data input. Both lists need to contain floats or integers")
    else:
        slope = round(result.slope, 3)
        r_squared = round(result.rvalue**2, 3)
        return slope, r_squared