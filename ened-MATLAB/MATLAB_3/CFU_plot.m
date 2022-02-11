% CFU_MATLAB_3
% MATLAB 3: 1-D ARRAYS AND PLOTTING 
clear; clc;

% CONSTANTS
k1 = 0.25;      % value 1
k2 = 0.5;       % value 2

lmax = 100;
T = 0.5;

% PLOT
t = 0:0.1:2;
       L1 = lmax*(1-exp(1).^(-k1*(t + T)));
       L2 = lmax*(1-exp(1).^(-k2*(t + T)));
       plot(t,L1,t,L2)
       xlabel('x-axis')
       ylabel('y-axis')
       title('CFU MATLAB 3')
       legend('L1','L2')
