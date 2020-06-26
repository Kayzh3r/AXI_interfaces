function [output_signal] = switch_output(inputArg0,inputArg1,inputArg2,selector)
%SWITCH_OUTPUT Summary of this function goes here
%   Detailed explanation goes here
persistent state, state = xl_state(0,{xlUnsigned, 3, 0});
switch selector
    case 0
        state = inputArg0;
    case 1
        state = inputArg1;
    case 2
        state = inputArg2;
    otherwise
end
output_signal = state;

