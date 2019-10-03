def get_pair_stats(two_things):
    # I definitely didn't copy from 1.py file
    # You can tell because I took the time to change the comments and identifiers
    edit_distance = editdistance.eval(two_things[0][1], two_things[1][1])

    # Do somthing important
    mean_length = ( len(two_things[0][1]) + len(two_things[1][1]) ) / 2.0
    
    ratio = 100.0 * (1.0 - (edit_distance / mean_length))

    # Return everything
    return((ratio, edit_distance, two_things[0], two_things[1]))
