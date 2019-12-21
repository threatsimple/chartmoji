

def chartmoji(vals, chart_type="ln"):
    """
    accept series of values (up to 5) and return a normalized chartmoji string
    for a line chart
    """
    assert chart_type in ("ln","bar")
    h=2.0
    if len(vals) > 5: return ''
    vals = [float(i) for i in vals]
    mn = float(min(vals))
    norm_vals = [ v-mn for v in vals ]
    starter = norm_vals[0]
    # if we're less than 5 in length, then pad the leading values with the first
    # value till we get to 5
    for i in range(5-len(norm_vals)):
        norm_vals.insert(0, starter)
    mx = float(max(norm_vals))
    series = "".join([str(int(round( (float(v)/mx) * h ))) for v in norm_vals])
    return f":chart_{chart_type}{series}:"

