% Description:
% This Matlab script produces a table to display columns for size of city,
% efficiency, m^2 of solar panels needed to supply city with energy, number
% of solar panels needed, and cost of panels needed. 

clc; clear;

% average houshold uses 13000 kilo Watt-hours of electricity per year
% sun produces aproximately 1370 Watt-hours per m^2 per day


% VARIABLES

nrow = 20; ncol = 5;        %number of rows/columns
arr = zeros(nrow, ncol);

% ADD HOUSEHOLDS

for i=1:4
    arr(i,1) = 5000;
    arr(i+4,1) = 10000;
    arr(i+8,1) = 20000;
    arr(i+12,1) = 50000;
    arr(i+16,1) = 100000;
end

% ADD EFFICIENCIES
ii = 20;

for i=1:5
    for j=1:4
        arr(ii,2) = j*10;
        ii = ii - 1;
    end
end

% ADD SOLAR PANEL VALUES

for i=1:nrow
    % ADD m^2 SOLAR CELLS
    house_watts = 13000 * 1000;             %watts per house per year
    sun_watts = 1370 * 365;                 %watts per m^2 per year (sun)
    need = arr(i,1) .* house_watts;         %electricity for houses   
    eff = arr(i,2) / 100;                   %efficiency
    arr(i,3) = need / (sun_watts * eff);
    % ADD NUM SOLAR PANELS
    arr(i,4) = arr(i,3) / 1.4;              %number of panels
    % ADD COST SOLAR PANELS
    if arr(i,2) == 40
        arr(i,5) = arr(i,4) * 290;
    elseif arr(i,2) == 30
        arr(i,5) = arr(i,4) * 260;
    elseif arr(i,2) == 20
        arr(i,5) = arr(i,4) * 200;
    else
        arr(i,5) = arr(i,4) * 150;
    end
end
