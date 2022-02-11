% ACT_MATLAB_2p2b
% MATLAB 2: REPETITION 
clc; clear;

% calculate Jacobsthal numbers until < or = to input
% J(n) = J(n-1)+2J(n-2)

% INPUT & VARIABLES
n = input('n:\n');

x = 1;
y = 0;

% CALCULATIONS & OUTPUT
fprintf('\nJacobsthal sequence:\n')
fprintf('0\n1\n')

while x < n
    z = x;
    x = x + (2 * y);
    y = z;
    if x < n
        fprintf('%d\n', x)
    end
end


%---------------------------------------------------------------------
% n| Jn-2    Jn-1    Jn
% 0| x       x       0
% 1| x       0       1
% 2| 0       1       1
% 3| 1       1       3
% 4| 1       3       5
% 5| 3       5       11
% 6| 5       11      21
% 7| 11      21      43
