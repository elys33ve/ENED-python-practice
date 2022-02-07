% ACT_MATLAB_2p3
% MATLAB 2: REPETITION 
clc; clear;

% input pos whole number for n. check validity
% if odd, multiply by 3, add 1
% if even, divide by 2
% generate outputs until 1 is reached

% INPUT
n = input('posative whole number:  ');

% CHECK INPUT VALIDITY
while or(n < 1, (floor(n) ~= n))
    n = input('input a posative whole number:   ');
end

% GENERATE OUTPUTS
while n ~= 1                    % while n isnt 1
    if mod(n, 2) == 0       % even numbers
        n = n / 2;
    else                    % odd numbers
        n = (n * 3) + 1;
    end
    fprintf("%d    ", n)
end

fprintf("\n")
