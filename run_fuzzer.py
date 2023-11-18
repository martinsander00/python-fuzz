import sys
import subprocess
import time
import os
from fuzzer import mutate

def main():
    if len(sys.argv) != 3:
        print("Usage: python fuzzer.py <target_program.py> <duration_in_seconds>")
        sys.exit(1)

    target_program = sys.argv[1]
    try:
        duration = int(sys.argv[2])
    except ValueError:
        print("Please specify the duration in seconds as an integer.")
        sys.exit(1)

    # Create a subfolder named after the target program
    folder_name = os.path.splitext(target_program)[0]
    os.makedirs(folder_name, exist_ok=True)

    # Open files for writing inputs and crashes
    inputs_file = open(os.path.join(folder_name, 'inputs.txt'), 'w')
    crashes_file = open(os.path.join(folder_name, 'crashes.txt'), 'w')

    with open('input.txt', 'r') as file:
        initial_input = file.readline().strip()

    mutated_input = initial_input
    start_time = time.time()
    input_count = 0
    crash_count = 0

    while True:
        if time.time() - start_time > duration:
            print("Fuzzing completed.")
            print(f"Total inputs tested: {input_count}")
            print(f"Total crashes detected: {crash_count}")
            inputs_file.close()
            crashes_file.close()
            return

        mutated_input = mutate(mutated_input)

        process = subprocess.Popen(['python3', target_program],
                                   stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                                   stderr=subprocess.PIPE)
        _, stderr = process.communicate(input=mutated_input.encode())

        # Write to inputs file
        inputs_file.write(mutated_input + '\n')
        inputs_file.flush()

        input_count += 1

        if stderr or process.returncode != 0:
            crash_count += 1
            # Write to crashes file and flush
            crashes_file.write(mutated_input + '\n')
            crashes_file.flush()
if __name__ == "__main__":
    main()