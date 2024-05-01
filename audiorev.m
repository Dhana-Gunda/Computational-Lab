inputFileName='input_audio.wav';
outputFileName='reversed_audio.wav';
[inputData,sampleRate]=audioread("/home/rguktrkvaleey/Downloads/Jingle.wav");
reversedData=flipud(inputData);
audiowrite(outputFileName,reversedData,sampleRate);
disp('Audio file is reversed and saved successfully.');