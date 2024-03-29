from quadmodel.data.quad_base import Quad

class Mock1(Quad):

    def __init__(self, sourcemodel_type='NARROW_LINE_Gaussian',
                 macromodel_type='EPL_FIXED_SHEAR'):

        zlens = 0.5
        zsource = 2.0
        x = [1.11479788, -0.08983757,  0.55698859, -0.56995511]
        y = [-0.29678043,  1.06137241,  0.86675635, -0.47237552]
        m = [0.48206844, 0.78478408, 1., 0.18834882]
        delta_m = [0.0001, 0.0001, 0.0001, 0.0001]
        delta_xy = [0.001] * 4
        keep_flux_ratio_index = [0, 1, 2]

        self.log10_host_halo_mass = 13.3
        self.log10_host_halo_mass_sigma = 0.3

        kwargs_macromodel = {'shear_amplitude_min': 0.02, 'shear_amplitude_max': 0.16}

        super(Mock1, self).__init__(zlens, zsource, x, y, m, delta_m, delta_xy, sourcemodel_type, {}, macromodel_type,
                                    kwargs_macromodel, keep_flux_ratio_index)

