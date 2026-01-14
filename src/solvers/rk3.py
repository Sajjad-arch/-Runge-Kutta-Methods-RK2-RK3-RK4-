def rk3_step(f, x, y, h):
    k1 = f(x, y)
    k2 = f(x + h/2, y + h/2 * k1)
    k3 = f(x + h, y - h * k1 + 2 * h * k2)
    return y + h * (k1 + 4 * k2 + k3) / 6
