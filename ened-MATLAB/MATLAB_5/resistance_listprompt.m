% MATLAB 5: Task 2
% File:     ACT_MATLAB_6p2_TEAM256.m

clc; clear;


% INPUTS
AWG = input('AWG:  ');
L = input('length (m):  ');

% MATERIALS INPUT
m1 = 'Material: ';                  % prompt
m2 = {'gold', 'copper', 'iron'};    % choices
m = menu(m1,m2);

    % find material resistivity (ohms*m)
if m == 1            
    fprintf('Material:  Gold\n')
    p = 2.4*10^(-8);
elseif m == 2
    fprintf('Material:  Copper\n')
    p = 1.7*10^(-8);
elseif m == 3
    fprintf('Material:  Iron\n')
    p = 1.0*10^(-7);
end

% GET FUNCTION VALUES
[D] = Wire_Diameter(AWG);
[R] = Wire_Resistance(p, L, D);

% OUPUTS
fprintf('Resistance:  %d\n', R);


