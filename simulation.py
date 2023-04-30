import ltspice
import numpy as np

R1 = 10000  # 10k Ohm resistor
R2 = 10000
R3 = 10000
R4 = 10000
R_tol = 0.01  # 1% tolerance
V_inv = 1.5  
V_noninv = 2.5
opamp_model = 'OP07'
schematic_path = r'\circuit.asc'
# Running simulation
l = ltspice.Ltspice(schematic_path)
l.set_sim_param('VINV', V_inv)
l.set_sim_param('VNONINV', V_noninv)
l.run()
time = l.get_time()
V_in = l.get_data('V(in)')
V_out = l.get_data('V(out)')
V_diff = V_noninv - V_inv
V_expected = V_diff * (R2 + R4) / (R1 + R2 + R3 + R4)
# Comparasion for expected voltage with DC steady state voltage
V_dc = np.mean(V_out[-1000:])  # last 1000 samples are considered for DC voltage
if abs(V_expected - V_dc) <= 1e-4:
    print('DC steady state voltage matches expected analog voltage')
else:
    print(f'DC steady state voltage: {V_dc:.4f} V')
    print(f'Expected analog voltage: {V_expected:.4f} V')

# min and max o/p voltage based on tolerances
R_min = (1 - R_tol) * R1
R_max = (1 + R_tol) * R1
V_out_min = V_diff * (R2 + R4) / (R_max + R2 + R3 + R4)
V_out_max = V_diff * (R2 + R4) / (R_min + R2 + R3 + R4)
print(f'Minimum output voltage: {V_out_min:.4f} V')
print(f'Maximum output voltage: {V_out_max:.4f} V')
# Freq response of circuit
from matplotlib import pyplot as plt
from scipy.signal import freqresp
s = 1j * 2 * np.pi * np.logspace(-1, 6, 1000)
G = (R2 + R4) / (R1 + R2 + R3 + R4)
H = 1 / (1 + G / opamp_model + s * R3 * G)
_, mag, phase = freqresp((G, [1, opamp_model, 0], H), w=s)
fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(8, 8))
ax1.semilogx(s/(2*np.pi), 20*np.log10(mag))
ax1.set_ylabel('Magnitude (dB)')
ax1.set_title('Frequency Response')
ax2.semilogx(s/(2*np.pi), phase*180/np.pi)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Phase (deg)')
plt.show()
