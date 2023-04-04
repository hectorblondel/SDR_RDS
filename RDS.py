#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: hector
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
import RDS_epy_block_0_1 as epy_block_0_1  # embedded python block



from gnuradio import qtgui

class RDS(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "RDS")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.transition_width = transition_width = 4000
        self.t_d = t_d = 1/1187.5
        self.t0 = t0 = 20
        self.samp_rate = samp_rate = 320000
        self.num_taps = num_taps = 50
        self.fsk_deviation_hz = fsk_deviation_hz = 1
        self.f = f = 104300000
        self.cutoff_freq = cutoff_freq = 17000
        self.G = G = 40
        self.Constant = Constant = 0.5

        ##################################################
        # Blocks
        ##################################################
        self._transition_width_range = Range(0, 100000, 1000, 4000, 200)
        self._transition_width_win = GrRangeWidget(self._transition_width_range, self.set_transition_width, "'transition_width'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._transition_width_win)
        self._t0_range = Range(0, 70, 1, 20, 200)
        self._t0_win = GrRangeWidget(self._t0_range, self.set_t0, "'t0'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._t0_win)
        self._samp_rate_range = Range(0, 500000, 100, 320000, 200)
        self._samp_rate_win = GrRangeWidget(self._samp_rate_range, self.set_samp_rate, "'samp_rate'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._samp_rate_win)
        self._num_taps_range = Range(0, 100, 1, 50, 200)
        self._num_taps_win = GrRangeWidget(self._num_taps_range, self.set_num_taps, "'num_taps'", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._num_taps_win)
        self._f_range = Range(100000000, 110000000, 1000, 104300000, 200)
        self._f_win = GrRangeWidget(self._f_range, self.set_f, "fréquence de travail", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._f_win)
        self._G_range = Range(0, 60, 1, 40, 200)
        self._G_win = GrRangeWidget(self._G_range, self.set_G, "'G'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._G_win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0_0.set_center_freq(f, 0)
        self.uhd_usrp_source_0_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0_0.set_gain(G, 0)
        self.root_raised_cosine_filter_0 = filter.fir_filter_fff(
            1,
            firdes.root_raised_cosine(
                1,
                samp_rate,
                1187.5,
                1,
                num_taps))
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_f(
            10240, #size
            samp_rate, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(270)
        self.qtgui_eye_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "Diagramme de l'oeil après filtrage")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(True)
        self.qtgui_eye_sink_x_0.enable_grid(False)
        self.qtgui_eye_sink_x_0.enable_axis_labels(True)
        self.qtgui_eye_sink_x_0.enable_control_panel(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'blue', 'blue', 'blue', 'blue',
            'blue', 'blue', 'blue', 'blue', 'blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_eye_sink_x_0.set_line_label(i, "Eye[Data {0}]".format(i))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_eye_sink_x_0_win)
        self.qtgui_const_sink_x_3 = qtgui.const_sink_c(
            512, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_3.set_update_time(0.10)
        self.qtgui_const_sink_x_3.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_3.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_3.enable_autoscale(False)
        self.qtgui_const_sink_x_3.enable_grid(False)
        self.qtgui_const_sink_x_3.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_3.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_3.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_3_win = sip.wrapinstance(self.qtgui_const_sink_x_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_3_win)
        self.qtgui_const_sink_x_2 = qtgui.const_sink_c(
            512, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_2.set_update_time(0.10)
        self.qtgui_const_sink_x_2.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_2.enable_autoscale(False)
        self.qtgui_const_sink_x_2.enable_grid(False)
        self.qtgui_const_sink_x_2.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_2_win = sip.wrapinstance(self.qtgui_const_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_2_win)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            512, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_1_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            512, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.low_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                1000,
                transition_width,
                window.WIN_BLACKMAN,
                6.76))
        self.epy_block_0_1 = epy_block_0_1.blk(t0=t0, nb_ech_par_symb=270)
        self._cutoff_freq_range = Range(0, 20000, 1, 17000, 200)
        self._cutoff_freq_win = GrRangeWidget(self._cutoff_freq_range, self.set_cutoff_freq, "'cutoff_freq'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._cutoff_freq_win)
        self.blocks_multiply_xx_0_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.band_pass_filter_0_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                55000 ,
                59000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                18000 ,
                20000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.analog_quadrature_demod_cf_0_0 = analog.quadrature_demod_cf(1)
        self._Constant_range = Range(0, 3, 0.01, 0.5, 200)
        self._Constant_win = GrRangeWidget(self._Constant_range, self.set_Constant, "'Constant'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._Constant_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0_0, 0), (self.band_pass_filter_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0_0_0, 0))
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_float_to_complex_0, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_multiply_xx_0_0_0, 1))
        self.connect((self.blocks_multiply_xx_0_0_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.epy_block_0_1, 3), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.epy_block_0_1, 2), (self.qtgui_const_sink_x_1, 0))
        self.connect((self.epy_block_0_1, 1), (self.qtgui_const_sink_x_2, 0))
        self.connect((self.epy_block_0_1, 0), (self.qtgui_const_sink_x_3, 0))
        self.connect((self.low_pass_filter_1, 0), (self.root_raised_cosine_filter_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.root_raised_cosine_filter_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.analog_quadrature_demod_cf_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "RDS")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 1000, self.transition_width, window.WIN_BLACKMAN, 6.76))

    def get_t_d(self):
        return self.t_d

    def set_t_d(self, t_d):
        self.t_d = t_d

    def get_t0(self):
        return self.t0

    def set_t0(self, t0):
        self.t0 = t0
        self.epy_block_0_1.t0 = self.t0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate, 18000 , 20000, 1000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(1, self.samp_rate, 55000 , 59000, 1000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 1000, self.transition_width, window.WIN_BLACKMAN, 6.76))
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, 1187.5, 1, self.num_taps))
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_num_taps(self):
        return self.num_taps

    def set_num_taps(self, num_taps):
        self.num_taps = num_taps
        self.root_raised_cosine_filter_0.set_taps(firdes.root_raised_cosine(1, self.samp_rate, 1187.5, 1, self.num_taps))

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.uhd_usrp_source_0_0.set_center_freq(self.f, 0)

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq

    def get_G(self):
        return self.G

    def set_G(self, G):
        self.G = G
        self.uhd_usrp_source_0_0.set_gain(self.G, 0)

    def get_Constant(self):
        return self.Constant

    def set_Constant(self, Constant):
        self.Constant = Constant




def main(top_block_cls=RDS, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
