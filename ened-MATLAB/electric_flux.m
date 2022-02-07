% Homework: MATLAB 1
% Electric Flux Density:
% This script allows the user to input the charge density (Pv), radial 
% distance (r), internal radius (a), and external radius (b). It then 
% determines the electric flux density (D), and outputs he value using 
% a print statement.

clc; clear;

% INPUTS
Pv = input('charge density (nC/cm^3): ');
r = input('radial distance (cm): ');
a = input('internal radius (cm): ');
b = input('external radius (cm): ');

% CONDITIONALS
if or(r <= a, 0 < r)
    D = (Pv*r)/2;
elseif r < b
    D = (Pv*a^2)/(2*r);
elseif b <= r
    D = 0;
else
    fprintf("invalid inputs")
end

% OUTPUT
fprintf('electric flux density (nC/cm^2): %0.1f\n', D)
