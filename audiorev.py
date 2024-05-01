from pydub import AudioSegment

def reverse_audio(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    reversed_audio = audio.reverse()
    reversed_audio.export(output_file, format="wav")
if __name__ == "__main__":
    input_file = "/home/rguktrkvaleey/Downloads/Classical.wav"
    output_file = "reversed_audio.wav"
    reverse_audio(input_file, output_file)

