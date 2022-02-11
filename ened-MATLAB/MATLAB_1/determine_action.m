% ACT_MATLAB_1p5
% MATLAB 1: SEQUENTIAL AND CONDITIONAL
clc; clear;

% determine action needed based on input values

% INPUTS
temp = input('Tempature:  ');
bpm = input('Heart rate:  ');

% OUTPUTS
er = 'Send to ER\n';
rv = 'Request Dr visit\n';
gm = 'Give prescribed medication\n';
na = 'Normal/No Action\n';

% CONDITIONALS
if or(temp  > 103, bpm > 110)
    fprintf(er)
elseif or(temp > 100, bpm > 95)
    fprintf(rv)
elseif or(temp > 99, bpm > 85)
    fprintf(gm)
else
    fprintf(na)
end
