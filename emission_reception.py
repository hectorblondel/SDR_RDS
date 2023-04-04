#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
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
from gnuradio import digital
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
import emission_reception_epy_block_0 as epy_block_0  # embedded python block
import emission_reception_epy_block_1 as epy_block_1  # embedded python block



from gnuradio import qtgui

class emission_reception(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "emission_reception")

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
        self.tap_num = tap_num = 110
        self.sps = sps = 20
        self.samp_rate = samp_rate = 1000000
        self.offset = offset = 13
        self.gain = gain = 40
        self.fw = fw = 10000
        self.fc = fc = 10000
        self.f = f = 2300000000
        self.df = df = 1000
        self.constellation = constellation = digital.constellation_8psk().base()
        self.alpha = alpha = 1

        ##################################################
        # Blocks
        ##################################################
        self._tap_num_range = Range(1, 200, 1, 110, 200)
        self._tap_num_win = GrRangeWidget(self._tap_num_range, self.set_tap_num, "Taps", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._tap_num_win)
        self._gain_range = Range(0, 100, 1, 40, 200)
        self._gain_win = GrRangeWidget(self._gain_range, self.set_gain, "'gain'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._gain_win)
        self._fc_range = Range(0, 100000, 1, 10000, 200)
        self._fc_win = GrRangeWidget(self._fc_range, self.set_fc, "cutoff frequency", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._fc_win)
        self._f_range = Range(1000, 10000000000, 1000, 2300000000, 200)
        self._f_win = GrRangeWidget(self._f_range, self.set_f, "fréquence porteuse", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._f_win)
        self._alpha_range = Range(0.01, 1, 0.01, 1, 200)
        self._alpha_win = GrRangeWidget(self._alpha_range, self.set_alpha, "Roll-Off", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._alpha_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(f, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.root_raised_cosine_filter_0_0 = filter.fir_filter_ccf(
            1,
            firdes.root_raised_cosine(
                2,
                samp_rate,
                (samp_rate/sps),
                alpha,
                tap_num))
        self.qtgui_freq_sink_x_1_0_0 = qtgui.freq_sink_c(
            (1024*8), #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            'Sortie', #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_1_0_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1_0_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_1_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_1_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1_0_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1_0_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_1_0_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_1_0_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_0_0_win)
        self.qtgui_eye_sink_x_0 = qtgui.eye_sink_c(
            1024, #size
            samp_rate, #samp_rate
            1, #number of inputs
            None
        )
        self.qtgui_eye_sink_x_0.set_update_time(0.10)
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(sps)
        self.qtgui_eye_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_eye_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_eye_sink_x_0.enable_tags(True)
        self.qtgui_eye_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_eye_sink_x_0.enable_autoscale(False)
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


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_eye_sink_x_0.set_line_label(i, "Eye [Re{{Data {0}}}]".format(round(i/2)))
                else:
                    self.qtgui_eye_sink_x_0.set_line_label(i, "Eye [Im{{Data {0}}}]".format(round((i-1)/2)))
            else:
                self.qtgui_eye_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_eye_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_eye_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_eye_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_eye_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_eye_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_eye_sink_x_0_win = sip.wrapinstance(self.qtgui_eye_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_eye_sink_x_0_win)
        self.qtgui_const_sink_x_0_2_0 = qtgui.const_sink_c(
            1024, #size
            'Sortie finale', #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_2_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_2_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_2_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_2_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_2_0.enable_grid(False)
        self.qtgui_const_sink_x_0_2_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_2_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_2_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_2_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_2_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_2_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_2_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_2_0_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_1 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_1.set_update_time(0.10)
        self.qtgui_const_sink_x_0_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_1.enable_autoscale(False)
        self.qtgui_const_sink_x_0_1.enable_grid(False)
        self.qtgui_const_sink_x_0_1.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_1_win = sip.wrapinstance(self.qtgui_const_sink_x_0_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_1_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)


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
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
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
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._offset_range = Range(0, 19, 1, 13, 200)
        self._offset_win = GrRangeWidget(self._offset_range, self.set_offset, "'offset'", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._offset_win)
        self._fw_range = Range(0, 100000, 1, 10000, 200)
        self._fw_win = GrRangeWidget(self._fw_range, self.set_fw, "transition width", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._fw_win)
        self.epy_block_1 = epy_block_1.blk()
        self.epy_block_0 = epy_block_0.blk(t0=00, nb_ech_par_symb=20)
        self._df_range = Range(0, 10000, 1, 1000, 200)
        self._df_win = GrRangeWidget(self._df_range, self.set_df, "'df'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_layout.addWidget(self._df_win)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.epy_block_0, 3), (self.epy_block_1, 3))
        self.connect((self.epy_block_0, 2), (self.epy_block_1, 2))
        self.connect((self.epy_block_0, 0), (self.epy_block_1, 0))
        self.connect((self.epy_block_0, 1), (self.epy_block_1, 1))
        self.connect((self.epy_block_0, 3), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.epy_block_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.epy_block_0, 1), (self.qtgui_const_sink_x_0_1, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_const_sink_x_0_2_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.epy_block_0, 0))
        self.connect((self.root_raised_cosine_filter_0_0, 0), (self.qtgui_eye_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_1_0_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.root_raised_cosine_filter_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "emission_reception")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_tap_num(self):
        return self.tap_num

    def set_tap_num(self, tap_num):
        self.tap_num = tap_num
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.alpha, self.tap_num))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.qtgui_eye_sink_x_0.set_samp_per_symbol(self.sps)
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.alpha, self.tap_num))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_eye_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1_0_0.set_frequency_range(0, self.samp_rate)
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.alpha, self.tap_num))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)

    def get_fw(self):
        return self.fw

    def set_fw(self, fw):
        self.fw = fw

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_f(self):
        return self.f

    def set_f(self, f):
        self.f = f
        self.uhd_usrp_source_0.set_center_freq(self.f, 0)

    def get_df(self):
        return self.df

    def set_df(self, df):
        self.df = df

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.root_raised_cosine_filter_0_0.set_taps(firdes.root_raised_cosine(2, self.samp_rate, (self.samp_rate/self.sps), self.alpha, self.tap_num))




def main(top_block_cls=emission_reception, options=None):

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
