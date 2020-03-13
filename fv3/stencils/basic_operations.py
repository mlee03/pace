import fv3.utils.gt4py_utils as utils
import gt4py.gtscript as gtscript
from gt4py.gtscript import computation, interval, PARALLEL

sd = utils.sd


@gtscript.stencil(backend=utils.backend)
def adjustmentfactor_stencil(adjustment: sd, q_out: sd):
    with computation(PARALLEL), interval(...):
        q_out[0, 0, 0] = q_out * adjustment


@gtscript.stencil(backend=utils.backend)
def adjust_divide_stencil(adjustment: sd, q_out: sd):
    with computation(PARALLEL), interval(...):
        q_out[0, 0, 0] = q_out / adjustment


@gtscript.stencil(backend=utils.backend)
def multiply_stencil(in1: sd, in2: sd, out: sd):
    with computation(PARALLEL), interval(...):
        out[0, 0, 0] = in1 * in2


@gtscript.stencil(backend=utils.backend)
def divide_stencil(in1: sd, in2: sd, out: sd):
    with computation(PARALLEL), interval(...):
        out[0, 0, 0] = in1 / in2


@gtscript.stencil(backend=utils.backend)
def addition_stencil(in1: sd, in2: sd, out: sd):
    with computation(PARALLEL), interval(...):
        out[0, 0, 0] = in1 + in2


@gtscript.stencil(backend=utils.backend)
def add_term_stencil(in1: sd, out: sd):
    with computation(PARALLEL), interval(...):
        out[0, 0, 0] = out + in1


@gtscript.stencil(backend=utils.backend)
def add_term_two_vars(in1: sd, out1: sd, in2: sd, out2: sd):
    with computation(PARALLEL), interval(...):
        out1[0, 0, 0] = out1 + in1
        out2[0, 0, 0] = out2 + in2
