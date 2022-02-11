% Homework: MATLAB 1
% COVID-19 Infection:
% This MATLAB script takes inputs for; s, u, y, A, B1, B2, and a. It then 
% computes the values for R and ac to determine appropriate public health
% action. 

clc; clear;

% INPUTS
s = input('coefficient sigma:  ');
u = input('coefficient mu:     ');
y = input('coefficient gamma:  ');
A = input('coefficient delta:  ');
B1 = input('coefficient beta 1: ');
B2 = input('coefficient beta 2: ');
a = input('parameter alpha:    ');

% CALCULATEY SHITS
F = (A *((B1 * s) + (y + u)* B2)) / ((s + u)*(y + u)* u);
R = (1 - a)* F;
ac = 1 - (1/F);

fprintf('reproduction number R_o:  %0.2f\n', R)
fprintf('threshold coefficient for action is alpha_c:  %0.2f\n', ac)

% CONDITIONALS
if and(R == 1, a < ac)
    fprintf('Endemic state, Increase Public Health Measures\n')
elseif and(R == 1, a >= ac)
    fprintf('No change in current Public Health Measure\n')
elseif and(R > 1, a < ac)
    fprintf('Disease expansion state, Increase Public Health Measures\n')
elseif and(R > 1, a >= ac)
    fprintf('No change in current Public Health Measure\n')
elseif and(R < 1, a > ac)
    fprintf('Disease controlled, Decrease Public Health Measures\n')
else
    fprintf('No change in current Public Health Measure\n')
end




