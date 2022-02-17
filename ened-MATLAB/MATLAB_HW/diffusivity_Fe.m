% Homework 5.2: MATLAB 3
% Description:
% This program calculates the diffusivity of two types of iron and creates
% four subplots (rectangle, semilogx, semilogy, loglog) for diffusivity vs
% inverse temerature.

clc; clear;

%%% VARIABLES
R = 8.31;           % gas constant (J/(mol*K))
    
    % Alpha Fe
D0a = 0.0062;       % (cm^2/s)
Qda = 80000;        % (J/mol)
    % Gamma Fe
D0g = 0.23;         % (cm^2/s)
Qdg = 148000;       % (J/mol)

    % temperature (from deg C to K)
Tk1 = 25 + 273.15; 
Tk2 = 1000 + 273.15; 
Tk = 5 + 273.15;


%%% PLOT
subplot(2,2,1)   % plot (rectangle???)
T = Tk1:Tk:Tk2;               % temperature (K)
Ti = 1 ./ T;
    Da = D0a * exp(-(Qda * Ti ./ R));  % Diffusivity alpha (cm^2/s)
    Dg = D0g * exp(-(Qdg * Ti ./ R));  % Diffusivity gamma (cm^2/s)
    plot(T, Da, T, Dg)
    %rectangle('position',[min(T) min(min(Da,Dg)) max(T) max(max(Da,Dg))])???
    xlabel('(1/K)')
    ylabel('(cm^2/s)')
    title('rectangle')
    legend({'Alpha Fe','Gamma Fe'},'Location','northwest')
    legend('boxoff')

subplot(2,2,2)                              % semi-log x
    semilogx(T, Da, T, Dg)
    xlabel('log(1/K)')
    ylabel('(cm^2/s)')
    title('semi-log x')
    legend({'Alpha Fe','Gamma Fe'},'Location','northwest')
    legend('boxoff')
    
subplot(2,2,3)                              % semi-log y
    semilogy(T, Da, T, Dg)
    xlabel('(1/K)')
    ylabel('log(cm^2/s)')
    title('semi-log y')
    legend({'Alpha Fe','Gamma Fe'},'Location','southeast')
    legend('boxoff')

subplot(2,2,4)                              % log-log
    loglog(T, Da, T, Dg)
    xlabel('log(1/K)')
    ylabel('log(cm^2/s)')
    title('log-log')
    legend({'Alpha Fe','Gamma Fe'},'Location','southeast')
    legend('boxoff')

