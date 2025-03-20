import pygame
import os

pygame.init()

def play_audio(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def pause_audio():
    pygame.mixer.music.pause()

def unpause_audio():
    pygame.mixer.music.unpause()

def list_audio_files(directory):
    audio_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    return audio_files

def main():
    audio_directory = "audio"
    audio_files = list_audio_files(audio_directory)

    if not audio_files:
        print("No audio files found in the directory.")
        return

    print("Available audio files:")
    for i, file in enumerate(audio_files):
        print(f"{i + 1}. {file}")

    choice = int(input("Select a file by number: ")) - 1

    if choice < 0 or choice >= len(audio_files):
        print("Invalid choice.")
        return

    selected_file = os.path.join(audio_directory, audio_files[choice])
    play_audio(selected_file)

    while True:
        print("\n1. Pause")
        print("2. Unpause")
        print("3. Stop")
        print("4. Exit")
        action = input("Choose an action: ")

        if action == '1':
            pause_audio()
        elif action == '2':
            unpause_audio()
        elif action == '3':
            stop_audio()
            break
        elif action == '4':
            stop_audio()
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()