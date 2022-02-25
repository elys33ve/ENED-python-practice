% MATLAB 5: Task 1
% File:     Forces.m

% FORCES FUNCTION
function [Fr, Th_r] = Forces(F1, theta1, F2, theta2, units)

        % convert angle 
    while not(or(or(units == 'D', units == 'degrees'), or(units == 'R', units == 'radians')))
        if or(units == 'D', units == 'degrees')
            theta1 = theta1 * (pi/180);
            theta2 = theta2 * (pi/180);
        end
    end

        % caclulate x & y components
    F1x = abs(F1) * cos(theta1);
    F1y = abs(F1) * sin(theta1);

    F2x = abs(F2) * cos(theta2);
    F2y = abs(F2) * sin(theta2);
        
        % caculate x & y resultant forces
    Frx = F1x + F2x;
    Fry = F1y + F2y;

        % calculate Fr
    Fr = sqrt(Frx^2 + Fry^2);
    
        % calculate Th_r
    if Frx >= 0
        Th_r = atan(Fry/Frx);
    else
        Th_r = atan(Fry/Frx) + pi;
    end

end





