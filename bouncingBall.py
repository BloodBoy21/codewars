def bouncing_ball(h,bounce,window):
    canBounce = h > 0 and (bounce > 0 and bounce < 1) and window < h
    if not canBounce:
        return -1
    count = 1
    current_bounce = h * bounce
    while current_bounce > window:
        current_bounce *= bounce
        count += 2
    return count
