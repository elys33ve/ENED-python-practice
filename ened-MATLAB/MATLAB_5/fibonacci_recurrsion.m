% ACT_MATLAB_6p6
% MATLAB FUNCTIONS (RECURRSION)
clc; clear;

% calculate Fibonacci nth term using recurrsion
% F(n) = F(n-1) + F(n-2)

% (input n into function arg to call)

% DEF Fibonacci FUNCTION

function x = fibonacci(n)
    if x > 1
        x = fibonacci(n-1) + fibonacci(n-2);
        n = x;
    elseif x == 1                   % n = 1
        x = 1;
    elseif x <= 0                   % no no infinite recurrsion
        x = 0;
    end
end



