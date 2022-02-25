% MATLAB 5: Task 1
% File:     ACT_MATLAB_6p1_TEAM256.m

clc; clear;


% INPUTS
F1 = input('Force 1 magnitude:  ');
theta1 = input('Force 1 angle:  ');

F2 = input('Force 2 magnitude:  ');
theta2 = input('Force 2 angle:  ');

units = input('units:  ','s');

% CALL FUNCTION
[Fr, Th_r] = Forces(F1, theta1, F2, theta2, units);

% OUTPUTS
fprintf('Fr = %d\n', Fr)
fprintf('Th_r = %d\n', Th_r)
