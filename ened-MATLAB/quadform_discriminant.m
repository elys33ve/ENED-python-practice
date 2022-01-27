% ACT_MATLAB_1p2
clc; clear;     %clear cmd window, clear variables

% INPUTS
a = input('a: ');
b = input('b: ');
c = input('c: ');

% OTHER SHIT
D = (b ^ 2) - (4 * a * c);

% OUTPUTS & STUFF
fprintf('D is ')

if D > 0                    % pos
    fprintf('Real\n')
elseif D == 0               % zero
    fprintf('Repeated\n')
else                        % neg
    fprintf('Complex\n')
end
