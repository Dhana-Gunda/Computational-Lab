t = 0:0.01:1;

sin_dict = struct('s1', [2, 5], 's2', [11, 17], 's3', [12, 20], 's4', [20, 30], 's5', [24, 50]);

h = input('Enter sinusoidal key to generate: ', 's');

if isfield(sin_dict, h)
    x = sin_dict.(h)(1) * sin(2 * pi * sin_dict.(h)(2) * t);
    plot(t, x);
    xlabel('Time');
    ylabel('Amplitude');
    title(['Sinusoidal Signal for ', h]);
    grid on;
    legend(h);
    axis tight;
    show();
else
    disp('Invalid key entered. Please choose from the following keys:');
    disp(fieldnames(sin_dict)');
end
