% Homework 6.2: MATLAB
% Description:
% This script takes a matrix and calculates the sum of values in odd
% numbered columns, sum of values along the diagonal, and sum of values
% above and to the right of the diagonal.

clc; clear;

% VARIABLES & CONSTANTS
A = [-4 2 -7 6 8 ; 4 -5 8 -1 0 ; 0 -4 3 1 10 ; -8 7 -10 5 -2];

s = size(A);        % size of matrix
sr = s(1);          % number of rows
sc = s(2);          % number of columns

%%% SUBTASK 1: SUM VALUES IN ODD COLUMNS
sum1 = 0;

for i=1:sr
    for j=1:sc
        if mod(j,2) ~= 0
            sum1 = sum1 + A(i,j);
        end
    end
end

fprintf('sum of values in odd columns:  %d\n', sum1)

%%% SUBTASK 2: SUM VALUES ALONG DIAGONAL
sum2 = 0;
    
    % find smaller value
if sr > sc
    x = sc;
else
    x = sr;
end
    
    % iterate through matrix
for i=1:x
    sum2 = sum2 + A(i,i);
end

fprintf('sum of values along diagonal:  %d\n', sum2)

%%% SUBTASK 3: SUM VALUES ABOVE & RIGHT OF DIAGONAL
sum3 = 0;

for i=1:sr
    for j=1:sc
        if j > i
            sum3 = sum3 + A(i,j);
        end
    end
end

fprintf('sum of values above and right of diagonal:  %d\n', sum3)

