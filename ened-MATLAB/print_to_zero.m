% ACT_MATLAB_2p1
% MATLAB 2: REPETITION
clc; clear;

% print from inputted value to zero, then print sum of sequence

% INPUT & VARIABLES
user = input('Enter an integer:  \n');

s = 0;         %sum of sequence

% OUTPUT & FOR LOOP
fprintf("The sequence is:\n")

if user > 0                     %for posative input
    for i = 0:user
        x = user - i;
        fprintf('%d\n', x)
        s = s + x;          %sum
    end
elseif user < 0                 %for negative input
    for i = 0:abs(user)
        x = user + i;
        fprintf('%d\n', x)
        s = s + x;          %sum
    end
else                            %for input = 0
    fprintf('0\n')
end

fprintf('Sequence sum:  %d\n', s)

