% ACT_MATLAB_3
% MATLAB 3: 1-D ARRAYS AND PLOTTING 
clc; clear;

% INTERVALS
x1 = -5;
x2 = 10;

t1 = 0;
t2 = 10;

% PLOT
subplot(2,1,1)
x = x1:1:x2; 
       y = (1/3)*x.^4 - 2*x.^3 - 2.3*x.^2 + 6*x + 4; 
       plot(x,y,'-k','LineWidth',2)
       xlabel('x')
       ylabel('y')
       title('y vs x')

subplot(2,1,2)
t = t1:1:t2;
       f = 300 * sqrt(t);
       plot(t,f,'-k','LineWidth',2)
       xlabel('t')
       ylabel('f')
       title('f vs t')

%-------------------------------------------------------------------------
% xlabel
% ylabel
% legend 
% title 

% COLOR ------
% y -yellow
% m -magenta
% c -cyan
% r -red
% g -green
% b -blue
% w -white
% k -black

% STYLE ------
% - Solid line (default)
% -- Dashed line
% : Dotted line
% -. Dash-dot line

% MARKER ------
% o Circle
% + Plus sign
% * Asterisk
% . Point
% x Cross
% s Square
% d Diamond
% ^ Upward-pointing triangle
% v Downward-pointing triangle
% > Right-pointing triangle
% < Left-pointing triangle
% p Pentagram
% h Hexagram

