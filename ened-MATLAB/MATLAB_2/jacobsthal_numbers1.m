% ACT_MATLAB_2p2a
% MATLAB 2: REPETITION 
clc; clear;

% calculate Jacobsthal numbers to the nth term
% J(n) = J(n-1)+2J(n-2)

% INPUT & VARIABLES
n = input('n:\n');

% CALCULATIONS & OUTPUT
fprintf('\nJacobsthal sequence:\n')

for i = 0:n
    if i <= 0
        x = 0;
    elseif i == 1
        x = 1;
        y = 0;
    else
        z = x;
        x = x + (2 * y);
        y = z;
    end
    fprintf('%d\n', x)
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
