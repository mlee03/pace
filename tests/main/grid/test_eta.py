#!/usr/bin/env python3

import os
import pytest
import numpy as np
from pace.util.grid import set_hybrid_pressure_coefficients

input_dir='./input/'

ak_ref = np.array(
    [
    300,      646.7159, 1045.222,
    1469.188, 1897.829, 2325.385,
    2754.396, 3191.294, 3648.332,
    4135.675, 4668.282, 5247.94,
    5876.271, 6554.716, 7284.521,
    8066.738, 8902.188, 9791.482,
    10734.99, 11626.25, 12372.12,
    12990.41, 13496.29, 13902.77,
    14220.98, 14460.58, 14629.93,
    14736.33, 14786.17, 14785.11,
    14738.12, 14649.66, 14523.7,
    14363.82, 14173.24, 13954.91,
    13711.48, 13445.4,  13158.9,
    12854.07, 12532.8,  12196.85,
    11847.88, 11487.39, 11116.82,
    10737.48, 10350.62, 9957.395,
    9558.875, 9156.069, 8749.922,
    8341.315, 7931.065, 7519.942,
    7108.648, 6698.281, 6290.007,
    5884.984, 5484.372, 5089.319,
    4700.96,  4320.421, 3948.807,
    3587.201, 3236.666, 2898.237,
    2572.912, 2261.667, 1965.424,
    1685.079, 1421.479, 1175.419,
    947.6516, 738.8688, 549.713,
    380.7626, 232.5417, 105.481,
    -0.0008381903, 0])

bk_ref = np.array([
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0, 0, 0,
    0,           0.001065947, 0.004128662,
    0.009006631, 0.01554263,  0.02359921,
    0.03305481,  0.0438012,   0.05574095,
    0.06878554,  0.08285347,  0.09786981,
    0.1137643,   0.130471,    0.1479275,
    0.1660746,   0.1848558,   0.2042166,
    0.2241053,   0.2444716,   0.2652672,
    0.286445,    0.3079604,   0.3297701,
    0.351832,    0.3741062,   0.3965532,
    0.4191364,   0.4418194,   0.4645682,
    0.48735,     0.5101338,   0.5328897,
    0.5555894,   0.5782067,   0.6007158,
    0.6230936,   0.6452944,   0.6672683,
    0.6889648,   0.7103333,   0.7313231,
    0.7518838,   0.7719651,   0.7915173,
    0.8104913,   0.828839,    0.846513,
    0.8634676,   0.8796583,   0.8950421,
    0.9095779,   0.9232264,   0.9359506,
    0.9477157,   0.9584892,   0.9682413,
    0.9769447,   0.9845753,   0.9911126,
    0.9965372,   1])


def write_files(ak_in=ak_ref, bk_in=bk_ref, eta_file='./input/eta79.txt'):

    """  Write eta files for testing """

    if os.path.isfile(eta_file) : cleanup(eta_file)
    os.mkdir(input_dir)
    with open(eta_file,'w') as myfile:
        for i in range(80): myfile.write('{0}  {1}\n'.format(ak_in[i],bk_in[i]))


def cleanup(eta_file='./input/eta79.txt') :

    """ Remove input directory """

    if( os.path.isfile(eta_file)  ) : os.remove(eta_file)
    if( os.path.isfile(input_dir) ) : os.rmdir(input_dir)


@pytest.mark.xfail
def test_set_hybrid_pressure_coefficients_nofile() :

    """ File does not exist.  Test should fail """

    km = 79
    pressure_data = set_hybrid_pressure_coefficients( km )


def test_set_hybrid_pressure_coefficients_correct(km=79) :

    """  Good values of ak, bk.  Test should pass """

    ak = ak_ref[:]
    bk = bk_ref[:]

    ak_answer=ak_ref[:]
    bk_answer=bk_ref[:]
    ks_answer = 18
    ptop_answer = 300.0

    write_files(ak_in=ak, bk_in=bk, eta_file='./input/eta79.txt')
    pressure_data = set_hybrid_pressure_coefficients( km )

    if( not np.array_equal(ak_answer,pressure_data.ak) ) :
        raise ValueError("Unexpected values in ak array")
    if( not np.array_equal(bk_answer,pressure_data.bk) ) :
        raise ValueError("Unexpected values in bk array")
    if( ks_answer != pressure_data.ks ) :
        raise ValueError("Unexpected ks value")
    if( ptop_answer != pressure_data.ptop) :
        raise ValueError("Unexpected ptopt value")

    cleanup('./input/eta79.txt')


@pytest.mark.xfail
def test_set_hybrid_pressure_coefficients_nonincreasing(km=79) :

    """
    Array bk is not monotonically increasing.
    Test is expected to fail
    """

    ak = ak_ref[:]
    bk = bk_ref[:]

    bk[10]=142. #random number

    write_files(ak_in=ak, bk_in=bk, eta_file="./input/eta79.txt")
    pressure_data = set_hybrid_pressure_coefficients( km )


def test_cleanup():
    cleanup("./input/eta79.txt")
