function [input, model_parameters] = model_init()
    %% MODEL PARAMETERS
    % Model sampling rate
    sampling_rate = 100e6;
    t_ini = 0; % Simulation initial time in seconds
    t_end = 0.02; % Simulation ending time in seconds
    model_parameters.sampling_rate = sampling_rate;
    model_parameters.ini = t_ini;
    model_parameters.end = t_end;
    %% MODEL INPUTS
    % Inputs generated as timeseries with a series of values and times samples
    % at sampling rate
    % Time vector generation
    time = t_ini:1/sampling_rate:t_end;
    % Signals generation
    f1  = 20e6;
    f2  = 40e6;
    amp = 1;
    signal = amp*(sin(2*pi*f1.*time) + sin(2*pi*f2.*time));
    key = zeros(1,length(time));
    key(uint32(length(key)/3):uint32(2*length(key)/3)) = 1;
    key(uint32(2*length(key)/3):end) = 2;
    input.tdata  = timeseries(signal, time, 'Name', 'tdata');
    input.tvalid = timeseries(ones(1,length(time)), time, 'Name', 'tvalid');
    input.tlast  = timeseries([zeros(1,length(time)-1) 1], time, 'Name', 'tlast');
    input.tready = timeseries([ones(1,length(time)-1) 1], time, 'Name', 'tready');
    input.key    = timeseries(key, time, 'Name', 'key');
end