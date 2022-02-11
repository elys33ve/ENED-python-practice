% ACT_MATLAB_1p4
% MATLAB 1: SEQUENTIAL AND CONDITIONAL
clc; clear;

% perform specified function on inputted values

% INPUTS
user = input('Function:  ', 's');
A = input('Amplitude:  ');
t = input('t value:  ');

% SIN FUNCTION
if user == 'sin'
    f = input('Frequency:  ');
    y = A * sin(2 * pi * f * t);
% COS FUNCTION
elseif user == 'cos'
    f = input('Frequency:  ');
    y = A * cos(2 * pi * f * t);
% EXPONENTAL FUNCTION
elseif user == 'exp'
    tau = input('Time constant:  ');
    y = A * exp(1) ^ (-t / tau);
else
    fprintf('invalid input for function\n')
end

% OUTPUT
fprintf('y = %d\n', y)


