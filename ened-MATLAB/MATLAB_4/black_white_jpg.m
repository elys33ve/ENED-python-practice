% MATLAB 4: 2D Arrays
% Turn a jpg picture from greyscale to black and white

clc; clear;

%%% GET JPG
pic = imread('Arm_Fracture.jpg');

%%% INPUT
t = input('threshold value:  ');

%%% VALIDATE
while or(t > 255, t < 0)
    fprintf('invalid value\n')
    t = input('threshold value:  ');
end

%%% LOOP THROUGH VALUES
s = size(pic);

for i=1:s(1)
    for j=1:s(2)
        if pic(i,j) > t
            pic(i,j) = 255;
        elseif pic(i,j) < t
            pic(i,j) = 0;
        end
    end
end

%%% DISPLAY PIC
figure(1); imshow(pic);
