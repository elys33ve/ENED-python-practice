% Homework 4.2: MATLAB 2 - Repetition
% Description:
% This script prompts a user for the number of rounds (n) and the name of
% each player (p1n & p2n). It then determines the Driver (d) and the 
% Follower (f) and keeps track of the score for each player. Each round, 
% it displays the winner and after the final round, it outputs the total 
% score for each player.

clc; clear;

% SET VARIABLES
d_score = 0;                 % driver score
f_score = 0;                 % follower score


% INTPUTS
p1n = input('Player 1 name:  ', 's');
p2n = input('Player 2 name:  ', 's');
n = input('Number of attempts:  ');


% INITIAL DICE ROLL (+ set follower and driver)
p1d =  randi([1, 6], 1);        % p1 dice roll
p2d =  randi([1, 6], 1);        % p2 dice roll

while p1d == p2d                        % while tied --> repeat rolls
    fprintf('It was a tie, please roll again\n')
    p1d =  randi([1, 6], 1);
    p2d =  randi([1, 6], 1);
end

if p1d > p2d                            % p1 dice higher - driver
    d = p1d;            % driver dice value
    dn = p1n;      % set p1 (name) to driver
    fn = p2n;      % set p2 to follower
    fprintf('The Driver is %s, the Follower is %s\n', p1n, p2n)
else                                    % p2 dice higher - driver
    d = p2d;            % driver dice value
    dn = p2n;      % set p2 (name) to driver
    fn = p1n;      % set p1 to follower
    fprintf('The Driver is %s, the Follower is %s\n', p2n, p1n)
end


% GAME PART
for i=1 : n   % for num of attempts
    f = randi([1, 6], 1);   % follower rolls dice  
    if f == d
        fprintf('The winner of round %d is %s\n', i, fn)
        f_score = f_score + 1;      % follower wins 
    else 
        fprintf('The winner of round %d is %s\n', i, dn)
        d_score = d_score + 1;      % driver wins
    end
    %fprintf('%s = %d, %s = %d\n', dn, d, fn, f)
end


% END OUTPUTS
if d_score > f_score                    % driver wins
    fprintf('The winner is %s\n', dn)
elseif f_score > d_score                % follower wins
    fprintf('The winner is %s\n', fn)
else                                    % tie
    fprintf('It was a tie\n')
end

fprintf('%s''s total score: %d\n', dn, d_score)     % driver score
fprintf('%s''s total score: %d\n', fn, f_score)     % follower score

