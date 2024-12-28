from lib.regex import parse_numbers
from lib.math import get_nth_digit


class IntcodeException(Exception):
    pass


class IntcodeMemory:
    def __init__(self, initial_state: list[int] = []):
        self._state = initial_state.copy()

    def _expand(self, index):
        """Expand memory with zeros for an index value that exceeds current memory"""
        if index >= len(self._state):
            self._state += [0] * (index + 1 - len(self._state))

    def __getitem__(self, index: int):
        self._expand(index)

        return self._state[index]

    def __setitem__(self, index: int, value: int):
        self._expand(index)

        self._state[index] = value

    def __iter__(self):
        for value in self._state:
            yield value


class Intcode:
    def __init__(
        self,
        program: list[int],
        pause_on_input=False,
        output_as_array=False,
        initial_pointer=0,
    ):
        self.program = program
        self.reset()
        self.pointer = initial_pointer
        self.pause_on_input = pause_on_input
        self.output_as_array = output_as_array

    def reset(self):
        self.pointer = 0
        self.memory = IntcodeMemory(self.program)
        self.value = None
        self.current_instruction = 0
        self.current_instruction_pointer = 0
        self.relative_base = 0

    def _read_next(self):
        """Read next integer from pointer position, and move pointer one step."""
        output = self.memory[self.pointer]
        self.pointer += 1
        return output

    def _read(self, num_positions: int):
        """Read `num_positions` integers from pointer position, and move pointer accordingly."""
        output = self.memory[self.pointer : self.pointer + num_positions]
        self.pointer += num_positions
        return output

    def _get_param(self, mode="r"):
        value = self._read_next()
        parameter_position = 1 + self.pointer - self.current_instruction_pointer

        match get_nth_digit(self.current_instruction, parameter_position):
            case 0:  # Position mode
                pointer = value
            case 1:  # Immediate mode (only in read mode, so we can return it directly)
                if mode == "w":
                    raise IntcodeException("Parameter mode 1 does not support writing")

                return value
            case 2:  # Relative mode
                pointer = self.relative_base + value
            case _ as parameter_mode:
                raise IntcodeException(
                    f"Parameter mode {parameter_mode} not recognized"
                )

        match mode:
            case "r":  # Read value at pointer position from memory
                return self.memory[pointer]
            case "w":  # Return pointer position for writing
                return pointer
            case _ as mode:
                raise IntcodeException(f"Mode {mode} not supported")

    def _get_params(self, num_params: int, *args, **kwargs):
        parameter_position = 2
        params: list[int] = []

        for _ in range(num_params):
            param = self._get_param(*args, **kwargs)
            params.append(param)
            parameter_position += 1

        return params

    def run(self, *program_inputs: list[int], reset=False):
        program_inputs = list(program_inputs)

        if self.output_as_array:
            self.value = []

        while True:
            self.current_instruction = self._read_next()
            self.current_instruction_pointer = self.pointer

            match self.current_instruction % 100:
                # Day 2
                case 1 | 2 as opcode:
                    # Add (1) or multiply (2) the numbers at positions p1 and p2 and write the output to p3
                    p1, p2 = self._get_params(2)
                    p3 = self._get_param("w")

                    self.memory[p3] = p1 + p2 if opcode == 1 else p1 * p2

                # Day 5, part a
                case 3:  # Write input to position p1
                    if program_inputs:
                        program_input = program_inputs.pop(0)
                    elif self.pause_on_input:
                        self.pointer -= 1
                        return self.value
                    else:
                        raise IntcodeException("Additional input is required")

                    p1 = self._get_param("w")

                    self.memory[p1] = program_input
                case 4:  # Write parameter value to output
                    p1 = self._get_param()

                    if self.output_as_array:
                        self.value.append(p1)
                    else:
                        self.value = p1

                # Day 5, part b
                case 5:  # Jump to second paramter if first is non-zero
                    p1, p2 = self._get_params(2)

                    if p1 != 0:
                        self.pointer = p2
                case 6:  # Jump to second paramter if first is zero
                    p1, p2 = self._get_params(2)

                    if p1 == 0:
                        self.pointer = p2
                case 7:  # Set value of
                    p1, p2 = self._get_params(2)
                    p3 = self._get_param("w")

                    self.memory[p3] = int(p1 < p2)
                case 8:  # Equals
                    p1, p2 = self._get_params(2)
                    p3 = self._get_param("w")

                    self.memory[p3] = int(p1 == p2)

                # Day 9
                case 9:
                    p1 = self._get_param()

                    self.relative_base += p1

                # Day 2
                case 99:
                    break
                case _ as opcode:
                    raise IntcodeException(f"Unknown opcode: {opcode}")

        program_output = self.value

        if reset:
            self.reset()

        return program_output

    def copy(self):
        return Intcode(
            list(self.memory),
            pause_on_input=self.pause_on_input,
            output_as_array=self.output_as_array,
            initial_pointer=self.pointer,
        )

    @property
    def has_terminated(self):
        return self.current_instruction == 99

    @classmethod
    def parse_input(cls, input_string: str, *args, **kwargs):
        program = parse_numbers(input_string, include_negative=True)

        return cls(program, *args, **kwargs)
