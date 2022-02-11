% ACT_MATLAB_3
% MATLAB 3: 1-D ARRAYS AND PLOTTING
clc; clear;

% VARIABLES
T = [7, 9, -8, 9, 3, -8, -5, 1, 10, 10, 0, -7]; % deg F over 12 days

mean_pos = (7 + 9 + 9 + 3 + 1 + 10 + 10)/7;     % control p
mean_neg = (-8 + -8 + -5 + -7)/4;                   % control n

len = length(T);

% AVERAGE OF POSATIVE AND NEGATIVE VALUES
p = 0;
n = 0;
p_sum = 0;
n_sum = 0;

for i=1 : len
    if T(i) > 0         % posative
        p_sum = p_sum + T(i);
        p = p + 1;
    elseif T(i) < 0     % negative
        n_sum = n_sum + T(i);
        n = n + 1;
    end
end

p = p_sum/p;
n = n_sum/n;

% OUTPUTS
fprintf('posative mean: %d      (%d)\n', p, mean_pos)
fprintf('negative mean: %d      (%d)\n', n, mean_neg)

