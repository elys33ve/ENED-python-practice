% ACT_MATLAB_1p3
clc; clear;
% determine quadrant of a point

% INPUTS
x = input('x coordinate: ');
y = input('y coordinate: ');

% DETERMINE QUADRANT
fprintf('(%d,%d) is ', x, y)

if x > 0
    if y > 0
        fprintf('in quadrant 1\n')
    elseif y < 0
        fprintf('in quadrant 4\n')
    else
        fprintf('on the x-axis\n')
    end
elseif x < 0
    if y > 0
        fprintf('in quadrant 2\n')
    elseif y < 0
        fprintf('in quadrant 3\n')
    else
        fprintf('on the y-axis\n')
    end
else
    fprintf('on the origin\n')
end
