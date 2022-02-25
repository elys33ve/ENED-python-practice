% MATLAB 5: Task 2
% File:     Wire_Diameter.m



function [D] = Wire_Diameter(AWG)
    D = 0.1274 * 92^((36-AWG)/39);      % diameter in mm
end



