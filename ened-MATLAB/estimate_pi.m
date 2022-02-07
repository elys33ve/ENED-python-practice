% ACT_MATLAB_2p4
% MATLAB 2: REPETITION 
clc; clear;

% estimate the value of pi within an inputted accuracy range

% INPUT
a = input('desired accuracy:  ');
y = 0;
x = 0;

% CALCULATIONS
while not(a == abs((4*y) - pi))
    y = y + (((-1)^x) / (2 * x + 1));
    x = x + 1;
end

y = 4 * y;

% OUTPUT
fprintf('final value or y:  %d\n', y)
fprintf('number of terms needed:  %d\n', x)



