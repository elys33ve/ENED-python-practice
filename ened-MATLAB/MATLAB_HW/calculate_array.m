% Description:
% Generate rand int between 1 and 6 for 2D array. Calculate mean value for 
% each row, save the mean values to a 1D array. Count num rows with mean 
% value range 3.44 to 3.56 (include bounds). Calculate percent rows with 
% mean withing range. Output percentage to cmd window w 2 decimal places. 
% Plot mean values on y-axis and row number on x-axis. Include title and 
% labels.
clear all; clc;

%%%%%   random array
rng(3);
A = randi([1, 6], 100,300);     % 2D array 100r,300c --> randnum [1,6]

%%% CALC MEAN VALUE
avg = zeros(100);           % array of means

for i = 1:100                   % rows
    sum = 0;
    for j = 1:300               % columns
        sum = sum + A(i,j);         % get sum of row
    end
    mean = sum / 300;
    avg(i) = mean;
end

%%% COUNT IN RANGE
sum = 0;

for i = 1:100
    if avg(i) >= 3.44 && avg(i) <= 3.56     % numbers in range
        sum = sum + 1;
    end
end

in_range = sum / 100;      % decimal form percentage
fprintf('in range: %0.2f\n', in_range)

%%% PLOT

i = 1:1:100;
    plot(i,avg(i),'-k','LineWidth',2)
       xlabel('row number')
       ylabel('mean values')
       title('Plotted Mean Values')

