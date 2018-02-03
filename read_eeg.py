#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 19:57:05 2018

@author: obarquero
"""

#read EEG and get signals

import mne
import matplotlib.pyplot as plt
import biosppy.signals.eeg as eeg
import numpy as np

raw_eeg = mne.io.read_raw_edf('./data/S001R01.edf',preload = True, verbose=False)

#get info
print('Num channels: %d',raw_eeg.info['nchan'])
print('Sampling freq[Hz]: %f',raw_eeg.info['sfreq'])

#get data as numpy array
eeg,time = raw_eeg[:,:]
fs = raw_eeg.info['sfreq']
#plot some channels

plt.plot(time,eeg[:3,:].T)

#EEG numpy array

signal = np.array(eeg)

#EEG Features
ts,filtro, features_ts,theta,alpha_low,alpha_high,beta,gamma,plf_pairs,plf = eeg(signal = signal, sampling_rate=fs) 