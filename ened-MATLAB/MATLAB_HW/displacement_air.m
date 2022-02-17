% Homework 5.2: MATLAB 3
% Description:
% This program allows a user to input initial speed (in m/s) then
% calculates the y-displacement for each time interval, for two cases;
% an projectile not affected by air friction, and the same object affected
% by air friction. It calculates until one of the cases yeilds a point
% back at ground level. It then plots these two cases on a time vs
% displacement graph.

clc; clear;

%%% VARIABLES & CONSTANTS
P = 1.2;            % kg/m^3        (air density)
r = 0.04;           % m             (radius)
A = pi * r^2;       % m^2           (area)
m = 0.15;           % kg            (mass)
t = 0.1;            % s             (time interval)
g = 9.8;            % m/s^2         (gravity acceleration)
C = 0.5;            %               (drag coefficient)

D = (P * C * A) / 2;      % drag force


%%% INPUT
Vy0 = input('initial speed (m/s):  ');      % initial speed


%%% CALCULATE v, a, y FOR n = 0, n = 1
    % no air friction   (initials)
y = 0;                     %n=0
Vy = Vy0;                  %n=1
ay = -g;                   %n
    % air friction      (initials)
y_air = 0;                 %n=0
Vy_air = Vy0;              %n=0
ay_air = -g - (D / m) * abs(Vy0) * Vy0; %n=0

%%% GET POINTS
    % arrays for y displacement
Y = [];                         % no air friction
Y_air = [];                     % air friction

    % get points & add to arrays
while and(y >= 0, y_air >= 0)
    Y = [Y, y];
    Y_air = [Y_air, y_air];
%no air friction
    Vy = Vy - g * t;
    y = y + (Vy * t) + (1/2) * ay * t^2;
%air friction
    Vy_air = Vy_air + (ay_air * t);
    ay_air = -g - (D / m) * abs(Vy_air) * Vy_air;
    y_air = y_air + (Vy_air * t) + (1/2) * (ay_air * t^2);
end

    % add last points 
Y = [Y, y];
Y_air = [Y_air, y_air];
    % number of points
len_y = length(Y);

    % plot points
t = linspace(0, t, len_y);
    plot(t, Y, t, Y_air)
    title('y-displacement vs time')
    xlabel('time (s)')
    ylabel('y-displacement (m)')
    legend({'without air friction','with air friction'}, ...
        'location','southwest')



