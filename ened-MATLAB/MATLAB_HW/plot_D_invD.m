% Homework: MATLAB 3

clc; clear;

%%% VARIABLES
R = 8.31;           % gas constant (J/(mol*K))
    
    % Alpha Fe
D0a = 0.0062;       % (cm^2/s)
Qda = 80000;        % (J/mol)
    % Gamma Fe
D0g = 0.23;         % (cm^2/s)
Qdg = 148000;       % (J/mol)

    % Temperature (from deg C to K)
%Tk1 = 25 + 273.15;
%Tk2 = 1000 + 273.15;
% = 5 + 273.15;

%%% PLOT
subplot(2,1,1)
T = 25:5:1000;                  % temperature (C)       
    Da = D0a * exp(-(Qda ./ (R * (T + 273.15))));
    Da_i = D0a * exp(-(Qda ./ (R * (T + 273.15).^(-1))));
    plot(T, Da, T, Da_i)


subplot(2,1,2)
T = 25:5:1000;                  % temperature (C)
    Dg = D0g * exp(-(Qdg ./ (R * (T + 273.15))));           % temp
    Dg_i = D0g * exp(-(Qdg ./ (R * (T + 273.15).^(-1))));
    plot(T, Dg, T, Dg_i)
