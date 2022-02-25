% MATLAB 4: 2D Arrays
% File:     ACT_MATLAB_4p3_TEAM256.m
% uses Arm_Fracture.jpg

clear; clc;

%%% GET JPG
pic = imread('Arm_Fracture.jpg');
s = size(pic);

%%% INPUT
s1 = input('starting row:  ');
s2 = input('starting column:  ');
nrow = input('number of rows:  ');
ncol = input('number of columns:  ');

%%% LOOP
pic2 = zeros(nrow,ncol);

for i=1:nrow        %1 to num rows
    ii = i-1;       %i start 0
    for j=1:ncol        %1 to num col
        jj = j-1;       %j start 0
        pic2(i,j) = pic(s1+ii,s2+jj);
    end
end

%%% DISPLAY
pic2 = uint8(pic2);
figure(1); imshow(pic2);
figure(2); imshow(pic(s1:s1+nrow,s2:s2+ncol));





