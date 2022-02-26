% ACT_MATLAB_2p2c
% MATLAB REPETITION (FOR LOOP) 
clc; clear;

% calculate Fibonacci sequence to the nth term
% F(n) = F(n-1) + F(n-2)

% INPUT
n = input('n:  ');          % nth term/stop point

% LOOP & OUTPUT
fprintf('\nFibonacci sequence:\n')

if n < 0                    % n < 0
    fprintf('-1\n')
else
    for i=0:n
        if i == 0           % n = 0
            x = 0;
        elseif i == 1       % n = 1
            x = 1;
            y = 0;
        else                % n > 1
            z = x;
            x = x + y;
            y = z;
        end
        fprintf('%d\n', x)
    end
end

