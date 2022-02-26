% ACT_MATLAB_2p2d
% MATLAB REPETITION (WHILE LOOP) 
clc; clear;

% calculate Fibonacci sequence until input >= output nth term
% F(n) = F(n-1) + F(n-2)

% INPUT
n = input('n:  ');

% CALCULATIONS & OUTPUT
fprintf('\nFibonacci sequence:\n')

if n < 0
    fprintf('-1\n')
elseif n >= 0
    fprintf('0\n')
end
if n >= 1
    fprintf('1\n')
end
if n > 1
    x = 1;
    y = 0;
    while x < n
        z = x;
        x = x + y;
        y = z;
        if x <= n
            fprintf('%d\n', x)
        end
    end
end




