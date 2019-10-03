def get_pair_stats(pair):
    """ Returns statistics related to pair similarity """
    dld = editdistance.eval(pair[0][1], pair[1][1])
    avg_len = ( len(pair[0][1]) + len(pair[1][1]) ) / 2.0
    percent = 100.0 * (1 - (dld / avg_len))
    return((percent, dld, pair[0], pair[1]))
