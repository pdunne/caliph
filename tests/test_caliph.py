from caliph import __version__, routines
from caliph.cli import calib, conv
import numpy as np
import fire


def test_version():
    assert __version__ == "0.2.0"


def test_calib():
    result = routines.pH_calibration([3.75, 9.49], 21.0)
    assert np.allclose(result, [1.05365854, 0.05078049])


def test_conv():
    result = routines.pH_convert(3.5, [1.05365854, 0.05078049])
    assert np.allclose(result, 3.738585365853657)
