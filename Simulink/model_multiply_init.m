function [input, model_parameters] = model_multiply_init()
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
    const = zeros(1,length(time));
    const(uint32(length(const)/3):uint32(2*length(const)/3)) = 1;
    const(uint32(2*length(const)/3):end) = 2;
    input.tdata  = timeseries(time, time, 'Name', 'tdata');
    input.tvalid = timeseries(ones(1,length(time)), time, 'Name', 'tvalid');
    input.tlast  = timeseries([zeros(1,length(time)-1) 1], time, 'Name', 'tlast');
    input.tready = timeseries([ones(1,length(time)-1) 1], time, 'Name', 'tready');
    input.const  = timeseries(const, time, 'Name', 'key');
end