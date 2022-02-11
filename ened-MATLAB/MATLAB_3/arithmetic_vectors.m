% ACT_MATLAB_3
% MATLAB 3: 1-D ARRAYS AND PLOTTING 
clc; clear;

A = linspace(0,10,5);
B = 10:-2:2;
%length(A) == length(B)

C = A + B; 
D = A - B; 
E = A * B;          % error
F = A .* B; 
G = A / B;          % error
H = A ./ B; 
K = A ^ 3;          % error
L = A .^ 3; 
