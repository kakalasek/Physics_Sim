from Anim.Anim2D import Anim2D
from Throw.Throw2D import Throw2D
from math import pi

if __name__ == "__main__":
    cannonBall = Throw2D(v0=20, y0=2, x0=2, theta=pi/8, t0=0.5)
    anim = Anim2D((0, 50), (0, 20), cannonBall)
    anim.start_animation()