% MATLAB 5: Task 2
% File:     ACT_MATLAB_6p2_TEAM256.m

clc; clear;


% INPUTS
AWG = input('AWG:  ');
L = input('length (m):  ');

% MATERIALS INPUT
materials = {'g','gold','c','copper','i','iron'};
m_valid = false;

    % check valid/in cell
while m_valid == false                  
    m = input('material:  ','s');
    x = find(strcmp(materials, m));
    if x > 0
       m_valid = true; 
    end
end

    % find material resistivity (ohms*m)
if or(m == 'gold', m == 'g')            
    p = 2.4*10^(-8);
elseif or(m == 'coppoer', m == 'c')
    p = 1.7*10^(-8);
elseif or(m == 'iron', m == 'i')
    p = 1.0*10^(-7);
end

% GET FUNCTION VALUES
[D] = Wire_Diameter(AWG);
[R] = Wire_Resistance(p, L, D);

% OUPUTS
fprintf('Resistance:  %d\n', R);
