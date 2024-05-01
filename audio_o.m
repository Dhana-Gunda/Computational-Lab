file_path = '/home/rguktrkvalley/python(Cl)/Chorus.wav';
[data_audio, sample] = audioread(file_path);
timing= (0:length(data_audio)-1) / sample;
plot(timing, data_audio);
xlabel('Time (s)');
ylabel('Amplitude');
title('Audio Signal');
